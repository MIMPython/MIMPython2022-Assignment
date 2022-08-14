import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--student", type=str)
parser.add_argument("--studentInfo", type=map)
args = parser.parse_args()
student = args.student
studentInfo = args.studentInfo


def fileName(**data):
    for student, studentInfo in data.items():
        studentInfo["name"].replace(" ", "")
        print(
            f"week{studentInfo['week']:02d}_assignment{studentInfo['exercise']:02d}_student{studentInfo['no']:02d}_{studentInfo['name']}.py"
        )


students = {
    "liemmt28": {
        "name": "Mai Thanh Liem",
        "no": 28,
        "week": 2,
        "exercise": 3,
    },
    "haopt19": {
        "name": "Pham The Hao",
        "no": 19,
        "week": 3,
        "exercise": 10,
    },
    "sonnt46": {
        "name": "Nguyen The Son",
        "no": 46,
        "week": 8,
        "exercise": 7,
    },
}

fileName(**students)
