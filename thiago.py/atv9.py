quantidade = int(input("Digite a quantidade atual em stock: "))

if quantidade > 100:
    print("Stock elevado")
elif quantidade >= 20:
    print("Stock adequado")
else:
    print("Atenção: Stock crítico! Reabastecer agora")