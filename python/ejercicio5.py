# Ejercicio 5: Descuento en compras
# Instrucciones:
# - Pedir al usuario el monto total de la compra.
# - Si el monto es mayor a $50.000, aplicar un 15% de descuento.
# - Mostrar el monto final a pagar y el descuento aplicado.

# Tu código aquí:

# Pedir el monto total:
monto_inicial = float(input("ingrese el monto: "))
descuento = float(input("ingresar valor del descuento"))
# Verificar si corresponde descuento:
if monto_inicial >= 50000:
    descuento = (monto_inicial * descuento) / 100
    monto_final = (monto_inicial - descuento)
    print("el monto luego del descuento es:", monto_final)
else:
    monto_inicial < 50000
    monto_final = monto_inicial
    print("no conseguiste el descuento, asi que tu monto final es: ", monto_final)
print("tu total a pagar es:", monto_final)

# Calcular el monto final y el descuento si es necesario:

# Mostrar el resultado: 
# print("El total a pagar es:", ...)
