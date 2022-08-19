import sys

def main():
    name = sys.argv[1]
    id = int(sys.argv[2])
    week = int(sys.argv[3])
    assignment = int(sys.argv[4])
    print(f"week{week:02d}_assignment{assignment:02d}_student{id:02d}_{name}.py")

if __name__ == '__main__':
    main()    