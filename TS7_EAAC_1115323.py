#Introducción a la programación 21/09/2023
print("Estephanie Alexandra Arana Corado")
while True:
    try:
        y = int(input("Por favor, ingrese un número del 1 al 10: "))
        if 1 <= y <= 10:
            for i in range(1, 11):
                resultado = y * i
                print(f"{y} x {i} = {resultado}")
            opcion = input("¿Deseas generar la tabla de otro número? (si/no): ")
            if opcion.lower() != 'si':
                break
        else:
            print("El número debe estar en el rango del 1 al 10. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingrese otro número del 1 al 10: ")