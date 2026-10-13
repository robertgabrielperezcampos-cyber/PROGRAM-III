# RONDA 2 CORREGIDA
# Ejercicio: consultar y vender productos de un inventario.

inventario = {
    "arroz": {"precio": 1.25, "stock": 10},
    "frijoles": {"precio": 1.50, "stock": 8},
    "aceite": {"precio": 3.75, "stock": 5}
}

try:
    producto = input("Producto que desea comprar: ").strip().lower()

    if producto not in inventario:
        raise KeyError(producto)

    cantidad = int(input("Cantidad: "))

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    precio = inventario[producto]["precio"]
    stock = inventario[producto]["stock"]

    if cantidad > stock:
        print(f"Stock insuficiente. Solo hay {stock} unidades.")
    else:
        inventario[producto]["stock"] = stock - cantidad
        total = precio * cantidad
        descuento = total * 0.10
        total_final = total - descuento

        print(f"Subtotal: ${total:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"Total a pagar: ${total_final:.2f}")
        print(f"Stock restante: {inventario[producto]['stock']}")

except ValueError as error:
    print(f"Error en la cantidad: {error}")
except KeyError:
    print("El producto solicitado no existe en el inventario.")
finally:
    print("Consulta de inventario finalizada.")
