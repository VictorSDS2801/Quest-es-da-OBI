ql = int(input())
lista = list(map(int, input().split()))
lampada1 = False
lampada2 = False
for b in lista:
    if b == 1:
        lampada1 = not lampada1
    if b == 2:
        lampada1 = not lampada1
        lampada2 = not lampada2
if lampada1 == True:
    lampada1 = 1
elif lampada1 == False:
    lampada1 = 0
if lampada2 == True:
    lampada2 = 1
elif lampada2 == False:
    lampada2 = 0
print(lampada1)
print(lampada2)

