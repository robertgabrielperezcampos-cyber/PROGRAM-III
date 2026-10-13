import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QRadioButton,
    QPushButton,
    QTextEdit,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox
)


class AplicacionPedidos(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicacion de pedidos de comida")
        self.resize(600, 650)

        # Diccionario que agrupa las comidas y sus precios
        self.menu_comidas = {
            "Seleccionar comida": 0.00,
            "Hamburguesa": 5.00,
            "Pizza personal": 6.50,
            "Tacos": 4.00,
            "Pollo frito": 5.50,
            "Pupusas": 3.00
        }

        self.iniciar_interfaz()

    def iniciar_interfaz(self):

        # Titulo principal
        self.titulo = QLabel("APLICACION DE PEDIDOS DE COMIDA")
        self.titulo.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
            "color: white;"
            "background-color: #e67e22;"
            "padding: 12px;"
        )

        # Campos del formulario
        self.edit_nombre = QLineEdit()
        self.edit_nombre.setPlaceholderText(
            "Escriba el nombre del cliente"
        )

        self.edit_telefono = QLineEdit()
        self.edit_telefono.setPlaceholderText(
            "Ejemplo: 77778888"
        )
        self.edit_telefono.setMaxLength(8)

        self.combo_comida = QComboBox()

        for comida in self.menu_comidas:
            self.combo_comida.addItem(comida)

        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        self.spin_cantidad.setMaximum(20)

        self.label_precio = QLabel("$0.00")

        # Layout de formulario
        formulario = QFormLayout()
        formulario.addRow("Nombre del cliente:", self.edit_nombre)
        formulario.addRow("Telefono:", self.edit_telefono)
        formulario.addRow("Comida:", self.combo_comida)
        formulario.addRow("Cantidad:", self.spin_cantidad)
        formulario.addRow("Precio unitario:", self.label_precio)

        grupo_cliente = QGroupBox("Datos del pedido")
        grupo_cliente.setLayout(formulario)

        # Entrega a domicilio
        self.check_domicilio = QCheckBox(
            "Solicitar entrega a domicilio"
        )

        self.edit_direccion = QLineEdit()
        self.edit_direccion.setPlaceholderText(
            "Escriba la direccion del cliente"
        )
        self.edit_direccion.setEnabled(False)

        layout_entrega = QVBoxLayout()
        layout_entrega.addWidget(self.check_domicilio)
        layout_entrega.addWidget(self.edit_direccion)

        grupo_entrega = QGroupBox("Tipo de entrega")
        grupo_entrega.setLayout(layout_entrega)

        # Metodo de pago
        self.radio_efectivo = QRadioButton("Efectivo")
        self.radio_tarjeta = QRadioButton("Tarjeta")

        layout_pago = QHBoxLayout()
        layout_pago.addWidget(self.radio_efectivo)
        layout_pago.addWidget(self.radio_tarjeta)

        grupo_pago = QGroupBox("Metodo de pago")
        grupo_pago.setLayout(layout_pago)

        # Total del pedido
        self.label_total = QLabel("Total del pedido: $0.00")
        self.label_total.setStyleSheet(
            "font-size: 18px;"
            "font-weight: bold;"
            "color: #27ae60;"
        )

        # Botones
        self.boton_registrar = QPushButton("Registrar pedido")
        self.boton_limpiar = QPushButton("Limpiar formulario")
        self.boton_salir = QPushButton("Salir")

        self.boton_registrar.setStyleSheet(
            "background-color: #27ae60;"
            "color: white;"
            "padding: 8px;"
        )

        self.boton_limpiar.setStyleSheet(
            "background-color: #3498db;"
            "color: white;"
            "padding: 8px;"
        )

        self.boton_salir.setStyleSheet(
            "background-color: #c0392b;"
            "color: white;"
            "padding: 8px;"
        )

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_registrar)
        layout_botones.addWidget(self.boton_limpiar)
        layout_botones.addWidget(self.boton_salir)

        # Area que mostrara el pedido registrado
        self.area_resumen = QTextEdit()
        self.area_resumen.setReadOnly(True)
        self.area_resumen.setPlaceholderText(
            "Aqui aparecera el resumen del pedido"
        )

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.titulo)
        layout_principal.addWidget(grupo_cliente)
        layout_principal.addWidget(grupo_entrega)
        layout_principal.addWidget(grupo_pago)
        layout_principal.addWidget(self.label_total)
        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(QLabel("Resumen del pedido:"))
        layout_principal.addWidget(self.area_resumen)

        self.setLayout(layout_principal)

        # Eventos de la aplicacion
        self.combo_comida.currentIndexChanged.connect(
            self.actualizar_total
        )

        self.spin_cantidad.valueChanged.connect(
            self.actualizar_total
        )

        self.check_domicilio.stateChanged.connect(
            self.cambiar_entrega
        )

        self.edit_nombre.textChanged.connect(
            self.validar_nombre_visual
        )

        self.edit_telefono.textChanged.connect(
            self.validar_telefono_visual
        )

        self.boton_registrar.clicked.connect(
            self.registrar_pedido
        )

        self.boton_limpiar.clicked.connect(
            self.limpiar_formulario
        )

        self.boton_salir.clicked.connect(
            self.close
        )

    def obtener_total(self):
        comida = self.combo_comida.currentText()
        precio = self.menu_comidas[comida]
        cantidad = self.spin_cantidad.value()

        total = precio * cantidad

        if self.check_domicilio.isChecked():
            total += 1.50

        return total

    def actualizar_total(self):
        comida = self.combo_comida.currentText()
        precio = self.menu_comidas[comida]

        self.label_precio.setText(f"${precio:.2f}")

        total = self.obtener_total()

        self.label_total.setText(
            f"Total del pedido: ${total:.2f}"
        )

    def cambiar_entrega(self):
        if self.check_domicilio.isChecked():
            self.edit_direccion.setEnabled(True)
        else:
            self.edit_direccion.clear()
            self.edit_direccion.setEnabled(False)

        self.actualizar_total()

    def validar_nombre_visual(self, texto):
        if len(texto.strip()) > 0 and len(texto.strip()) < 3:
            self.edit_nombre.setStyleSheet(
                "border: 2px solid red;"
            )
        else:
            self.edit_nombre.setStyleSheet("")

    def validar_telefono_visual(self, texto):
        if texto != "" and not texto.isdigit():
            self.edit_telefono.setStyleSheet(
                "border: 2px solid red;"
            )
        else:
            self.edit_telefono.setStyleSheet("")

    def validar_datos(self):
        nombre = self.edit_nombre.text().strip()
        telefono = self.edit_telefono.text().strip()
        comida = self.combo_comida.currentText()
        direccion = self.edit_direccion.text().strip()

        if nombre == "":
            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe ingresar el nombre del cliente."
            )
            self.edit_nombre.setFocus()
            return False

        if len(nombre) < 3:
            QMessageBox.warning(
                self,
                "Nombre incorrecto",
                "El nombre debe tener al menos 3 caracteres."
            )
            self.edit_nombre.setFocus()
            return False

        if not nombre.replace(" ", "").isalpha():
            QMessageBox.warning(
                self,
                "Nombre incorrecto",
                "El nombre solamente debe contener letras."
            )
            self.edit_nombre.setFocus()
            return False

        if telefono == "":
            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe ingresar el numero de telefono."
            )
            self.edit_telefono.setFocus()
            return False

        if not telefono.isdigit():
            QMessageBox.warning(
                self,
                "Telefono incorrecto",
                "El telefono solamente debe contener numeros."
            )
            self.edit_telefono.setFocus()
            return False

        if len(telefono) != 8:
            QMessageBox.warning(
                self,
                "Telefono incorrecto",
                "El telefono debe tener exactamente 8 digitos."
            )
            self.edit_telefono.setFocus()
            return False

        if comida == "Seleccionar comida":
            QMessageBox.warning(
                self,
                "Comida no seleccionada",
                "Debe seleccionar una comida."
            )
            self.combo_comida.setFocus()
            return False

        if (
            self.check_domicilio.isChecked()
            and direccion == ""
        ):
            QMessageBox.warning(
                self,
                "Direccion incompleta",
                "Debe escribir la direccion de entrega."
            )
            self.edit_direccion.setFocus()
            return False

        if (
            not self.radio_efectivo.isChecked()
            and not self.radio_tarjeta.isChecked()
        ):
            QMessageBox.warning(
                self,
                "Metodo de pago",
                "Debe seleccionar un metodo de pago."
            )
            return False

        return True

    def registrar_pedido(self):
        if not self.validar_datos():
            return

        nombre = self.edit_nombre.text().strip()
        telefono = self.edit_telefono.text().strip()
        comida = self.combo_comida.currentText()
        cantidad = self.spin_cantidad.value()
        precio = self.menu_comidas[comida]
        total = self.obtener_total()

        if self.check_domicilio.isChecked():
            entrega = "Entrega a domicilio"
            direccion = self.edit_direccion.text().strip()
        else:
            entrega = "Retirar en el restaurante"
            direccion = "No aplica"

        if self.radio_efectivo.isChecked():
            metodo_pago = "Efectivo"
        else:
            metodo_pago = "Tarjeta"

        resumen = (
            "******** PEDIDO REGISTRADO ********\n"
            f"Cliente: {nombre}\n"
            f"Telefono: {telefono}\n"
            f"Comida: {comida}\n"
            f"Precio unitario: ${precio:.2f}\n"
            f"Cantidad: {cantidad}\n"
            f"Tipo de entrega: {entrega}\n"
            f"Direccion: {direccion}\n"
            f"Metodo de pago: {metodo_pago}\n"
            f"TOTAL: ${total:.2f}\n"
            "***********************************"
        )

        self.area_resumen.setText(resumen)

        QMessageBox.information(
            self,
            "Pedido registrado",
            "El pedido fue registrado correctamente."
        )

        # Se borran los datos despues de registrarlos correctamente
        self.limpiar_campos_entrada()

    def limpiar_campos_entrada(self):
        self.edit_nombre.clear()
        self.edit_telefono.clear()
        self.combo_comida.setCurrentIndex(0)
        self.spin_cantidad.setValue(1)
        self.check_domicilio.setChecked(False)
        self.edit_direccion.clear()
        self.radio_efectivo.setAutoExclusive(False)
        self.radio_tarjeta.setAutoExclusive(False)
        self.radio_efectivo.setChecked(False)
        self.radio_tarjeta.setChecked(False)
        self.radio_efectivo.setAutoExclusive(True)
        self.radio_tarjeta.setAutoExclusive(True)
        self.actualizar_total()
        self.edit_nombre.setFocus()

    def limpiar_formulario(self):
        self.limpiar_campos_entrada()
        self.area_resumen.clear()

    def closeEvent(self, evento):
        respuesta = QMessageBox.question(
            self,
            "Confirmar salida",
            "¿Esta seguro de que desea cerrar la aplicacion?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            evento.accept()
        else:
            evento.ignore()


app = QApplication(sys.argv)

ventana = AplicacionPedidos()
ventana.show()

sys.exit(app.exec_())