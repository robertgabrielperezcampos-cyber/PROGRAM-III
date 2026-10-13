# Laboratorio 2 Computo 1 - Programacion Computacional III
# Estudiante: Robert Gabriel Perez Campos


def ejercicio_facturacion():
    print("\n*** GENERACION DE FACTURA ***")

    nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    precio_unitario = float(input("Ingrese el precio unitario del producto: $"))
    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    descuento = float(input("Ingrese el descuento que se aplicara: $"))
    propina = float(input("Ingrese la propina: $"))

    subtotal = precio_unitario * cantidad_producto

    if descuento > subtotal:
        print("El descuento no puede superar el subtotal. Se aplicara un descuento de $0.00.")
        descuento = 0.0

    subtotal_con_descuento = subtotal - descuento
    total_final = subtotal_con_descuento + propina

    print("\n" + "=" * 42)
    print("              FACTURA")
    print("=" * 42)
    print(f"Cliente:                  {nombre_cliente}")
    print(f"Precio unitario:          ${precio_unitario:.2f}")
    print(f"Cantidad:                  {cantidad_producto}")
    print(f"Subtotal:                 ${subtotal:.2f}")
    print(f"Descuento:                -${descuento:.2f}")
    print(f"Subtotal con descuento:   ${subtotal_con_descuento:.2f}")
    print(f"Propina:                  +${propina:.2f}")
    print("-" * 42)
    print(f"TOTAL FINAL:              ${total_final:.2f}")
    print("=" * 42)


def mostrar_inventario(inventario):
    print("\n*** REPORTE DE INVENTARIO ***")
    print("-" * 42)
    for ingrediente, cantidad in inventario.items():
        print(f"{ingrediente.title():25} {cantidad:.2f} unidades")
    print("-" * 42)


def ejercicio_inventario():
    inventario = {
        "arroz": 50.0,
        "frijoles": 40.0,
        "carne": 30.0,
        "pollo": 35.0,
        "tomate": 25.0,
        "cebolla": 20.0
    }

    print("\n*** CONTROL DE INVENTARIO ***")
    mostrar_inventario(inventario)

    cantidades_solicitadas = {}
    cantidad_ingredientes = int(input("\nCuantos ingredientes desea retirar?: "))

    for numero in range(1, cantidad_ingredientes + 1):
        print(f"\nIngrediente {numero} de {cantidad_ingredientes}")
        ingrediente = input("Nombre del ingrediente: ").strip().lower()
        cantidad = float(input("Cantidad que desea retirar: "))

        # Si se solicita dos veces el mismo ingrediente, se suman las cantidades.
        cantidades_solicitadas[ingrediente] = cantidades_solicitadas.get(ingrediente, 0) + cantidad

    solicitud_valida = True

    # Primero se comprueba toda la solicitud sin modificar el inventario.
    for ingrediente, cantidad in cantidades_solicitadas.items():
        if ingrediente not in inventario:
            print(f"No existe el ingrediente '{ingrediente}' en el inventario.")
            solicitud_valida = False
        elif cantidad <= 0:
            print(f"La cantidad solicitada de '{ingrediente}' debe ser mayor que cero.")
            solicitud_valida = False
        elif cantidad > inventario[ingrediente]:
            print(
                f"No hay suficiente {ingrediente}. "
                f"Disponible: {inventario[ingrediente]:.2f}, solicitado: {cantidad:.2f}."
            )
            solicitud_valida = False

    # Solo se descuentan ingredientes cuando toda la solicitud es valida.
    if solicitud_valida:
        for ingrediente, cantidad in cantidades_solicitadas.items():
            inventario[ingrediente] -= cantidad
        print("\nTodos los ingredientes fueron retirados correctamente.")
    else:
        print("\nLa operacion fue cancelada. No se modifico ningun ingrediente.")

    mostrar_inventario(inventario)


def ejercicio_platillo_mas_vendido():
    print("\n*** REGISTRO DE PLATILLOS VENDIDOS ***")

    ventas = {}
    cantidad_registros = int(input("Cuantos registros de ventas desea ingresar?: "))

    for numero in range(1, cantidad_registros + 1):
        print(f"\nRegistro {numero} de {cantidad_registros}")
        platillo = input("Nombre del platillo: ").strip().title()
        cantidad = int(input("Cantidad vendida: "))

        if cantidad > 0:
            ventas[platillo] = ventas.get(platillo, 0) + cantidad
        else:
            print("La cantidad debe ser mayor que cero. Este registro no se agregara.")

    if len(ventas) == 0:
        print("\nNo se registraron ventas validas.")
        return

    mayor_cantidad = max(ventas.values())
    platillos_mas_vendidos = []

    for platillo, cantidad in ventas.items():
        if cantidad == mayor_cantidad:
            platillos_mas_vendidos.append(platillo)

    print("\n*** REPORTE DE VENTAS ***")
    for platillo, cantidad in ventas.items():
        print(f"{platillo}: {cantidad} unidades")

    if len(platillos_mas_vendidos) == 1:
        print(
            f"\nEl platillo mas vendido fue {platillos_mas_vendidos[0]} "
            f"con {mayor_cantidad} unidades."
        )
    else:
        print(f"\nExiste un empate con {mayor_cantidad} unidades vendidas.")
        print("Los platillos mas vendidos fueron:")
        for platillo in platillos_mas_vendidos:
            print(f"- {platillo}")


