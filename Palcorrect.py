string = "favour"
value = 1
for i in range(len(string)):
    temp = ord(string[i]) - 97
    print(temp, end='\t')
    value ^= 2
    print(value)