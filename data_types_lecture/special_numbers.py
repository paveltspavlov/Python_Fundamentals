number = int(input())

for i in range(1, number + 1):
    sum = 0
    digits = i
    while digits > 0:
        sum += digits % 10
        digits = int(digits / 10)
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
