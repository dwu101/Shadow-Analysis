from gasp import *
import numpy as np
import cv2 as cv2
import math 

#Settings
back = color.BLACK
dot = color.WHITE
linec = color.GRAY
scale = 200
timestep = 0.05
distance = 2

#Dont mess with the ones below

centerx = 0
centery = 0

angle = 0

points = np.array([

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

    rotationZ = np.array([ #These have to be inside the function because angle will still static when initiailzing.
        # [np.cos(angle), -np.sin(angle), 0],
        # [np.sin(angle), np.cos(angle), 0],
        # [0, 0, 1]
        [1,0,0],
        [0,1,0],
        [0,0,1]


    ])

    rotationX = np.array([

        
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0,0,0]
        # # [0, np.sin(angle), np.cos(angle)],

    ])

    rotationY = np.array([

        [1,0,0],
        [0,1,0],
        [0,0,1]
        # [np.cos(angle), 0, -np.sin(angle)],
        # [0, 1, 0],
        # [0,0,0]
        # #[np.sin(angle), 0, np.cos(angle)]

    ])

    projected = []

    for v in points:
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

    for i in range(4):
        # i = 0 : connect(0,1,4,5,0,4)
        #
        #
        #
        connect(i, (i + 1) % 4, projected)
        connect(i + 4, ((i + 1) % 4) + 4, projected)
        connect(i, i + 4, projected)

def createWindow():
    begin_graphics(width=800, height=600, title="3D Renderer", background=back)
    return 400, 300

def point(x, y):
    Circle((x + centerx, y + centery), 2, True, dot, 5)

def connect(i, j, points):
    print(points)

    a = points[i]
    b = points[j]
    # c = points[k]
    # d = points[l]
    # e = points[m]
    # f = points[n]
    # temp1 = (a,b,c,d,e,f)
    # new = []
    
    # for index in range(len(temp1)):
    #     for index_check in range(index, len(temp1)):
    #         if temp1[index][0] == temp1[index_check][0] and temp1[index][1] == temp1[index_check][1]:
    #             continue
    #         else:
    #             new.append(temp1[index]) 
    
    # new = tuple(new)

    # point1 = (a[0] + centerx, a[1] + centery)
    # point2 = (b[0] + centerx, b[1] + centery)
    # Box(point1, math.fabs(point1[1]-point2[1]) , math.fabs(point1[0] - point2[0]), True, linec, 10)
    Line((a[0] + centerx, a[1] + centery), (b[0] + centerx, b[1] + centery), linec)

    # Polygon(new, True, color.WHITE, 1)
    # Circle(point1, 10, True, color.WHITE, 5)
     ###the problem is that i want to shade the faces in so i can analyze them. perhaps finding the order at which these points are 
     ###stored can provide an easy calculation to find total area of the faces seen


def clear():
    clear_screen()

centerX, centerY = createWindow()
centerx = centerX
centery = centerY

while True:
    draw()
    time.sleep(timestep+1)
    clear()
    angle = angle + 0.1 # full rotation is 80 ticks 
    
    
    