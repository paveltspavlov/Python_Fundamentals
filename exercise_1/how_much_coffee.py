command = input()

coffees_needed = 0

action_to_lower = ['coding', 'movie', 'dog', 'cat']
action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while command != 'END':

    if command in action_to_lower:
        coffees_needed += 1
    elif command in action_to_upper:
        coffees_needed += 2

    command = input()

    if command == 'END':
        if coffees_needed > 5:
            print('You need extra sleep')
        else:
            print(coffees_needed)
