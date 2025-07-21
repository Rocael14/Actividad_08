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

            case 4:
                print("Letra en una palabra")
            case 5:
                print("Invertir Palabra")
            case 6:
                print("Potencia")
            case 7:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("El valor ingresado no es valido")