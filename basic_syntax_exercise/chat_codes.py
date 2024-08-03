numbers = int(input())

while numbers > 0:
    command = int(input())

    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88 and command != 86:
        print("GREAT!")
    else:
        print("Bye.")
    numbers -= 1
    