szam1 = int(input("Adj meg egy pozitív egész számot: "))
szam2 = int(input("Adj meg egy másik pozitív egész számot: "))
for i in range(szam1, szam2+1):
    if i % 2 == 0:
        print(i)
