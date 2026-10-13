# Parcial de Primer Computo
# Sistema de tienda de electronica
"""
Integrantes:
             Anderson Oziel Cruz Medina
             Robert Gabriel Pérez Campos 
"""

# Funcion externa numero 1
# Valida el ingreso de numeros enteros
def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("El numero no puede ser negativo")
                continue

            return numero

        except ValueError:
            print("Error, debe ingresar un numero entero valido")


# Funcion externa numero 2
# Valida el ingreso de numeros decimales
def validar_decimal(mensaje):
    while True:
        try:
            numero = float(input(mensaje))

            if numero < 0:
                print("El numero no puede ser negativo")
                continue

            return numero

        except ValueError:
            print("Error, debe ingresar un numero valido")


# Clase principal o clase padre
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Metodo 1
    def mostrar_informacion(self):
        print("\n*** Informacion del producto ***")
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Unidades disponibles: {self.stock}")

    # Metodo 2
    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero")
            return False

        if cantidad > self.stock:
            print("No hay suficientes unidades disponibles")
            return False

        self.stock -= cantidad
        total = self.precio * cantidad

        print("\nVenta realizada correctamente")
        print(f"Producto: {self.nombre}")
        print(f"Cantidad vendida: {cantidad}")
        print(f"Total de la venta: ${total:.2f}")
        print(f"Unidades restantes: {self.stock}")

        return True


# Clase hija
class ProductoElectronico(Producto):
    def __init__(self, codigo, nombre, precio, stock,
                 marca, categoria, garantia, disponible=True):

        super().__init__(codigo, nombre, precio, stock)

        self.marca = marca
        self.categoria = categoria
        self.garantia = garantia
        self.disponible = disponible

    # Sobrescritura del metodo mostrar_informacion
    def mostrar_informacion(self):
        super().mostrar_informacion()

        print(f"Marca: {self.marca}")
        print(f"Categoria: {self.categoria}")
        print(f"Garantia: {self.garantia} meses")

        if self.disponible and self.stock > 0:
            print("Estado: Disponible")
        else:
            print("Estado: No disponible")

    # Metodo con valor por defecto
    def calcular_precio_final(self, descuento=0.10):
        precio_final = self.precio - (self.precio * descuento)
        return precio_final

    # Segundo comportamiento propio de la clase hija
    def actualizar_disponibilidad(self):
        if self.stock > 0:
            self.disponible = True
        else:
            self.disponible = False


# Funcion externa numero 3
# Busca un producto dentro de la lista mediante su codigo
def buscar_producto(lista_productos, codigo):
    for producto in lista_productos:
        if producto.codigo.lower() == codigo.lower():
            return producto

    return None


# Funcion externa numero 4
# Registra los datos ingresados por el usuario
def registrar_producto(lista_productos, categorias):
    print("\n*** Registrar producto electronico ***")

    while True:
        codigo = input("Ingrese el codigo del producto: ").strip()

        if codigo == "":
            print("El codigo no puede quedar vacio")
            continue

        producto_existente = buscar_producto(lista_productos, codigo)

        if producto_existente is not None:
            print("Ya existe un producto con ese codigo")
            continue

        break

    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre != "":
            break

        print("El nombre no puede quedar vacio")

    precio = validar_decimal("Ingrese el precio del producto: $")
    stock = validar_entero("Ingrese la cantidad disponible: ")

    while True:
        marca = input("Ingrese la marca del producto: ").strip()

        if marca != "":
            break

        print("La marca no puede quedar vacia")

    print("\nCategorias disponibles:")

    for categoria in categorias:
        print(f"- {categoria}")

    while True:
        categoria = input("Ingrese la categoria: ").strip().title()

        if categoria in categorias:
            break

        print("La categoria ingresada no es valida")

    garantia = validar_entero("Ingrese los meses de garantia: ")

    producto = ProductoElectronico(
        codigo,
        nombre,
        precio,
        stock,
        marca,
        categoria,
        garantia
    )

    lista_productos.append(producto)

    print("\nProducto registrado correctamente")


# Funcion para mostrar todos los productos
def mostrar_productos(lista_productos):
    print("\n*** Inventario de productos ***")

    if len(lista_productos) == 0:
        print("No hay productos registrados")
        return

    for producto in lista_productos:
        producto.actualizar_disponibilidad()
        producto.mostrar_informacion()
        print("-" * 35)


# Funcion para consultar un producto
def consultar_producto(lista_productos):
    codigo = input("Ingrese el codigo del producto: ").strip()

    producto = buscar_producto(lista_productos, codigo)

    if producto is None:
        print("No se encontro un producto con ese codigo")
    else:
        producto.actualizar_disponibilidad()
        producto.mostrar_informacion()


