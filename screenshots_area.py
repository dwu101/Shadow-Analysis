def screenshots():
    import pyautogui 


    for i in range(80):
        screenshot = pyautogui.screenshot()
        screenshot.save(r"C:\Users\danqw\OneDrive\Desktop\cs_stuff\shadow\screenshots\screenshot{x}".format(x = i))
    

def area_plot():
    import os
    import cv2

    
    os.chdir(r"C:/Users/danqw/OneDrive/Desktop/cs_stuff/shadow/screenshots")
    for i in range(1):

        img = cv2.imread("screenshot_{x}.jpg".format(x=1))
        
        size = img.shape #(y,x)
        x = size[1]
        y = size[0]

        total_area = 0 

        for i in range(y):
            edge_found = False
            count = 0
            print(i)
            for j in range(x):
                if img[i,j][0] == 0 and edge_found:
                    try:
                        if img[i,j+1][0] !=0:
                            count +=1
                            break
                    except:
                        break
                    count +=1
                if img[i,j][0] != 0 and not edge_found:
                    try:
                        if img[i,j+1][0] == 0:
                            edge_found = True
                            cv2.circle(img,(i,j), 3, (0,255,0), -1)
                    except:
                        break
            
            total_area += count 
    while(1):
        cv2.imshow("Cross-Section",img)
        if cv2.waitKey(20) & 0xFF ==27:
            break
    return total_area


area_plot()
