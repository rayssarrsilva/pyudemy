#Retorne o menor valor digitado pelo usuário.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c 

print(f"O menor valor digitado é: {menor}")