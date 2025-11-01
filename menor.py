#Retorne o menor valor digitado pelo usuário.

def menor_valor(form):
    # pega os três números do formulário
    a = int(form["a"])
    b = int(form["b"])
    c = int(form["c"])

    if a < b and a < c:
        menor = a
    elif b < c:
        menor = b
    else:
        menor = c

    return menor
