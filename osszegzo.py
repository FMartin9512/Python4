szam = int(input("Adj meg egy pozitív egész számot: "))
szum = 0
for i in range(1, szam):
    szum = szum + i
print(f"A számok összege : {szum}")
