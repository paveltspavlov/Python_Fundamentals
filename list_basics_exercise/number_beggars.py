def beggars_distribution(offerings, num_beggars):
    if num_beggars == 0:
        return []

    beggar_sums = [0] * num_beggars

    for i, offering in enumerate(offerings):
        beggar_index = i % num_beggars
        beggar_sums[beggar_index] += offering

    return beggar_sums


# Input processing
offerings = list(map(int, input().split(", ")))
num_beggars = int(input())

# Calculate and print the result
result = beggars_distribution(offerings, num_beggars)
print(result)