
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}


student_name = input("Enter the student's name: ")


if student_name in students:
    print(f"{student_name} scored {students[student_name]} marks.")
else:
    print(f"Student named '{student_name}' not found in the record.")
