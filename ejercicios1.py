def ejercicio1():
    num1 = 4
    num2 = 12
    print(4 + 1)

def menu():
    ejercicios = '1. A partir de una variable num1 con valor inicial 12 y una variable num2 con valor inicial 4, crear nuevas variables que almacenen el resultado de realizar la suma, resta, multiplicación, división y resto de num1 y num2. Mostrar el valor de las nuevas variables por pantalla. \n\n' \
    '2. Escribir un programa en el cual se piden cuatro números y se calcule e imprima la suma de los dos primeros y el producto del tercero y el cuarto. '

    while True:
        print(ejercicios)

        ejercicio = input('\nSelecciona el ejercicio (ej 1, 2, 3, 4), 0 para salir: ')

        match ejercicio:
            case "1":
                ejercicio1()

        print()
        
        if ejercicio == "0":
            break
    

def main():
    menu()

if __name__ == "__main__":
    main()