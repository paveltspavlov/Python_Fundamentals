string_one = input()
string_two = input()
buff = list(string_one)
buff2 = list(string_two)
delimiter_comma = ""
printable = ""
i = 0

for i in range(len(string_one)):
    if buff[i] != buff2[i]:
        buff[i] = buff2[i]
        printable = delimiter_comma.join(buff)
        output = printable.replace(",", "")
        print(printable)
    i += 1
