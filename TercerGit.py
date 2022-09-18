nombre = input('¿Cual es tu nombre?')

edad = int(input('¿Cuantos años tienes?'))

InformaciónPersonal= 'Hola mundo, soy ' + nombre + ' y tengo ' + str(edad) + ' años '
print (InformaciónPersonal)

numero1 = 25
numero2 = 24

if numero1 > numero2:
    print('el numero 1 es mayor al numero 2')
elif numero2 > numero1:
    print('el numero 2 es mayor que el numero 1')

if edad >= 18:
    print( nombre + ' ES MAYOR DE EDAD')
elif edad <= 17:
    print(nombre + ' ES MENOR DE EDAD')
