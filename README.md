# Shadow-Analysis
Can the shape of an object be approximated just by analyzing how its shadow changes?

The current alogirthm involves a cube that is rotated about the axis that spans the length of the computer screen. As it rotates, screenshots 
are taken in order to capture the projection of the 3D shape on our 2D computer screens. The area of each projection is found, and is saved to a file called areas_data.csv

To operate:

You probably shouldn't generate the data yourself using generating_data_github.py since the process takes 3 hours and CAN NOT be run in the background on the computer. The only way around this is to have the window it renders be on the computer/main screen, and work can be done on a monitor. If you really want to, just download it, make sure you have all the libraries installed, and then look in the file for something that says (INSERT DIRECTORY ...) and follow the directions in the .... It should be the full directory (i.e."C:/Users/dwu101/OneDrive/Desktop/folder1/folder2/"). Notice these instructions are in quotes. Make sure the directory name is also surrounded by these quotes so its a string. After this, the program can be run.

If you don't want to generate the data, you can also just download areas_data.csv, which has 34 pre-generated points. By pre-generated, I mean that I went through the pain of waiting the 3 hours for the data to generate. I hope to make this process more efficient, and already have some ideas for optimization. Anyways, also download ML_github.py and make sure it is in the same folder as areas_data.csv. If you are unsure of where areas_data.csv is, you could also look for the (INSERT DIRECTORY ...) at the top of the file and insert the directory that points to areas_data.csv is (i.e "C:\Users\dwu101\OneDrive\Desktop\folder1\folder2\folder3\areas_data.csv"). Then you can run the file and train the neural network. The accuracy is low and the loss is high, which is largely due to the extremely small sample size. As I increase the efficiency of generating_data_github.py, the sample size will grow as well.
