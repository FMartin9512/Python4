szam = int(input("Adj meg egy pozitív egész számot: "))
for i in range(szam):
    if (i % 2 == 0):
        print(0, end="")
    elif (i % 2 != 0):
        print(1, end="")
