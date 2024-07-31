budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

loaf_price = flour_price + eggs_price + (milk_price / 4)
loaf_counter = 0
colored_eggs = 0

while budget >= loaf_price:
    budget -= loaf_price
    if budget <= 0:
        break
    loaf_counter += 1
    colored_eggs += 3
    if loaf_counter % 3 == 0:
        colored_eggs -= (loaf_counter - 2)

print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
