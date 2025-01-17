f_repouso = int(input())
f_atual = int(input())
c_oxigenio = int(input())
if f_atual > (f_repouso * 3) or c_oxigenio < 95:
    print("diminuir")
elif f_atual < (f_repouso * 2) and c_oxigenio > 97:
    print("aumentar")
else: 
    print("manter")