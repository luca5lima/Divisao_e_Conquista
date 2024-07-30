# Encontrar o maximo valor de um vetor
# Entrada: vetor de inteiros
# Saída: valor maximo do vetor

vetor = [1,2,7,4,5]

def maximo(vetor):
    maximo = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maximo:
            maximo = vetor[i]
    return maximo

        
# Encontrar o maximo valor de um vetor com divisão e conquista
# Entrada: vetor de inteiros
# Saída: valor maximo do vetor
def maxDivConq(vetor, inicio, fim):
    if inicio == fim:
        return vetor[inicio]
    meio = (inicio + fim) // 2
    max_left = maxDivConq(vetor, inicio, meio)
    max_right = maxDivConq(vetor, meio + 1, fim)
    return max(max_left, max_right)

print(maxDivConq(vetor, 0, len(vetor)-1))

# def divisao_e_conquista(x):
#     if x é pequeno ou simples:
#         return resolve(x)
#     else:
#         decompor x em n conjuntos menores x₀, x₁, ..., xn-₁
#         for i in [0, 1, ..., n-1]:
#             yi = divisao_e_conquista(xi)
#         combinar y₀, y₁, ..., yn-₁ em y
#         return y    