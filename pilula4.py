def calcularResulto():
    n1 = float(input("nota 1: "))
    n2 = float(input("nota 2: "))
    n3 = float(input("nota 3: "))
    
    media = (n1+n2+n3)/3
    if media < 6:
        rec = float(input('Recuperação'))
        media = (media + rec)/ 2
    
    return media

m = calcularResulto()
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado') 