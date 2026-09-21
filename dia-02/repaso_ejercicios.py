'''
# ejercicio 1 
edad = int(input("ingrese su edad: "))

if edad >= 18:
    print ("eres mayor de edad")
else:
    print("eres menor de edad")
'''

'''
# ejercicio 2
numero = int(input("ingrese un numero: "))

if numero > 0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es igual a cero")
else:
    print("el numero es negativo")
'''
'''# ejercicio 3

nota = float(input("ingrese su nota: "))

if 0 < nota <=20:
    if nota >= 18:
        print("sacaste una nota exelente")
    elif 11 <= nota < 18:
        print("aprobaste")
    else:
        print("no aprobaste")
else:
    print("la nota que ingresaste debe de estar entre 0 y 20")
'''
'''
#ejercicio 4

primer_numero = int(input("ingrese el primer numero: "))
segundo_numero = int(input("ingrese el segundo numero: "))

if primer_numero > segundo_numero:
    print(f"el primer numero {primer_numero} es mayor que el segundo numero {segundo_numero}")
else:
    print(f"el segundo numero {segundo_numero} es mayor que el primer numero {primer_numero}")
'''
'''
#ejercicio 5

usuario = input("ingrese su usuario: ")
contraseña = input("ingrese su contraseña: ")
if usuario == "carlos" and contraseña == "1234@":
    print("usuario y contraseña correctos")
else:
    print("usuario y contraseña incorrectos, ingrese nuevamente su usuario y contraseña")
'''
'''
#ejercicio 6
dia = input("ingrese el dia de la semana: ")
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
if dia in dias:
    if dia == "sabado" or dia == "domingo":
        print("es fin de semana")
    else:
        print("es dia laborable")
else:
    print("el dia ingresado no es valido")
'''
'''
# ejercicio 7

persona = input("tiene membresia? (si/no): ")
if persona == "si" or persona == "no":
    if not persona == "si":
        print("no puede ingresar")

    else:
        print("puede ingresar")
else:
    print("valor incorrecto, solo es valido si o no")
'''
'''
# ejercicio 8

numero = int(input("ingrese un numero: "))

if numero>=11 and numero<=50:
    print("el numero entra dentro del rango")
else:
    print("el numero no entra dentro del rango")
'''
'''
#ejercicio 9
primer_numero = int(input("ingrese el primer numero: "))
segundo_numero = int(input("ingrese el segundo numero: "))
tercer_numero = int(input("ingrese el tercer numero: "))

if primer_numero >segundo_numero and primer_numero > tercer_numero:
    print(f"el primer numero {primer_numero} es el mayor")
elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
    print(f"el segundo numero {segundo_numero} es el mayor")
else:
    print(f"el tercer numero {tercer_numero} es el mayor")
'''
'''
#ejercicio 10

temperatura = float(input("ingrese la temperatura: "))

if temperatura <= 10:
    print("mucho frio")
elif temperatura >= 10 and temperatura <=25:
    print("templado")
else:
    print("calor")
'''