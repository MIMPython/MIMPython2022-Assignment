"""
F:
cd F:\x
mkdir foo
cd foo
code data.txt
copy data.txt newData.txt
copy data.txt newData_2.txt
cd F:\x\
mkdir bar
cd F:\x\foo
move newData.txt F:\x\bar
del newData_2.txt
"""