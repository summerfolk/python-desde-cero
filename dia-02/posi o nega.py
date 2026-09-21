edad = 17

if edad>=18:
    print("Eres mayor de edad")
else:
    print("eres menor de edad")

nota = 19

if nota>=18:
    print("aprobaste tienes una nota exelente")
elif nota>=14:
    print("aprobaste")
else:
    print("no aprobaste")

#comparadores
# == igual a
# != distinto de 
# > mayor que
# < menor que
# >= mayor igual que
# <= menor igual que

x = 20

print(x == 20)
print(x != 19)
print(x > 18)
print(x < 21)

#en and las dos condiciones deben de ser verdaderas

edad = 19
tiene_dni = True

if edad >=18 and tiene_dni:
    print("puedes votar")

#en or basta con que una sea verdadera para que sea verdadero
dia = "sabado"

if dia == "sabado" or dia == "domingo":
    print ("esfin de semana")