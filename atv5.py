lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Classificação
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
else:
    print("Não é um triângulo")