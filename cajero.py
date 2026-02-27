print("Bienvenido al cajero automático")
print("Por favor, ingrese su número de cuenta:")
numero_cuenta = input()
print("Por favor, ingrese su PIN:")
pin = input()
print("Seleccione una opción:")
print("1. Consultar saldo")
print("2. Retirar efectivo")
print("3. Depositar efectivo")
opcion = input()
if opcion == "1":
    print("Su saldo es: $1000")
elif opcion == "2":    
    print("Ingrese la cantidad a retirar:")
    cantidad = input()
    print(f"Ha retirado ${cantidad}")
elif opcion == "3":   
    print("Ingrese la cantidad a depositar:")
    cantidad = input()
    print(f"Ha depositado ${cantidad}")
else:  
    print("Opción no válida")
    print("Gracias por usar el cajero automático")
