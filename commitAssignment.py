import os
import sys
from pathlib import Path

commitFolder = sys.argv[1]
fileList = os.listdir(commitFolder)

assert len(fileList) != 0, 'Folder is empty.'
for filename in fileList:
    os.system(f'git add {filename}')
    os.system(f'git commit -m "Add {filename} for {commitFolder}"')

os.system('git push')
