year = int(input())

while True:
    digits = list(str(year))
    unique_digits = set(digits)

    if len(unique_digits) == len(digits):
        print(year)
        break

    year += 1
