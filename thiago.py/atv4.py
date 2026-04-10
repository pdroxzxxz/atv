alice = int(input("Alice (0 ou 1): "))
beto = int(input("Beto (0 ou 1): "))
clara = int(input("Clara (0 ou 1): "))

if alice != beto and alice != clara:
    print("Alice")
elif beto != alice and beto != clara:
    print("Beto")
elif clara != alice and clara != beto:
    print("Clara")
else:
    print("Empate")