from random import randint

def nameData():
    data = ""
    with open("additionalFolder\\name.txt", "r") as file:
        data = file.read()
    data = data.replace("\"", "")
    data = data.split(",")
    return data

def classData():
    branchData = ["ToanHoc","ToanTin","KHMT&TT","KHMT&TT","KHDL"]
    data = []
    for i in range(63, 68):
        for j in range(5):
            data.append("K{}A{} {}".format(i , j + 1 , branchData[j]))
    return data

def scoreData():
    data = []
    for i in range(0, 101):
        data.append(i/10)
    return data

def dataFame():
    dataName = nameData()
    dataName.sort()
    dataClass = classData()
    dataScore = scoreData()
    data = set()
    while len(data) < 100000:
        name = dataName[randint(0, len(dataName) - 1)]
        cLass = dataClass[randint(0, len(dataClass) - 1)]
        score = dataScore[randint(0, len(dataScore) - 1)]
        data.add("{:<12} | {:^15} | {:^6}".format(name, cLass, score))
    return data

if __name__ == "__main__":
   
    with open("additionalFolder\\dataFameEx03.txt", "w") as file:
        file.write("{:^12} | {:^15} | {:^6}".format("Name", "Class", "Score"))
        randomData = dataFame()
        for i in randomData:
            data = "\n" + i
            file.write(data)
