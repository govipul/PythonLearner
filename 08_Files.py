import os
from pathlib import Path

# add the correct path
print(os.getcwd())
filrPath = os.getcwd() + '/PythonLearner/input/01_test.txt'
with open(filrPath, 'r') as reader:
    for line in reader.readlines():
        print(line.strip())
