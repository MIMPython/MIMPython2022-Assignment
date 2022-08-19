""""
cd C:\Users\Minh\Desktop\x
mkdir foo
cd foo
type nul > data.txt
echo Hello World! > data.txt
copy data.txt newData.txt
copy data.txt newData_2.txt
cd ..
mkdir bar
cd foo
move newData.txt ~/../bar
del newData_2.txt

"""