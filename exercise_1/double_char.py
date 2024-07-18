command = ""
while command != "End":

    if command != "SoftUni":
        command = input()
        buff = list(command)
        print(f"{''.format(buff, buff)}")
    elif command == "End":
        break
