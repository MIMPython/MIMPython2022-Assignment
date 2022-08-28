import os

def readFile(rootdir):
    # import required module
    # assign directory

    # iterate over files in
    # that directory
    for filename in os.listdir(rootdir):
        f = os.path.join(rootdir, filename)
        # checking if it is a file
        print(f)

if __name__ == '__main__':
    readFile("..\.idea")