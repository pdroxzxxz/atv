valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 500:
    desconto = valor_compra * 0.20
elif valor_compra >= 100:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto

print("Valor do desconto:", desconto)
print("Valor final a pagar:", valor_final)