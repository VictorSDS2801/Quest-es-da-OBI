n, m = map(int, input().split())

lista = []
for nv in range(n):
    tempos = list(map(int, input().split()))
    soma = sum(tempos)
    lista.append(soma)



lista_final = min(lista)
print(lista.index(lista_final) + 1)
