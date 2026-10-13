#Realizar un codigo que gestione una tienda
#La tienda debe poder:
#Ingresar producto
#Ver los productos en cualquier momento
#Todo se manejara por un menu que funcionara
#en bucle hasta que el usuario se saga por completo
#Se tiene que poder regresar al menu principal
#Ejemplo.
#Menu
#1-Ingresar producto
#2-Ver inventario
#3-Salir

print("**Bienvenido a la tienda**")
inventario = []

while True:
    print("\nMenu:")
    print("1- Ingresar producto")
    print("2- Ver inventario")
    print("3- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Producto agregado al inventario.")
    elif opcion == "2":
        print("\nInventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

        