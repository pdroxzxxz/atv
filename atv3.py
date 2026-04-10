ouro_a = int(input("Ouro País A: "))
prata_a = int(input("Prata País A: "))
bronze_a = int(input("Bronze País A: "))

ouro_b = int(input("Ouro País B: "))
prata_b = int(input("Prata País B: "))
bronze_b = int(input("Bronze País B: "))

if ouro_a > ouro_b:
    print("País A está melhor classificado.")
elif ouro_b > ouro_a:
    print("País B está melhor classificado.")
else:
    if prata_a > prata_b:
        print("País A está melhor classificado.")
    elif prata_b > prata_a:
        print("País B está melhor classificado.")
    else:
        if bronze_a > bronze_b:
            print("País A está melhor classificado.")
        elif bronze_b > bronze_a:
            print("País B está melhor classificado.")
        else:
            print("Os países estão empatados no ranking.")