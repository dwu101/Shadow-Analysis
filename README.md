# Shadow-Analysis
Can the shape of an object be approximated just by analyzing how its shadow changes?

The current alogirthm involves a cube that is rotated about the axis that spans the length of the computer screen. As it rotates, screenshots 
are taken in order to capture the projection of the 3D shape on our 2D computer screens. The area of each projection is found, and a plot is displayed showing
the area vs the screenshot number. 

This prototype can be run by simply opening shadow.py in an IDE and replcaing the (INSERT DIRECTORY) with where you want the screenshots to be saved. 
Once the screenshots are taken, you have an option to analyze the screenshots. When prompted, typing "y" in the terminal will analyze the screenshots and will
display the plot, while typing "n" will result in the screenshots not being analyzed.

