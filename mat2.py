n = int(input("Digite o tamanho do vetor: "))

mat = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = float(input(f"digite o valor do elemento [{i}, {j}]: "))

print("diagonal principal: ")
for i in range(n):
    print(f"{mat[i][i]:.2f} ", end='')

print()

cont = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            cont = cont + 1 

print(f"Números negativos: {cont}")