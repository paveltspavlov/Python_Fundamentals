numbers_count = int(input())
numbers_list = []
buff = []
buff_2 = []

for i in range(numbers_count):
    buff = input()
    numbers_list.append(buff)

command = input()

if command == "even":
    buff_2 = [int(num) for num in numbers_list if int(num) % 2 == 0]
    print(buff_2)
elif command == "odd":
    buff_2 = [int(num) for num in numbers_list if int(num) % 2 != 0]
    print(buff_2)
elif command == "negative":
    buff_2 = [int(num) for num in numbers_list if int(num) < 0]
    print(buff_2)
else:
    buff_2 = [int(num) for num in numbers_list if int(num) > 0]
    print(buff_2)
