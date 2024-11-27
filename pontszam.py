x = int(input("Add meg a pontszámodat: "))
jegy = 1
if x < 50:
    jegy = 1
elif x < 60:
    jegy = 2
elif x < 70:
    jegy = 3
elif x < 80:
    jegy = 4
else:
    jegy = 5
print(f"Az érdemjegy: {jegy}")
