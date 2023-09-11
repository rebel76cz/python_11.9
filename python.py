def vytvor_obrazec(Z):
    if Z % 2 == 0:
        print("Zadejte liché číslo Z.")
        return

    for i in range(1, Z + 1):
        for j in range(1, Z + 1):
            if i == j == (Z + 1) // 2:
                print('5', end='')
            elif i == j or i + j == Z + 1:
                print('3', end='')
            else:
                print(' ', end='')
        print()

# Načtení vstupu od uživatele
try:
    Z = int(input("Zadejte liché číslo Z: "))
    vytvor_obrazec(Z)
except ValueError:
    print("Chybný vstup. Zadejte liché číslo Z.")
