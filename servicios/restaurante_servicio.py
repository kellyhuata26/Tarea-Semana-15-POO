from datetime import datetime

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self, archivo_servicio):
        self.archivo = archivo_servicio

        self.usuarios = []
        self.productos = []
        self.ventas = []

        self.cargar_datos()

    # =====================================================
    # CARGAR DATOS
    # =====================================================

    def cargar_datos(self):

        datos_usuarios = self.archivo.leer("usuarios.json")
        datos_productos = self.archivo.leer("productos.json")
        datos_ventas = self.archivo.leer("ventas.json")

        self.usuarios = [
            Usuario.desde_diccionario(datos)
            for datos in datos_usuarios
        ]

        self.productos = [
            Producto.desde_diccionario(datos)
            for datos in datos_productos
        ]

        self.ventas = [
            Venta.desde_diccionario(datos)
            for datos in datos_ventas
        ]

    # =====================================================
    # GUARDAR PRODUCTOS
    # =====================================================

    def guardar_productos(self):

        self.archivo.guardar(
            "productos.json",
            [
                producto.a_diccionario()
                for producto in self.productos
            ]
        )

    # =====================================================
    # GUARDAR VENTAS
    # =====================================================

    def guardar_ventas(self):

        self.archivo.guardar(
            "ventas.json",
            [
                venta.a_diccionario()
                for venta in self.ventas
            ]
        )

    # =====================================================
    # LOGIN
    # =====================================================

    def validar_login(self, usuario, password):

        for persona in self.usuarios:

            if (
                persona.usuario == usuario
                and persona.password == password
            ):
                return persona

        return None

    # =====================================================
    # OBTENER USUARIOS
    # =====================================================

    def obtener_usuarios(self):
        return self.usuarios.copy()

    # =====================================================
    # OBTENER PRODUCTOS
    # =====================================================

    def obtener_productos(self):
        return self.productos.copy()

    # =====================================================
    # OBTENER VENTAS
    # =====================================================

    def obtener_ventas(self):
        return self.ventas.copy()

    # =====================================================
    # BUSCAR USUARIO
    # =====================================================

    def buscar_usuario(self, identificacion):

        for usuario in self.usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    # =====================================================
    # BUSCAR PRODUCTO
    # =====================================================

    def buscar_producto(self, codigo):

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    # =====================================================
    # REGISTRAR VENTA
    # =====================================================

    def registrar_venta(
        self,
        identificacion_usuario,
        codigo_producto,
        cantidad=1
    ):

        if not identificacion_usuario:
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if not codigo_producto:
            raise ValueError(
                "Debe seleccionar un producto."
            )

        if cantidad < 1:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = self.buscar_producto(
            codigo_producto
        )

        if producto is None:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        if producto.stock < cantidad:
            raise ValueError(
                f"Stock insuficiente. Disponible: "
                f"{producto.stock}."
            )

        # Reducir stock
        producto.stock -= cantidad

        # Calcular total
        total = producto.precio * cantidad

        # Obtener fecha y hora
        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Crear objeto Venta
        venta = Venta(
            identificacion_usuario=usuario.identificacion,
            codigo_producto=producto.codigo,
            fecha=fecha,
            cantidad=cantidad,
            total=total
        )

        # Agregar la venta a la colección
        self.ventas.append(venta)

        # Guardar cambios
        try:

            self.guardar_productos()
            self.guardar_ventas()

        except Exception:

            # Si ocurre un error al guardar,
            # devolvemos el stock a su estado anterior.
            producto.stock += cantidad

            if venta in self.ventas:
                self.ventas.remove(venta)

            raise

        return venta

    # =====================================================
    # OBTENER NOMBRE DEL USUARIO
    # =====================================================

    def obtener_nombre_usuario(self, identificacion):

        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario:
            return usuario.nombre

        return "Usuario desconocido"

    # =====================================================
    # OBTENER NOMBRE DEL PRODUCTO
    # =====================================================

    def obtener_nombre_producto(self, codigo):

        producto = self.buscar_producto(
            codigo
        )

        if producto:
            return producto.nombre

        return "Producto desconocido"