from datetime import timedelta

def ejercicio1():
    num1 = 4
    num2 = 12
    print(4 + 1)

'''def ejercicio2():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    n3 = int(input("Número 3: "))
    n4 = int(input("Número 4: "))

    print("suma : ", n1+n2, "- multiplicación : ", n3*n4)
'''

'''def ejercicio2():
    #listas mutables
    numeros = []

    for i in range(4):
        numeros.append(int(input(f"Número {i+1} : ")))

    print(f"suma = {numeros[0] + numeros[1]} \nmultiplicación = {numeros[2] * numeros[3]}")    
'''

'''def ejercicio2():
    #listas mutables
    numeros = [0,0,0,0]

    for i in range(4):
        numeros[i] = int(input(f"Número {i+1} : "))

    print(f"suma = {numeros[0] + numeros[1]} \nmultiplicación = {numeros[2] * numeros[3]}")    
'''

def ejercicio2():
    #tuplas inmutables
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    n3 = int(input("Número 3: "))
    n4 = int(input("Número 4: "))

    numeros = (n1,n2,n3,n4)

    print(f"suma = {numeros[0] + numeros[1]} \nmultiplicación = {numeros[2] * numeros[3]}")

def ejercicio3():
      n = int(input("Digita el número: "))

      operacion = ((n+1)*n+2)*n+3
      print(str(operacion))

def ejercicio4():
    n_ardillas = int(input("Número de ardillas: "))
    n_nueces = int(input("Númeor de nueces: "))

    print(f"Corresponen {n_nueces//n_ardillas} a cada ardilla y sobran {n_nueces%n_ardillas} nueces")

def ejercicio5():
    c_minutos = float(input("Cantidad de minutos: "))
    
    horas = c_minutos // 60
    minutos = c_minutos % 60
    
    print(f"horas = {horas}, minutos = {minutos}")

'''def ejercicio6():
    c_segundos = int(input("Cantidad de segundos: "))
    
    # divmod devuelve (cociente, residuo)
    
    #es como retornar una tupla y se puede leer igualando en orden los elementos
    minutos, resto_segundos = divmod(c_segundos, 60)
    horas, resto_minutos = divmod(minutos, 60)
    
    print(f"horas: {horas} - minutos: {resto_minutos} - segundos: {resto_segundos}")
'''  

'''def ejercicio6_datetime():
    c_segundos = int(input("Cantidad de segundos: "))
    
    # Convierte los segundos en un objeto de tiempo
    tiempo = timedelta(seconds=c_segundos)
    
    tiempo_texto = str(tiempo) # Convierte "2:30:15" en texto
    horas, minutos, segundos = tiempo_texto.split(":")
    
    print(f"horas: {horas} - minutos: {minutos} - segundos: {segundos}")
'''

def ejercicio6():
    c_segundos = int(input("Cantidad de segundos: "))
    
    minutos = c_segundos // 60
    resto_segundos = c_segundos % 60
    horas = minutos // 60
    resto_minutos = minutos % 60
    
    print(f"horas: {horas} - minutos: {resto_minutos} - segundos: {resto_segundos}")
    
def ejercicio7():
    n = int(input('Digita un número de dos digitos: '))
    print(f'Decenas: {n//10}')
    print(f'Unidades: {n%10}')

def ejercicio8():
    n = int(input('Digita un número de dos cifras: '))
    n_invertido_forma1 = (n % 10) * 10 + (n // 10)
    n_invertido_forma2 = f'{n%10}{n//10}'
    n_invertido_forma3 = str(n)[1] + str(n)[0]
    n_invertido_forma4 = n[::-1]
    print(f'Cifras invertidas: {n_invertido_forma4}')

def menu():
    ejercicios = '1. A partir de una variable num1 con valor inicial 12 y una variable num2 con valor inicial 4, crear nuevas variables que almacenen el resultado de realizar la suma, resta, multiplicación, división y resto de num1 y num2. Mostrar el valor de las nuevas variables por pantalla.' \
    '\n\n2. Escribir un programa en el cual se piden cuatro números y se calcule e imprima la suma de los dos primeros y el producto del tercero y el cuarto. ' \
    '\n\n3.Escribe un programa que lea un valor entero n de la entrada estándar y muestre el resultado de la siguiente expresión aritmética: ((n + 1) \* n + 2) \* n + 3'
    '\n\n4. Unas ardillas encuentran unas nueces y deciden dividirlas equitativamente. Escribe un programa que pregunte por el número de ardillas y nueces, y, a continuación, calcule (y muestre) cuántas nueces corresponden a cada ardilla y cuántas sobrarán tras el reparto.'
    '\n\n5. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.' \
    '\n\n6. Escribe un programa que reciba un tiempo en segundos y muestre por pantalla este tiempo pero expresado en horas, minutos y segundos. Por ejemplo, 12.610 segundos son 3 horas, 30 minutos y 10 segundos.' \
    '\n\n7. Escribe un programa que pida un número de dos dígitos e imprima las decenas.' \
    '\n\n8. Escribe un programa que pida un número de dos cifras y muestre sus cifras invertidas.. Ejemplo, si se introduce 23 que muestre 32\.'
        
    while True:
        print(ejercicios)

        ejercicio = input('\nSelecciona el ejercicio (ej 1, 2, 3, 4), 0 para salir: ')

        match ejercicio:
            case "1":
                ejercicio1()

            case "2":
                ejercicio2()

            case "3":
                ejercicio3()

            case "4":
                ejercicio4()
            
            case "5":
                ejercicio5()
                
            case "6":
                ejercicio6()
                
            case "7":
                ejercicio7()
            
            case "8":
                ejercicio8()
                
        print()
        
        if ejercicio == "0":
            break
    
def main():
    menu()

if __name__ == "__main__":
    main()