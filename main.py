def Menu():
    print("--- MENU ---")
    print("1. Factorial")
    print("2. Suma de N numeros naturales")
    print("3. Fibonacci")
    print("4. Letra en una palabra")
    print("5. Invertir Palabra")
    print("6. Potencia")
    print("7. Salir")

def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero - 1)

def Suma(n):
    if n == 0:
        return 0
    else:
        return n + Suma(n-1)
def Fibonacci(numero_fibonacci):
    if numero_fibonacci == 0 or numero_fibonacci == 1:
        return 1
    else:
        return Fibonacci(numero_fibonacci - 2) +Fibonacci(numero_fibonacci - 1)
def Letra_palabra(letra, palabra, numero_letra):
    if numero_letra < 0:
        return 0
    if palabra[numero_letra] == letra:
        return 1 + Letra_palabra(letra, palabra, numero_letra - 1)
    else:
        return Letra_palabra(letra, palabra, numero_letra - 1)
def Palabra_invertida(palabra, numero_letra):
    if numero_letra < 0:
        return ""
    else:
        return palabra[numero_letra] + Palabra_invertida(palabra, numero_letra - 1)

def Potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * Potencia(base, exponente - 1)

while True:
    Menu()
    try:
        opcion=int(input("Ingresa una opcion: "))
        match opcion:
            case 1:
                print("Factorial")
                numero = int(input("Ingresa una numero entero Positivo(Factorial): "))
                print(f"El factorial es: {Factorial(numero)}")
            case 2:
                print("Suma de N numeros naturales")
                numero_natural = int(input("Ingresa un numero entero positivo: "))
                print(f"La suma desde 1 hasta {numero_natural} es: {Suma(numero_natural)}")
            case 3:
                print("Fibonacci")
                numero_fubonacci = int(input("Ingrese un numero entero positivo(Fibonacci): "))
                print(f"El fibonacci es: {Fibonacci(numero_fubonacci)}")
            case 4:
                print("Letra en una palabra")
                palabra = input("Ingresa una palabra: ").lower()
                letra = input("Ingresa una letra: ").lower()
                print(f"La letra ---{letra}--- aparece {Letra_palabra(letra, palabra, len(palabra) - 1)} veces en la palabra ---{palabra}----")
            case 5:
                print("Invertir Palabra")
                palabra = input("Ingresa una palabra: ").lower()
                print(f"Tu palabra invertida es: {Palabra_invertida(palabra, len(palabra) - 1)}")

            case 6:
                print("Potencia")
                numero_potencia = int(input("Ingresa un numero base entero positivo: "))
                exponente = int(input("Ingresa el exponente entero positivo: "))
                print(f"{numero_potencia} con exponente {exponente} es: {Potencia(numero_potencia, exponente)}")
            case 7:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("El valor ingresado no es valido")