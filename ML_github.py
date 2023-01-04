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


model = Sequential()
model.add(Dense(300, input_dim=79, kernel_regularizer=l2(0.01)))  #the picture rbg scla ehting is 3
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

model.add(Dense(34, input_dim=50)) 
model.add(Activation('softmax')) 




with open("areas_data.csv") as f:
    line = f.readline()
    areas = []
    dimensions = []
    num = ""
    while line:
        for char in line: ##since the file is read in as a string, I need to find the numbers and add them to an array to use as integers.
            if char == "\n":
                
                dimensions.append(int(float(num)*10)-1) #### the largest dimension (1.0) would mean there must be 11 indexes in the output of to_categorical. however, this would make the dim(areas) != dim(dimensions) as 10 !=11. so the dimensions must be 1 less to make 10 = 10 
                num = ""
                    
            elif char == ",":
                areas.append((int(num)/1000000))
                num = ""
            else:
                num += char  
        line = f.readline()

areas = np.array(areas)

dimensions = np.array(dimensions)

areas = areas.reshape(len(dimensions), 79)

sgd = SGD(lr=0.0001, decay=1e-6)

model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy']) #categorical crossentropy is loss for when the model has to decide where to categorize the data when there are >=2 possible categories


dimensions = to_categorical(dimensions, num_classes = len(dimensions)) 

model.fit(areas, dimensions, epochs=100)
model.evaluate(areas, dimensions)

