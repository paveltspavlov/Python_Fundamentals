budget = int(input())
price = ""

while price != "End":
    price = input()
    if price == "End":
        print("You bought everything needed.")
        break

    price = int(price)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break

