import sys


def getFileName(*argv):

    return f"week{int(sys.argv[1]):02d}_assignment{int(sys.argv[2]):02d}_student{int(sys.argv[3]):02d}_{sys.argv[4]}.py"


print(getFileName(sys.argv))

# python .\week05_assignment06_student05_LeThiMinhAnh.py 1 2 7 LeVanA
# week01_assignment02_student07_LeVanA.py
