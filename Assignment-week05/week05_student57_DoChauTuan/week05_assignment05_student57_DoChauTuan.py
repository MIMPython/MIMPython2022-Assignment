# Bai 5

# a)
while True:
    print("Tuan dep trai")  # Tuan dep trai Tuan dep trai Tuan dep trai Tuan dep trai Tuan dep trai ...........

# b)
names = ['Gdragon', 'TOP', 'Taeyang', 'Daesung', 'Seungri']
for name in names:
    print(
        "Bigbang is best")  # Bigbang is best Bigbang is best Bigbang is best Bigbang is best Bigbang is best ..........
    names.append("V.I.P <3")


# c)
def generator():
    while True:
        yield "FBI warning!!!"  # FBI warning!!! FBI warning!!! FBI warning!!! FBI warning!!! FBI warning!!! FBI warning!!! ..............


for n in generator():
    print(n) 