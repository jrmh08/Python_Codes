students = {}

while True:
    num = int(input("Enter Option: "))
    if num == 1:
        course = input("Enter Course (BSIT, BSIS, BSCS): ")
        age = int(input("Enter age: "))
        students[course] = age
    else:
        break

print(students)
print("Performing Condition")

for key, value in students.items():
    if "BSIT" in key and value == 20:
        print("Student exists")
    else:
        print("Student doesn't exist")
    