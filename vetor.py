n = int(input("Digite o tamanho do vetor: "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = float(input(f"Digite o valor da posição {i}: "))

print()
print("Valores do vetor:") 

for i in range(n):
    print(f"{vet[i]:.1f} ", end='')

print()

soma = 0
for i in range(n):
    soma += vet[i]

print(f"Soma dos valores do vetor: {soma:.2f}")