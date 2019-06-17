print('While con sentencia break')
print('=========================')

print('Sumador de numeros hasta 20')

s=0
n=0

while(n<20):
    s+=n
    n+=1
    print('El num es ' +str(n))

    if n>12:
        break

print('La suma es: ' +str(s) + '.')
