number  = int(input())
for i in range(0, number):
    input_string = input()
    buff = [char for char in input_string]

    if any(char in [',', '.', '_'] for char in buff):
        print(f"{input_string} is not pure!")
    else:
        print(f"{input_string} is pure.")
