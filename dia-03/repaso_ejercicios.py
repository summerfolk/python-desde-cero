'''
#ejercicio 1: tabla de multiplicar
numero = int(input("ingrese un numero: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
'''
'''
#jercicio 2: suma del 1 al 100:
suma = 0

for i in range(1, 101):
    suma += i
print(suma)
'''
'''
#ejercicio 3: contar vocales
oracion = input("ingrese su oracion: ")
for i in  oracion:
    if i in "aeiouAEIOU":
        print(i)
    else:
        pass
'''
'''
#ejercicio 4: mostrar numero
for i in range(1, 21):
    print(i)
'''
'''
#Ejercicio 5: mostrar numeros pares del 2 al 50

for i in range(2,51,2):
    print (i)
'''
'''
#ejercicio 6: mostrar los numeros impares del 1 al 49:
for i in range(1,50,2):
    print (i)
'''
'''
#ejercicio 8: contar cuantas letras tiene una palabra.
contador = 0
palabra = input("ingrese una palabra: ")
for i in palabra:
    contador += 1
print(f"tiene {contador} letras")
'''
'''
#ejercicio 8: sumar los numeros del 1al número que indique el usuario.

numero = int(input("ingrese un numero: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"resultado: {suma}")
'''
'''
#ejercicio 9: contar cuentas veces aparece la letra "a" en un apalabra.
palabra = input("ingrese una palabra: ")
contador = 0
for i in palabra:
    if i == "a":
        contador += 1
print(f"Cantidad: {contador}")

'''
'''
#ejercicio 10: mostrar cada caracter de una frase en una linea distinta:
palabra = input("ingrese una palabra: ")
for i in palabra:
    print(i)
'''
'''
#ejercicio 11: Calcular el factorial de un número

def factorial_de_un_numero():
    numero = int(input("ingrese un numero: "))
    contador = 1
    for i in range(1, numero + 1):
        contador *= i
    return contador
print(factorial_de_un_numero())
'''
'''
#ejercicio 12: pedir una palaba y mostrarla al revez
palabra = input("ingrese luna palabra: ")
invertido = palabra[::-1]
print(invertido)
'''

#ejercicio 13: contar cuantas consonantes tiene una palabra

palabra = input("pedir una palabra: ")
contador = 0
for i in palabra:
    if i in "bcdfghjklmnñpqrstvwxyz":
        contador += 1
    else:
        continue
print(f"tiene {contador} consonantes")

'''
#ejercicio 14: pedir una frase y contar: (vocales y espacios)

frase = input("ingrese una frase: ")
contador_vocales = 0
contador_espacios = 0

for i in frase:
    if i in "aeiou":
        contador_vocales += 1
    elif i == " ":
        contador_espacios += 1
print(f"vocales: {contador_vocales}")    
print(f"Espacios: {contador_espacios}")
'''
'''
#ejercicio 15: desafio
#pedir una palabra y determinar si es un palindromo
palabra = input("ingrese una palabra: ")

if palabra == palabra[::-1]:
    print("es un palindromo")
else:
    print("no es un palindromo")
'''
