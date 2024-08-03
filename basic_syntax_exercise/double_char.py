doubled_string = ""

while True:
    command = input()

    if command == "End":
        break
    elif command == "SoftUni":
        continue

    for char in command:
        doubled_string += char * 2

    print(doubled_string)
    doubled_string = ""
