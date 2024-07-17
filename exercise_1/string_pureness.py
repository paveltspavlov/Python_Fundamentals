number = int(input())

for i in range(0, number):
    input_string = input()
    buff = list(input_string.split(" "))
    for i in range(len(buff)):
        if buff[i] in (',', '.', '_'):
            print(f"{input_string} is pure")
        else:
            print(f"{input_string} is not pure!")
    i += 1
