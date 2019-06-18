def velocidad(d,t):
    v=d/t
    return v

d=float(input('Distancia recorrida: '))
t=float(input('Intervalo de tiempo en recorrer esa distancia: '))

v=velocidad(d,t)

print('La velocidad es: ' + str(v))

print('Programa terminado.')