class Empleado:
    def __init__(self, nombre, edad, meses_trabajados, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.meses_trabajados = meses_trabajados
        self.salario_base = salario_base

    def calcular_salario_actual(self):
        anios_completos = self.meses_trabajados // 12
        aumento = self.salario_base * 0.10 * anios_completos
        return self.salario_base + aumento

    def mostrar_informacion(self):
        anios_completos = self.meses_trabajados // 12
        print(f"Nombre completo:          {self.nombre}")
        print(f"Edad:                     {self.edad} anios")
        print(f"Tiempo trabajado:         {self.meses_trabajados} meses")
        print(f"Anios completos:          {anios_completos}")
        print(f"Salario base:             ${self.salario_base:.2f}")
        print(f"Salario con aumentos:     ${self.calcular_salario_actual():.2f}")


class Cocinero(Empleado):
    def __init__(self, nombre, edad, meses_trabajados, salario_base, especialidad):
        super().__init__(nombre, edad, meses_trabajados, salario_base)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print("\n*** INFORMACION DEL COCINERO ***")
        super().mostrar_informacion()
        print(f"Especialidad:              {self.especialidad}")


class Mesero(Empleado):
    def __init__(self, nombre, edad, meses_trabajados, salario_base, turno):
        super().__init__(nombre, edad, meses_trabajados, salario_base)
        self.turno = turno

    def mostrar_informacion(self):
        print("\n*** INFORMACION DEL MESERO ***")
        super().mostrar_informacion()
        print(f"Turno:                     {self.turno.title()}")


def pedir_datos_generales_empleado():
    nombre = input("Ingrese el nombre completo: ").strip()
    edad = int(input("Ingrese la edad: "))
    meses_trabajados = int(input("Ingrese el tiempo trabajado en meses: "))
    salario_base = float(input("Ingrese el salario base: $"))
    return nombre, edad, meses_trabajados, salario_base


def ejercicio_empleados():
    empleados = []

    print("\n*** REGISTRO DE EMPLEADOS ***")

    while True:
        print("\n1- Registrar cocinero")
        print("2- Registrar mesero")
        print("3- Mostrar empleados")
        print("4- Regresar al menu principal")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre, edad, meses, salario = pedir_datos_generales_empleado()
            especialidad = input("Ingrese la especialidad del cocinero: ").strip()
            empleados.append(Cocinero(nombre, edad, meses, salario, especialidad))
            print("Cocinero registrado correctamente.")

        elif opcion == "2":
            nombre, edad, meses, salario = pedir_datos_generales_empleado()

            while True:
                turno = input("Ingrese el turno (matutino/vespertino): ").strip().lower()
                if turno == "matutino" or turno == "vespertino":
                    break
                print("Turno no valido. Solo puede ingresar matutino o vespertino.")

            empleados.append(Mesero(nombre, edad, meses, salario, turno))
            print("Mesero registrado correctamente.")

        elif opcion == "3":
            if len(empleados) == 0:
                print("No hay empleados registrados.")
            else:
                for empleado in empleados:
                    empleado.mostrar_informacion()
                    print("-" * 45)

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")


def menu_principal():
    while True:
        print("\n" + "=" * 48)
        print("       LABORATORIO 2 - PRIMER COMPUTO")
        print("=" * 48)
        print("1- Generacion de factura")
        print("2- Control de inventario")
        print("3- Platillo mas vendido")
        print("4- Registro de empleados")
        print("5- Salir")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                ejercicio_facturacion()
            elif opcion == "2":
                ejercicio_inventario()
            elif opcion == "3":
                ejercicio_platillo_mas_vendido()
            elif opcion == "4":
                ejercicio_empleados()
            elif opcion == "5":
                print("Programa finalizado. Hasta luego.")
                break
            else:
                print("Opcion no valida. Seleccione una opcion del 1 al 5.")
        except ValueError:
            print("Error: debe ingresar un valor numerico del tipo solicitado.")


menu_principal()


"""
PREGUNTAS DE ANALISIS

1. En el Ejercicio 2, es importante verificar la disponibilidad de todos los
ingredientes antes de descontar cualquiera porque la salida representa una sola
operacion. Si se descuentan uno por uno y al final uno no tiene suficiente
existencia, los primeros ya habrian sido modificados aunque la receta no pueda
completarse. La verificacion previa evita dejar el inventario parcialmente
actualizado y conserva la consistencia de las cantidades almacenadas.

2. La herencia permite colocar en la clase Empleado los atributos y metodos que
comparten cocineros y meseros. De esta manera no se repiten el nombre, edad,
tiempo trabajado, salario ni el calculo del aumento. Si Hernan solicita un tercer
tipo de empleado, solamente se crea otra clase que herede de Empleado y se
agregan los atributos particulares de ese nuevo tipo. Esto facilita reutilizar
y mantener el codigo.

3. En este programa la propina se ingresa como una cantidad fija de dinero, por
lo tanto, calcularla antes o despues del descuento produciria el mismo total,
porque su valor no depende del subtotal. Si la propina fuera un porcentaje del
subtotal, calcularla antes del descuento daria un total mayor cuando existe un
descuento, ya que el porcentaje se aplicaria sobre una cantidad mas grande.
"""
