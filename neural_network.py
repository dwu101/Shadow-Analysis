from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras.regularizers import l2
from matplotlib import pyplot as plt
import numpy as np
import os 

os.chdir(r"(INSERT DIRECTORY TO WHERE areas_data.csv IS)") 


with open("areas_data.csv") as f: #cleans up the data, creating lists of integers from the strings in areas_data.csv
    line = f.readline()
    areas = []
    dimensions = []
    num = ""
    while line:
        for char in line: ##since the file is read in as a string, I need to find the numbers and add them to an array to use as integers.
            if char == "\n":
                
                dimensions.append(int(float(num)*10)-1) 
                num = ""
                    
            elif char == ",":
                areas.append((int(num)/1000000))
                num = ""
            else:
                num += char  
        line = f.readline()

areas = np.array(areas)

dimensions = np.array(dimensions)

areas = areas.reshape(len(dimensions), 79) #len(dimensions) is used to keep this program scalable. 79 screenshots are taken from each of the 34 shapes.

model = Sequential()
model.add(Dense(300, input_dim=79, kernel_regularizer=l2(0.01)))  #first layer of the neural network with 300 neurons
model.add(Activation('relu'))

model.add(Dense(250, input_dim=300, kernel_regularizer=l2(0.01)))
model.add(Activation('relu'))

model.add(Dense(200, input_dim=250, kernel_regularizer=l2(0.01)))
model.add(Activation('relu'))

model.add(Dense(150, input_dim=200, kernel_regularizer=l2(0.01)))
model.add(Activation('relu'))

model.add(Dense(100, input_dim=150, kernel_regularizer=l2(0.01)))
model.add(Activation('relu'))

model.add(Dense(50, input_dim=100, kernel_regularizer=l2(0.01)))
model.add(Activation('relu'))

model.add(Dense(len(dimensions), input_dim=50)) #last layer of neural network with len(dimensions) neurons since there are only len(dimensions) possible outputs
model.add(Activation('softmax'))

sgd = SGD(lr=0.0001, decay=1e-6)

model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy']) 


dimensions = to_categorical(dimensions, num_classes = len(dimensions)) 

model.fit(areas, dimensions, epochs=100) #trains model with 100 epochs
model.evaluate(areas, dimensions) #evaluates how well the model is with the exact same data it trained on. This will be different later.
