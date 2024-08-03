quantity_of_decorations = int(input())
days = int(input())

ornament_price = 2
ornament_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17
total_price = 0
total_points = 0

for i in range(1, days+1, +1):

    if i % 2 == 0:
        total_price += ornament_price
        total_points += ornament_points
    if i % 3 == 0:
        total_price += tree_skirt_price + tree_garland_price
        total_points += tree_skirt_points + tree_garland_points
    if i % 5 == 0:
        total_price += tree_lights_price
        total_points += tree_lights_points
    if i % 15 == 0:
        total_points += 30
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price

    if i % 10 == 0:
        total_points -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price

    if i % 11 == 0:
        quantity_of_decorations += 2

    if i == 10:
        total_points -= 30

    quantity_of_decorations -= 1

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_points}")
