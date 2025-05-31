# Este archivo es para crear la calculadora
# La Calculadora es un programa que permite realizar operaciones matemáticas básicas
# Como suma, resta, multiplicación y división.
# Yo Mateo Realizare las operaciones de multiplicacion y division



#Con este comando la calculadora para a pedir el ingreso de los numeros
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))


#Con este comando la calculadora para a pedir el ingreso de la operación
n = int("Selecciona la operación que deseas realizar: \n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n")


def validacion(n):
    # Con estos comandos la calculadora realiza las operaciones
    if n == 1:
        return numero1 + numero2
    elif n == 2:
        return numero1 - numero2
    elif n == 3:
        return numero1 * numero2
    elif n == 4:
        return numero1 / numero2



def main():
    # Imprime el resultado
    print("El resultado de la operación es:", validacion(n))