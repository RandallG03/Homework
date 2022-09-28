def menu():
    print("App de operaciones.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Verificacion numero primo")
    print("6. Verificacion numeros palindromos")
    print("7. Salir")
    option = input ("Escriba la opcion:")
    option = int(option)
    if option==1: suma()
    elif option==2: resta()
    elif option==3: multiplicacion()
    elif option==4: division()
    elif option==5: verificacionNumeroPrimo()
    elif option==6: verificacionNumerosPalindromos()
    else: exit()

def suma():
    print("")
    number1 = input("Numero 1: ")
    number2 = input("Numero 2: ")
    resultado=float(number1) + float(number2)
    print ("Resultado: ", resultado)
    print("")
    menu()

def resta():
    print("")
    print ("Hacer restas.")
    number1 = input("Numero 1: ")
    number2 = input("Numero 2: ")
    resultado=float(number1) - float(number2)
    print ("Resultado: ", resultado)
    print("")
    menu()

def multiplicacion():
    print("")
    print ("Hacer multiplicacion.")
    number1 = input("Numero 1: ")
    number2 = input("Numero 2: ")
    resultado=float(number1) * float(number2)
    print ("Resultado: ", resultado)
    print("")
    menu()

def division():
    print("")
    print ("Hacer division.")
    number1 = input("Numero 1: ")
    number2 = input("Numero 2: ")
    resultado=float(number1) / float(number2)
    print ("Resultado: ", resultado)
    print("")
    menu()

def verificacionNumeroPrimo():
   primerNumero=input("Ingrese el numero que desea comprobar: ")
   for i in range (2, int(primerNumero)):
     if(int(primerNumero)%i == 0):
                print("No es primo")
     else:
         print("Es primo")
     menu()

def verificacionNumerosPalindromos():
    number1 = int(input("Ingrese el numero"))

    if number1 > 99 and number1 <1000:
        a = number1 // 100
        b = number1 % 10
        if a ==b:
            print("El numero",number1, " es palindromo")
        else:
            print("El numero",number1, " no es palindromo")


menu()