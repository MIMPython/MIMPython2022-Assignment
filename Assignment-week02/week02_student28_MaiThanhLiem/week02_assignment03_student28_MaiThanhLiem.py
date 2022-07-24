def file_name(**data):
    for student, student_info in data.items():
        print(
            f"week{student_info['week']:02d}_assignment{student_info['exercise']:02d}_student{student_info['no']:02d}_{student_info['name']}.py"
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

file_name(**students)
