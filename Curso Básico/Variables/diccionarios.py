datos_basicos = {
"nombres":"Emmanuel Juda",

"apellidos":"Rodriguez Nachez",

"numero":"434958",

"fecha_nacimiento":"05252001",

"lugar_nacimiento":"Guanajuato, Mexico",

"nacionalidad":"Mexicana",

"estado_civil":"Soltero"}

print("\n")

print("Detalle del diccionario")

print("==========================")

print("\n")

print("Claves del diccionario:", datos_basicos.keys())

print("\n")

print("Valores del diccionario:", datos_basicos.values())

print("\n")

print("Elementos del diccionario:", datos_basicos.items())

#Lo que hicimos anteriormente fue crear una lista de datos en la que no solo
#incluia el dato (values), tambien incluia el tipo de dato que es (keys)
#podemos llamar esos datos agregando ".keys()", "values.()", "items.()"; para
#los tipos de de datos, datos y todos los elementos del diccionario,
#respectivamente.

#Ejemplo del uso practico de un diccionario

print("\n")

print("====================")

print("\n")

print("Inscripcion de Curso")

print("--------------------")

print("\n")

print("Datos del participante")

print("--------------------")

print("Cedula de identidad:", datos_basicos['numero'])

print("Nombre completo:", datos_basicos['nombres'] + " " + datos_basicos['apellidos'])

print("Fecha de nacimiento:", datos_basicos['fecha_nacimiento'])
