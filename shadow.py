from gasp import *
import numpy as np
import pyautogui 
import ctypes
import matplotlib.pyplot as plt



#Settings
back = color.BLACK
dot = color.WHITE
linec = color.GRAY
scale = 200
timestep = 0.05
distance = 2



centerx = 0
centery = 0

angle = 0

points = np.array([    #these are the points of the cube that will be generated

    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [0.5, 0.5, -0.5],
    [-0.5, 0.5, -0.5],

    [-0.5, -0.5, 0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, 0.5, 0.5]

])

def draw():

    rotationZ = np.array([           #set up rotation matricies for all dimensions
        # [np.cos(angle), -np.sin(angle), 0],
        # [np.sin(angle), np.cos(angle), 0],              #test matrix
        # [0, 0, 1]
        [1,0,0],
        [0,1,0],
        [0,0,1]


    ])

    rotationX = np.array([

        
        [1,0,0],
        [0,1,0],
        [0,0,1]
        

    ])

    rotationY = np.array([

        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0,0,0]

        
        # [np.cos(angle), 0, -np.sin(angle)],
        # [0, 1, 0],
        # [0,0,0]                                           #test matrix
        # #[np.sin(angle), 0, np.cos(angle)]

    ])

    projected = []

    for v in points: #produces rotated points
        rotatedY = np.matmul(rotationY, v)
        rotatedX = np.matmul(rotationX, rotatedY)
        rotatedZ = np.matmul(rotationZ, rotatedX)

        z = 1 / (distance - rotatedZ[2])
        projection = np.array([

            [z, 0, 0],
            [0, z, 0]

        ])

        projected2d = np.matmul(projection, rotatedZ)
        projected2d = projected2d * scale
        point(projected2d[0], projected2d[1])
        projected.append(projected2d)

    for i in range(4): #connects points correctly

        connect(i, (i + 1) % 4, projected) 
        connect(i + 4, ((i + 1) % 4) + 4, projected)
        connect(i, i + 4, projected)

def createWindow(): #returns the half the size of user's screen so the points can be centered on screen. Also creates the window showing the cube that is the size of the entire screen
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    begin_graphics(width=screensize[0], height=screensize[1], title="3D Renderer", background=back)
    return screensize[0]//2, screensize[1]//2

def point(x, y): #puts points in draw() function
    Circle((x + centerx, y + centery), 1, True, dot, 5) 

def connect(i, j, points): #connects points in previous draw() function
    print(points)

    a = points[i]
    b = points[j]
    
    Line((a[0] + centerx, a[1] + centery), (b[0] + centerx, b[1] + centery), linec)



def clear():
    clear_screen()

centerX, centerY = createWindow()
centerx = centerX
centery = centerY

num = 1 #photo num
while num <80: #takes screenshots of cube each time it rotates, to be analyzed later

    draw()
    time.sleep(timestep+1)
    clear()
    screenshot = pyautogui.screenshot()
    screenshot.save(r"INSERT_DIRECTORY\screenshot_{x}.jpg".format(x = num))
    angle = angle + 0.1    #rotation amount
    num +=1 # full rotation is 80 ticks 
clear()




def area_plot(): #ANALYZES THE SCREENSHOTS TAKEN
    import os
    import cv2

    
    os.chdir(r"INSERT DIRECTORY WHERE SCREENSHOTS ARE STOLEN") #changes directory to access all screenshots 
    all_areas = []
    num_of_photos = []
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    for i in range(1,80): #loops through 80 screenshots of projection
        num_of_photos.append(i)

        img = cv2.imread("screenshot_{x}.jpg".format(x=i))
        
        img = img[400: screensize[1]-400, 700: screensize[0]-700] #crops image

        size = img.shape #(y,x)
        # print(size)
        x = size[1]
        y = size[0]

        total_area = 0 
        
        for i in range(y):
            x_left = 0 
            x_right = x-1

            low_rgb_threshold = 128 
            high_rbg_threshold = 245
            
            while x_left < x_right:
                if low_rgb_threshold< img[i,x_right][0]< high_rbg_threshold and low_rgb_threshold < img[i,x_left][0] < high_rbg_threshold: #if both edges are gray and found
                    cv2.circle(img, (x_left,i), 1,(0,255,0), -1)
                    cv2.circle(img, (x_right,i), 1,(0,255,0), -1)
                    total_area += x_right - x_left
                    break
                elif low_rgb_threshold< img[i,x_right][0]<high_rbg_threshold: #if only right edge is found, increment the left
                    x_left +=1 
                elif low_rgb_threshold < img[i,x_left][0] < high_rbg_threshold: #if only left edge is found, increment the right
                    x_right -=1
                else:
                    x_left +=1 #no edge is found, increment both 
                    x_right -=1
        all_areas.append(total_area) #appends the area of a projection 

    plt.ylabel('Areas (Pixels^2)')
    plt.xlabel('screenshot num')
    plt.plot(num_of_photos, all_areas) #plots the photo num and the area of that photo 
    plt.show()
   
    # while(1): #display image until Esc is pressed

    #     cv2.imshow("Cross-Section",img)                #uncomment this chunk if displaying image is preferred
    #     if cv2.waitKey(20) & 0xFF ==27:
    #         break
    # return total_area


analyze = input("Proceed to Analyze (y/n)? ")
if analyze == "y":
    area_plot()


    
    
    
