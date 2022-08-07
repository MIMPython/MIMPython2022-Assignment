import os
import shutil
import zipfile
from pathlib import Path

import pandas as pd


def getAllCorrectFilename(studentID, week, numberOfAssignments, nameWithoutAccent):
    allCorrectFilename = []
    for assignment in range(1, numberOfAssignments + 1):
        allCorrectFilename.append(f'week{week:02}_assignment{assignment:02}_student{studentID:02}_{nameWithoutAccent}.py')
    return allCorrectFilename

def getNumberOfCharactersInFile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    return len(data)

zipAssignmentFolderPath = Path('path/to/week03_student01_TranThanhTung.zip')
week = 3
numberOfAssignments = 13
studentID = 1
nameWithoutAccent = 'TranThanhTung'

correctFolderName = f'week{week:02}_student{studentID:02}_{nameWithoutAccent}'
mistakes = []
extractPath = Path.cwd() / 'validCode'
assert not os.path.exists(extractPath)
with zipfile.ZipFile(zipAssignmentFolderPath, 'r') as z:
    z.extractall(extractPath)
for folder in os.listdir(extractPath):
    if folder != correctFolderName or not os.path.isdir(extractPath / folder):
        mistakes.append({'mistake': 'wrongName', 'description': folder})
    else:
        allCorrectFilename = getAllCorrectFilename(studentID,
                                                    week,
                                                    numberOfAssignments,
                                                    nameWithoutAccent)
        for file in os.listdir(extractPath / folder):
            if file == 'additionalFolder':
                continue
            if file not in allCorrectFilename or os.path.isdir(extractPath / folder / file):
                mistakes.append({'ID': studentID, 'mistake': 'wrongName', 'description':file})
                correct = False
            else:
                sizeOfFile = getNumberOfCharactersInFile(extractPath / folder / file)
                if sizeOfFile < 1:
                    mistakes.append({'ID': studentID, 'mistake': 'emptyFile', 'description':file})
                    correct = False

mistakesDf = pd.DataFrame(mistakes)
if len(mistakes) == 0:
    print('Ready to submit')
else:
    print('Invalid to submit')
    print(mistakesDf)
shutil.rmtree(extractPath, ignore_errors=False)
