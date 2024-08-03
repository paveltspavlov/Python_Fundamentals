dividor = int(input())
boundary = int(input())
max_num = 0

for max_num in range(boundary, 0, -1):
    if max_num % dividor == 0:
        if max_num <= boundary:
            if max_num > 0:
                print(max_num)
                break
