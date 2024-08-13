factor = int(input())
counter = int(input())
i = 0
result = []
number = 0

while i < counter:
    number += factor
    result.append(number)
    i += 1

print(result)
