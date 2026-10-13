# RONDA 2 - Programador: Integrante 2
# Ejercicio: consultar y vender productos de un inventario.
# Contiene errores intencionales.

inventario = {
    "arroz": {"precio": 1.25, "stock": 10},
    "frijoles": {"precio": 1.50, "stock": 8},
    "aceite": {"precio": 3.75, "stock": 5}
}

producto = input("Producto que desea comprar: ").strip().lower()
cantidad = int(input("Cantidad: "))

precio = inventario[producto]["precio"]
stock = inventario[producto]["stock"]

if cantidad <= stock:
    inventario[producto]["stock"] = stock - cantidad
    total = precio * cantidad
    descuento = total * 0.10
    total_final = total + descuento
    print(f"Total a pagar: ${total_final:.2f}")
else:
    print("No hay suficiente producto.")

print("Stock restante: " + inventario[producto]["stock"])
