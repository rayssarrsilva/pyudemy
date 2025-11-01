def processar_matriz(n, valores):
    n = int(input("Digite o tamanho do vetor: "))

    mat = [[0 for _ in range(n)] for _ in range(n)]

    k = 0

    for i in range(n):
        for j in range(n):
            mat[i][j] = valores[k]
            k += 1

    diagonal = [f"{mat[i][i]:.2f}" for i in range(n)]

    cont = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] < 0:
                cont = cont + 1 

    return diagonal, cont