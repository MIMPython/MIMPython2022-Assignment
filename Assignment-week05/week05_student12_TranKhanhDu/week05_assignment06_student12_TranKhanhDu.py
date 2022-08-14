def printFileName(weekNumber, id, name):
    string = "week" + str(weekNumber) + "_" + "student" + str(id) + "_" +str(name)
    print(string)
#pass argument
weekNumber = int(input("enter week number: "))
if weekNumber < 10:
    weekNumberToPrint = "0" + str(weekNumber)
else:
    weekNumberToPrint = str(weekNumber)
#pass argument
id = int(input("enter id: "))
if id < 10:
    idToPrint = "0" + str(id)
else:
    idToPrint = str(id)
#pass argument
name = input("what is your name? ")
if __name__ == "__main__":
    printFileName(weekNumberToPrint, idToPrint, name)