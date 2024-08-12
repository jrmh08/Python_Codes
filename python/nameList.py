names = []

while True:
    num = int(input("Option (1 = insert / 0 = exit): "))
    if num == 1:
        name = input("Input Name: ")
        names.append(name)
    elif num == 0:
        break

print(names)