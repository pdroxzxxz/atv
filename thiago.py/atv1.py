
largura_1 = float(input("Digite a largura do primeiro retângulo: "))
altura_1 = float(input("Digite a altura do primeiro retângulo: "))
area_1 = largura_1 * altura_1

largura_2 = float(input("Digite a largura do segundo retângulo: "))
altura_2 = float(input("Digite a altura do segundo retângulo: "))
area_2 = largura_2 * altura_2

if area_1 > area_2:
    print("O primeiro retângulo possui a maior área.")
elif area_2 > area_1:
    print("O segundo retângulo possui a maior área.")
else:
    print("Empate: ambos os retângulos possuem a mesma área.")
