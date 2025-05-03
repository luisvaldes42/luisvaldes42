# Ejercicio 1: Calculadora simple

# Instrucciones:
# - Pedir al usuario el primer número.
# - Pedir al usuario el segundo número.
# - Preguntar qué operación desea realizar (+, -, *, /).
# - Mostrar el resultado con el mensaje: "El resultado es: "

# Tu código aquí:

# Solicitar el primer número:
n1 = float(input("ingrese un numero: "))

# Solicitar el segundo número:
n2 = float(input("ingrese otro numero: "))

# Pedir la operación a realizar:
operación = input("ingresar la operación que desee realizar(+,-,*,/): ")

# Calcular el resultado según la operación:
if operación == "+":
    resultado = n1 + n2
elif operación == "-":
    resultado = n1 - n2
elif operación == "*":
    resultado = n1 * n2
elif operación == "/":
    if n2 != 0:
        resultado = n1 / n2
    else: 
        print("No es posible dividir entre cero")
else:
    print("operación invalida")

# Mostrar el resultado:
# print("El resultado es:", ...)
print("el resultado es:", resultado)