#Las tuplas son listas que no se pueden modificar una vez hechas
#Tupla simple

tupla = 25678, 73732, 'tuplas'

#Tuplas anidadas

atupla = tupla, (5, 3, 7, 8, 2)

#operacion de asignacion de valores de una tupla en variables

x, y, z = tupla

print(tupla)

print(atupla)

print(x)

print(y)

print(z)

#Ejemplo de tupla para conexion con base de datos

print("\nConectar a la base de datos MySql")

print("=============================\n")

conexion_bd = "1546.540.07.18", "accesoroot", "lgh6", "users",

print(conexion_bd)

conexion_c = conexion_bd, "3457", "19"

print("\n")

print("Conexion con estos parametros:", conexion_c)

print(conexion_c)

print("\n")

print("Acceder a la IP de la base de datos:", conexion_c[0][0])

print("Acceder al usuario de la base de datos:", conexion_c[0][1])

print("Acceder a la clave de la base de datos:", conexion_c[0][2])

print("Accederal nombre de la base de datos:", conexion_c[0][3])

print("Acceder al puerto:", conexion_c[1])

print("Acceder al tiempo de espera de conexion:", conexion_c[2])
