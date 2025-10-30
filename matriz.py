# Crie uma matriz com base no que o usuário digitar.

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz: list[list[int]] = [[0 for x in range(colunas)] for y in range(linhas)]

for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))

print()
print("Matriz preenchida:")
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f"{matriz[i][j]}", end=" ")
    print()