# Funcion para realizar una venta
def realizar_venta(lista_productos):
    print("\n*** Venta de producto ***")

    codigo = input("Ingrese el codigo del producto: ").strip()
    producto = buscar_producto(lista_productos, codigo)

    if producto is None:
        print("No se encontro un producto con ese codigo")
        return

    producto.mostrar_informacion()

    cantidad = validar_entero(
        "Ingrese la cantidad que desea comprar: "
    )

    producto.vender(cantidad)
    producto.actualizar_disponibilidad()


# Funcion para calcular descuentos
def consultar_descuento(lista_productos):
    print("\n*** Consultar precio con descuento ***")

    codigo = input("Ingrese el codigo del producto: ").strip()
    producto = buscar_producto(lista_productos, codigo)

    if producto is None:
        print("No se encontro un producto con ese codigo")
        return

    print(f"\nProducto: {producto.nombre}")
    print(f"Precio normal: ${producto.precio:.2f}")

    while True:
        aplicar_otro = input(
            "¿Desea ingresar un descuento diferente al 10%? (s/n): "
        ).lower()

        if aplicar_otro == "s":
            porcentaje = validar_decimal(
                "Ingrese el porcentaje de descuento: "
            )

            if porcentaje > 100:
                print("El descuento no puede ser mayor al 100%")
                continue

            descuento = porcentaje / 100
            precio_final = producto.calcular_precio_final(descuento)
            break

        elif aplicar_otro == "n":
            # Se utiliza el valor predeterminado del 10%
            precio_final = producto.calcular_precio_final()
            porcentaje = 10
            break

        else:
            print("Seleccione solamente s o n")

    print(f"Descuento aplicado: {porcentaje}%")
    print(f"Precio final: ${precio_final:.2f}")


# Funcion para mostrar resumen del inventario
def mostrar_resumen(lista_productos):
    cantidad_productos = len(lista_productos)
    total_unidades = 0
    valor_inventario = 0.0

    for producto in lista_productos:
        total_unidades += producto.stock
        valor_inventario += producto.precio * producto.stock

    print("\n*** Resumen del inventario ***")
    print(f"Productos diferentes: {cantidad_productos}")
    print(f"Total de unidades: {total_unidades}")
    print(f"Valor del inventario: ${valor_inventario:.2f}")


# Funcion principal que contiene el menu
def menu():
    # Lista para agrupar los objetos registrados
    productos = []

    # Tupla de categorias disponibles
    categorias = (
        "Computadoras",
        "Telefonos",
        "Televisores",
        "Accesorios",
        "Audio"
    )

    # Diccionario con datos generales de la tienda
    tienda = {
        "nombre": "ElectroTech",
        "telefono": "2661-0000"
    }

    sistema_activo = True

    while sistema_activo:
        print("\n===================================")
        print(f"       {tienda['nombre']}")
        print("   Sistema de control de productos")
        print("===================================")
        print("1. Registrar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto")
        print("4. Realizar venta")
        print("5. Consultar precio con descuento")
        print("6. Mostrar resumen del inventario")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(productos, categorias)

        elif opcion == "2":
            mostrar_productos(productos)

        elif opcion == "3":
            consultar_producto(productos)

        elif opcion == "4":
            realizar_venta(productos)

        elif opcion == "5":
            consultar_descuento(productos)

        elif opcion == "6":
            mostrar_resumen(productos)

        elif opcion == "7":
            sistema_activo = False
            print("\nGracias por utilizar el sistema")
            print(f"Telefono de la tienda: {tienda['telefono']}")

        else:
            print("Opcion incorrecta, intente nuevamente")

menu()


"""
DESCRIPCION DEL SISTEMA:
Este sistema permite administrar los productos de una tienda de electronica.
El usuario puede registrar, consultar y vender productos, calcular descuentos
y visualizar un resumen general del inventario.

ENTIDADES O CLASES IDENTIFICADAS:
1. Producto: representa la informacion general de un producto de la tienda.
2. ProductoElectronico: representa un producto electronico y hereda las
   caracteristicas y comportamientos de la clase Producto.

DESCRIPCION DE LAS CLASES:
Clase Producto:
Atributos: codigo, nombre, precio y stock.
Metodos: mostrar_informacion() muestra los datos del producto y vender()
permite realizar una venta y disminuir las existencias.

Clase ProductoElectronico:
Atributos heredados: codigo, nombre, precio y stock.
Atributos propios: marca, categoria, garantia y disponible.
Metodos: mostrar_informacion() presenta toda la informacion,
calcular_precio_final() aplica un descuento y
actualizar_disponibilidad() actualiza el estado del producto.
"""