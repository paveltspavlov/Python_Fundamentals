input_list = [item for item in input().split(" ")]
output_a = 0
output_b = 0
unique_cards_a = set()
unique_cards_b = set()
card1 = []

for item in input_list:
    card = item.split("-")

    if card[0] == "A":
        unique_cards_a.add(card[1])
        output_a += 1
    elif card[0] == "B":
        unique_cards_b.add(card[1])
        output_b += 1

if (11 - len(unique_cards_a)) <= 7 or (11 - len(unique_cards_b)) <= 7:
    print(f"Team A - {11 - len(unique_cards_a)}; Team B - {11 - len(unique_cards_b)}")
    print("Game was terminated")

else:
    print(f"Team A - {11 - len(unique_cards_a)}; Team B - {11 - len(unique_cards_b)}")
