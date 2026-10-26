# Función para sumar dos números
def sumar(a, b):
    return a + b


# Solicitar los números al usuario
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Calcular y mostrar el resultado
    resultado = sumar(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")