print('While controlado son evento.')

print('===========================')

print('Calcular promedio')

promedio=0.01
total=0
contar=0

print('Escribe el valor (-1 para salir)')

grado=float(input())

while grado !=-1:
    total += grado
    contar += 1

    print('Escribe el valor (-1 para salir):')
    grado=float(input())

    promedio = total/contar

    print('el promedio es ' + str(promedio))
