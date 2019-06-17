print('While con sentencia continue')
print('===============================')

vari=10

while (vari>0):
    vari=vari-1

    if vari>= 4:
        print('Entra en el continue y la vari es ' +str(vari))

    else:
        break

    continue

print('La variable es ' +str(vari))
