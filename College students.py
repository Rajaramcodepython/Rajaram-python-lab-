students = {
    "B.Sc Mathematics": [
        {"name": "Arun", "marks": [80, 75, 90]},
        {"name": "Bala", "marks": [85, 70, 88]}
    ],

    "B.Sc Computer Science": [
        {"name": "Kumar", "marks": [90, 85, 80]},
        {"name": "Priya", "marks": [78, 88, 92]}
    ],

    "B.Com": [
        {"name": "Ravi", "marks": [75, 80, 85]},
        {"name": "Divya", "marks": [88, 90, 82]}
    ]
}

subjects = ["Tamil", "English", "Mathematics"]

for department, student_list in students.items():

    print("\nDepartment:", department)
    print("-" * 40)

    for student in student_list:

        total = sum(student["marks"])

        print("Name       :", student["name"])

        for i in range(len(subjects)):
            print(subjects[i], ":", student["marks"][i])

        print("Total Mark :", total)
        print("-" * 40)
