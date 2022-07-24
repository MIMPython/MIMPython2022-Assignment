def getInfo(name, week, assignment):
    name = name.title().replace(" ","")
    return f"week{week}_assignment{assignment}_{name}.py"

def main():
    print (getInfo('nguyen duc nam', 2, 3))
    print (getInfo('nguyen   duc   nam', 2, 3))

if __name__ == '__main__':
    main()