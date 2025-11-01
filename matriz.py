# Crie uma matriz com base no que o usuário digitar.
def matriz_user(linhas, colunas, form):

    matriz = [[0 for x in range(colunas)] for y in range(linhas)]

    for i in range(0, linhas):
        for j in range(0, colunas):
            matriz[i][j] = int(form[f"valor_{i}_{j}"])

    return matriz

