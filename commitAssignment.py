import os
import sys
import zipfile
from pathlib import Path

commitFolder = sys.argv[1]
pathToCommitFolder = Path(commitFolder)
listDirectory = os.listdir(commitFolder)
fileZipList = [f for f in listDirectory if f.endswith('.zip')]

assert len(fileZipList) != 0, 'Folder is empty.'

for filename in fileZipList:
    pathToFile = pathToCommitFolder / filename
    with zipfile.ZipFile(pathToFile, 'r') as f:
        f.extractall(commitFolder)

listDirectory = os.listdir(commitFolder)
commitFolderList = [f for f in listDirectory if not f.endswith('.zip')]
for folderName in commitFolderList:
    os.system(f'git add {pathToCommitFolder/folderName}')
    os.system(f'git commit -m "Add {folderName} for {commitFolder}"')

os.system('git push')
