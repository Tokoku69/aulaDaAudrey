Emerson e Luiz ATIVIDADE DE LÓGICA
# Criação da matriz 3x3 e preenchimento com valores digitados pelo usuário
matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

print("\nMatriz 3x3 formatada:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()

# A) Soma de todos os valores pares
soma_pares = sum(valor for linha in matriz for valor in linha if valor % 2 == 0)

# B) Soma dos valores da terceira coluna
soma_terceira_coluna = sum(matriz[linha][2] for linha in range(3))

# C) Maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print("\nResultados:")
print(f"A) Soma dos valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")

