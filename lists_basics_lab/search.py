number = int(input())
word = input()
phrases = []
buff2 = []

for i in range(number):
    buff = input()
    phrases.append(buff)

    if word in buff:
        buff2.append(buff)

print(phrases)
print(buff2)
