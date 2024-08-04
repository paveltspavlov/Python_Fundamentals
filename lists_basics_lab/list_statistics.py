lines = int(input())
list_of_numbers = []
positive_numbers = 0
negative_numbers = 0
positive_list = []
negative_list = []

for i in range(lines):
    number = int(input())
    list_of_numbers.append(number)

    if list_of_numbers[i] >= 0:
        positive_list.append(list_of_numbers[i])
        positive_numbers += 1
    else:
        negative_list.append(list_of_numbers[i])
        negative_numbers += list_of_numbers[i]

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_numbers}")
print(f"Sum of negatives: {negative_numbers}")
