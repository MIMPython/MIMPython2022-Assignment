def getFileName(name, week, assignment):
    name = name.title().replace(" ", "")
    return f"week{week}_assignment{assignment}_{name}.py"

def main():
    print (getFileName("luong duc anh", 2, 3)) #week2_assignment3_LuongDucAnh.py
    print (getFileName("  luong  duc anh ", 2, 3)) #week2_assignment3_LuongDucAnh.py

if __name__ == "__main__":
    main()