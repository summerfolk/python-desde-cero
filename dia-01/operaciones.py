#ejercicio 2: pide dos números y muestra suma, resta, multiplicación y división. 
#Recuerda que input() te da texto, así que necesitas convertir a número — esta vez puedes usar float() 
#en vez de int(), para que también acepte decimal.

primer_numero = float(input("ingrese el primer número: "))
segundo_numero = float(input("ingrese el segundo número: "))

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
if segundo_numero!=0:
    division = primer_numero / segundo_numero
else:
    division = "no se puede dividir entre cero"

print(f"la suma es: {suma}")
print(f"la resta es: {resta}")
print(f"la multiplicación es: {multiplicacion}")
print(f"la división es: {division}")