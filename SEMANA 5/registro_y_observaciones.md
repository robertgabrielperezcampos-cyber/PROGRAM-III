# Actividad Formativa - Semana 5

**Integrantes:** Robert Gabriel Pérez Campos y ____________________  
**Objetivo:** Utilizar traceback, impresiones de seguimiento y manejo de excepciones para diagnosticar y corregir programas.

## Tabla de registro
a | Excepción capturada | Técnica utilizada | Solución aplicada |
|---:|---|---|---|---|---|
| N.° | Tipo de error | Descripción del error y línea aproximad
| 1 | Sintaxis | Ronda 1, línea 14: faltaban los dos punto la línea indicada. | Se agregó `:` al final de la condición. |
| 2 | Runtime | Ronda 1, línea 12: el promedio dividía `nota3` entre cero. | `ZeroDivisionError` se diagnosticó; se eliminó la operación incorrecta. | Traceback e inspección de ls después de `if promedio >= 6`. | No aplica. Un `SyntaxError` debe corregirse antes de ejecutar. | Traceback y revisión dea expresión. | Se cambió a `(nota1 + nota2 + nota3) / 3`. |
| 3 | Runtime | Ronda 1, línea 20: se intentaba concatenar texto con un valor `float`. | `TypeError` se diagnosticó; la salida se corrigió con formato. | Traceback y `print(type(promedio))`. | Se utilizó `print(f"Promedio: {promedio:.2f}")`. |
| 4 | Runtime | Ronda 2, línea 15: una clave inexistente producía un fallo al consultar el diccionario. | `KeyError`. | Traceback y observación de claves con `print(inventario.keys())`. | Se verificó la existencia y se agregó `except KeyError`. |
| 5 | Lógico | Ronda 2, línea 23: el descueto se sumaba y aumentaba el total. | No aplica. | Prueba manual y seguimiento con `print` de total y descuento. | Se cambió a `total_final = total - descuento`. |
| 6 | Runtime | Ronda 2, línea 28: se concatenaba una cadena con un entero. | `TypeError` se diagnosticó; la salida se corrigió con formato. | Traceback e inspección del tipo de `stock`. | Se empleó una f-string para mostrar el stock. |

> Las líneas son aproximadas y corrnesponden a los archivos con errores entregados en este paquete.

## Observaciones de la pareja

### 1. ¿Qué tipo de error fue más fácil y cuál fue más difícil?

El error de sintaxis fue el más fácil de detectar porque Python detuvo el programa antes de ejecutarlo y el traceback señaló la línea donde faltaban los dos puntos. Los errores lógicos fueron los más difíciles porque el programa podía ejecutarse sin mostrar una excepción, pero producía un resultado incorrecto. En la segunda ronda, el descuento se sumaba al total en vez de restarse. Para detectarlo fue necesario comparar el resultado del programa con un cálculo manual.

### 2. ¿Qué técnica de debugging fue más útil y en qué situación?

El traceback fue la técnica más útil para los errores de ejecución porque mostró el tipo de excepción y la línea del fallo. Las impresiones de seguimiento fueron más útiles para el error lógico del descuento, ya que permitieron observar por separado el subtotal, el descuento y el total final. También se puede colocar un breakpoint antes del cálculo del total para inspeccionar esas variables paso a paso en el depurador de Visual Studio Code.
