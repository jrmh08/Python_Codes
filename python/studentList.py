students = {}

while True:
    num = int(input("Enter Option: "))
    if num == 1:
        course = input("Enter Course (BSIT, BSIS, BSCS): ")
        age = int(input("Enter age: "))
        students[course] = age
    elif num == 0:
        break

print(students)
    