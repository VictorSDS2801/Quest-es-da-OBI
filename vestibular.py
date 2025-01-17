quant_quest = int(input())
gabarito = input()
respostas = input()
acertos = 0
for letra in range(quant_quest):
    if gabarito[letra] == respostas[letra]:
        acertos = acertos + 1
print(acertos)
