def Menu():
    print("--- MENU ---")
    print("1. Factorial")
    print("2. Suma de N numeros naturales")
    print("3. Fibonacci")
    print("4. Letra en una palabra")
    print("5. Invertir Palabra")
    print("6. Potencia")
    print("7. Salir")

while True:
    Menu()
    try:
        opcion=int(input("Ingresa una opcion: "))
        match opcion:
            case 1:
                print("Factorial")
            case 2:
                print("Suma de N numeros naturales")
            case 3:
                print("Fibonacci")
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