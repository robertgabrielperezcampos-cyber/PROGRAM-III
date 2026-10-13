#Ejemplo 1.
#Una tienda necesita registrar productos
#cada producto tiene un codigo nombre y stock
#El stock puede cambiar

inventario = [("ID001", "Lapicero", 50)
              ("ID002", "Cuaderno", 50)]
print("**Ingreso de nueva producto**")
while True:
    nuevocod = input("Ingresa el codigo del producto: ")
    nuevonom = input("Ingresa el nombre del producto: ")
    nuevostock = int(input("Ingresa el stock del producto: "))
    nuevoprod = (nuevocod, nuevonom, nuevostock)
    inventario.append(nuevoprod)
    opcion = input("Deseas agregar otro producto? (s/n): ").strip().lower()
    if (opcion == 's'):
        continue
    else:
        break
          
print("**Inventario de actual**")
nprod = 1
for codigo, nombre, stock in inventario:
    print(f"{nprod}*" +
          f"Codigo ------ {codigo}\n"+
          f"Nombre ------ {nombre}\n"+
          f"Stock ------- {stock}\n")
    print("*************************")
    nprod+=1