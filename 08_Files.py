import os
from pathlib import Path

filrPath = os.getcwd() + '/PythonLearner/input/01_test.txt'
with open(filrPath, 'r') as reader: # <- will close the file gracefully compared to reader = open(filrPath, 'r')
    for line in reader.readlines():
        print(line.strip())