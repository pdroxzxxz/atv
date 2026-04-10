peso = float(input("Digite o peso da carga (em kg): "))
distancia = float(input("Digite a distância da entrega (em km): "))

if peso > 2000:
    print("Caminhão")
else:
    if distancia >= 100:
        print("Carro")
    else:
        print("Moto")