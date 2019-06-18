def iva():
    total=int(input('Cuanto has gastado: '))
    n=int(input('Que tipo de producto compraste: 1)Leche 2)Pan 3)Alcohol 4)Otros: '))

    if n==1:
        iv=6

    elif n==2:
        iv=2

    elif n==3:
        iv=9

    else:
        iv=8

    iva=total*iv/100

    return iva

i=iva()
print(i)
