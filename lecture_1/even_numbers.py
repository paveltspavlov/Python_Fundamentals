num_count = int(input())
num = 0
while num_count > 0:
    num = int(input())
    if num % 2 == 0:
        if num_count == 1:
            print("All numbers are even.")
            break
    else:
        print(f"{num} is odd!")
        break
    num_count -= 1
