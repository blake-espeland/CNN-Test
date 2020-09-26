from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D
from os import walk

model = Sequential()

f = []  # input files
directory = r'C:\Users\blake\OneDrive\Desktop\Realsense Images'
for (dirpath, dirnames, filenames) in walk(directory):
    f.extend(filenames)
    break
f = [(directory + "\\" + x) for x in f if x[-1: -4: -1][::-1] in ('png', 'jpg', 'z16', 'raw')]

model.input()
# model.add(Conv2D(1, (3, 3), activation='relu'))
