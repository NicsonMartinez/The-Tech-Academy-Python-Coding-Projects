import os

fName = 'Hello.txt'

fPath = 'C:\\A\\' #It can't be 'C:\A\' because backslash in a string means to ignore the next character..

abPath = os.path.join(fPath, fName)

print(abPath)
