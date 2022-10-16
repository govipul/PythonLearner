import os
from pathlib import Path

filePath = os.getcwd() + '/PythonLearner/input/01_test.txt'
with open(filePath, 'r') as reader: # <- will close the file gracefully compared to reader = open(filrPath, 'r')
    for line in reader.readlines():
        print(line.strip())

writeFilePath = filePath = os.getcwd() + '/PythonLearner/input/02_write.txt'
with open(writeFilePath, 'w') as writer:
        writer.write('This is a line 1\n')
        writer.write('This is a line 2\n')

writeFilePath = filePath = os.getcwd() + '/PythonLearner/input/02_write.txt'
with open(writeFilePath, 'a') as writer:
        writer.write('append this line 3\n')