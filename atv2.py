x = float(input("Digite a coordenada X onde a bola tocou: "))
y = float(input("Digite a coordenada Y onde a bola tocou: "))

if 0 <= x <= 10 and 0 <= y <= 10:
    print("A bola caiu dentro da semi-quadra.")
else:
    print("A bola caiu fora da semi-quadra.")