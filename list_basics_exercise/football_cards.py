input_list = [item for item in input().split(" ")]
card = []
output_a = 0
output_b = 0

for i in range(0, len(input_list)):
    card[i] = input_list[i].split("-")

    if card[i] == "A":
        output_a += 1
    elif card[i] == "B":
        output_b += 1

    i += 1

print(f"Team A - {11 - output_a}; Team B - {11 - output_b}")
