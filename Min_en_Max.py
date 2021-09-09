var1 = input("    geef de waarde van a ")
var2 = input("    geef de waarde van b ")




print("")
print("---------------------------------------------------------------------->")


if var2 > var1:
    print("    a is het kleinste getal")
    min = var1
    max = var2

elif var2 < var1:
    print("    a is het grootste getal")
    min = var2
    max = var1
else: print("    a en b zijn gelijk")
print("")
print("---------------------------------------------------------------------->")
print("")
Min_TXT = '    het minimum is ' + str(min)
max_TXT = '    het maximum is ' + str(max)
print(max_TXT)
print(Min_TXT)