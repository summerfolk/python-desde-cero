cantidad_de_soles = float(input("ingrese la cantidad de soles que desea convertir:"))

valor_del_cambio = 3.75

valor_convertido_en_dolares = round(cantidad_de_soles / valor_del_cambio, 2)

print(f"el valor convertido en dolares es: {valor_convertido_en_dolares}")