import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView(tk.Frame):

    def __init__(
        self,
        parent,
        restaurante_servicio,
        usuario,
        al_cerrar_sesion
    ):
        super().__init__(
            parent,
            bg="#F4F7FB"
        )

        self.parent = parent
        self.restaurante_servicio = restaurante_servicio
        self.usuario = usuario
        self.al_cerrar_sesion = al_cerrar_sesion

        # Cargar logo e iconos
        self.cargar_assets()

        # Crear la interfaz
        self.crear_interfaz()

        # Mostrar Inicio
        self.mostrar_inicio()

    # =========================================================
    # CARGAR IMÁGENES
    # =========================================================

    def cargar_assets(self):

        carpeta_assets = (
            Path(__file__).resolve().parent.parent / "assets"
        )

        # -------------------------
        # LOGO
        # -------------------------

        ruta_logo = (
            carpeta_assets
            / "logo"
            / "restaurante_logo.png"
        )

        self.imagen_logo = None

        if ruta_logo.exists():
            try:
                self.imagen_logo = tk.PhotoImage(
                    file=str(ruta_logo)
                )
            except Exception:
                self.imagen_logo = None

        # -------------------------
        # ICONOS
        # -------------------------

        nombres = {
            "inicio": "inicio.png",
            "usuarios": "usuarios.png",
            "productos": "productos.png",
            "ventas": "ventas.png"
        }

        self.iconos = {}

        for nombre, archivo in nombres.items():

            ruta = (
                carpeta_assets
                / "iconos"
                / archivo
            )

            if ruta.exists():

                try:
                    self.iconos[nombre] = tk.PhotoImage(
                        file=str(ruta)
                    )

                except Exception:
                    self.iconos[nombre] = None

            else:
                self.iconos[nombre] = None

    # =========================================================
    # CREAR INTERFAZ PRINCIPAL
    # =========================================================

    def crear_interfaz(self):

        # =====================================================
        # BARRA SUPERIOR
        # =====================================================

        self.header = tk.Frame(
            self,
            bg="#2C3E50",
            height=55
        )

        self.header.pack(
            side="top",
            fill="x"
        )

        self.header.pack_propagate(False)

        lbl_titulo = tk.Label(
            self.header,
            text=(
                "Restaurante App - Usuario: "
                f"{getattr(self.usuario, 'nombre', 'Usuario')}"
            ),
            fg="white",
            bg="#2C3E50",
            font=("Arial", 13, "bold")
        )

        lbl_titulo.pack(
            side="left",
            padx=20
        )

        btn_salir = tk.Button(
            self.header,
            text="Cerrar Sesión",
            command=self.al_cerrar_sesion,
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        )

        btn_salir.pack(
            side="right",
            padx=20,
            pady=10
        )

        # =====================================================
        # CONTENEDOR PRINCIPAL
        # =====================================================

        self.contenedor_principal = tk.Frame(
            self,
            bg="#F4F7FB"
        )

        self.contenedor_principal.pack(
            side="top",
            fill="both",
            expand=True
        )

        # =====================================================
        # MENÚ LATERAL
        # =====================================================

        self.menu = tk.Frame(
            self.contenedor_principal,
            bg="#173F5F",
            width=210
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(False)

        # -------------------------
        # Logo
        # -------------------------

        if self.imagen_logo is not None:

            lbl_logo = tk.Label(
                self.menu,
                image=self.imagen_logo,
                bg="#173F5F"
            )

            lbl_logo.pack(
                pady=(20, 10)
            )

        else:

            lbl_logo = tk.Label(
                self.menu,
                text="🍽",
                font=("Arial", 35),
                bg="#173F5F",
                fg="white"
            )

            lbl_logo.pack(
                pady=(20, 10)
            )

        # Nombre del sistema

        tk.Label(
            self.menu,
            text="RESTAURANTE",
            font=("Arial", 12, "bold"),
            bg="#173F5F",
            fg="white"
        ).pack(
            pady=(0, 20)
        )

        # =====================================================
        # BOTONES DEL MENÚ
        # =====================================================

        self.crear_boton_menu(
            "Inicio",
            "inicio",
            self.mostrar_inicio
        )

        self.crear_boton_menu(
            "Usuarios",
            "usuarios",
            self.mostrar_usuarios
        )

        self.crear_boton_menu(
            "Productos",
            "productos",
            self.mostrar_productos
        )

        self.crear_boton_menu(
            "Ventas",
            "ventas",
            self.mostrar_ventas
        )

        # =====================================================
        # ÁREA DE CONTENIDO
        # =====================================================

        self.contenido = tk.Frame(
            self.contenedor_principal,
            bg="#F4F7FB"
        )

        self.contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

    # =========================================================
    # CREAR BOTÓN DEL MENÚ
    # =========================================================

    def crear_boton_menu(
        self,
        texto,
        nombre_icono,
        comando
    ):

        boton = tk.Button(
            self.menu,
            text=f"  {texto}",
            command=comando,
            bg="#173F5F",
            fg="white",
            activebackground="#245B7A",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            anchor="w",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=15
        )

        icono = self.iconos.get(nombre_icono)

        if icono is not None:
            boton.configure(
                image=icono,
                compound="left"
            )

        boton.pack(
            fill="x",
            padx=10,
            pady=4,
            ipady=8
        )

    # =========================================================
    # LIMPIAR CONTENIDO
    # =========================================================

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    # =========================================================
    # INICIO
    # =========================================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        # Título

        tk.Label(
            self.contenido,
            text="¡Bienvenido al Sistema del Restaurante!",
            font=("Arial", 22, "bold"),
            bg="#F4F7FB",
            fg="#2C3E50"
        ).pack(
            pady=(45, 10)
        )

        tk.Label(
            self.contenido,
            text="Selecciona una opción del menú para continuar.",
            font=("Arial", 12),
            bg="#F4F7FB",
            fg="#7F8C8D"
        ).pack(
            pady=(0, 35)
        )

        # =====================================================
        # TARJETAS RESUMEN
        # =====================================================

        tarjetas = tk.Frame(
            self.contenido,
            bg="#F4F7FB"
        )

        tarjetas.pack(
            pady=20
        )

        cantidad_usuarios = len(
            self.restaurante_servicio.obtener_usuarios()
        )

        cantidad_productos = len(
            self.restaurante_servicio.obtener_productos()
        )

        cantidad_ventas = len(
            self.restaurante_servicio.obtener_ventas()
        )

        self.crear_tarjeta(
            tarjetas,
            "Usuarios",
            cantidad_usuarios,
            0
        )

        self.crear_tarjeta(
            tarjetas,
            "Productos",
            cantidad_productos,
            1
        )

        self.crear_tarjeta(
            tarjetas,
            "Ventas",
            cantidad_ventas,
            2
        )

    # =========================================================
    # TARJETA
    # =========================================================

    def crear_tarjeta(
        self,
        contenedor,
        titulo,
        valor,
        columna
    ):

        tarjeta = tk.Frame(
            contenedor,
            bg="white",
            width=190,
            height=120,
            highlightthickness=1,
            highlightbackground="#D9E2EC"
        )

        tarjeta.grid(
            row=0,
            column=columna,
            padx=12
        )

        tarjeta.grid_propagate(False)

        tk.Label(
            tarjeta,
            text=titulo,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#6B7280"
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            tarjeta,
            text=str(valor),
            font=("Arial", 25, "bold"),
            bg="white",
            fg="#173F5F"
        ).pack()

    # =========================================================
    # USUARIOS
    # =========================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Usuarios",
            font=("Arial", 20, "bold"),
            bg="#F4F7FB",
            fg="#2C3E50"
        ).pack(
            pady=(30, 20)
        )

        contenedor_tabla = tk.Frame(
            self.contenido,
            bg="white"
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columnas = (
            "identificacion",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "identificacion",
            width=150
        )

        tabla.column(
            "nombre",
            width=220
        )

        tabla.column(
            "usuario",
            width=150
        )

        usuarios = (
            self.restaurante_servicio
            .obtener_usuarios()
        )

        for usuario in usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

        tabla.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

    # =========================================================
    # PRODUCTOS
    # =========================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Productos",
            font=("Arial", 20, "bold"),
            bg="#F4F7FB",
            fg="#2C3E50"
        ).pack(
            pady=(30, 20)
        )

        contenedor_tabla = tk.Frame(
            self.contenido,
            bg="white"
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "stock"
        )

        tabla = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "codigo",
            text="Código"
        )

        tabla.heading(
            "nombre",
            text="Producto"
        )

        tabla.heading(
            "precio",
            text="Precio"
        )

        tabla.heading(
            "stock",
            text="Stock"
        )

        tabla.column(
            "codigo",
            width=100
        )

        tabla.column(
            "nombre",
            width=250
        )

        tabla.column(
            "precio",
            width=120
        )

        tabla.column(
            "stock",
            width=100
        )

        productos = (
            self.restaurante_servicio
            .obtener_productos()
        )

        for producto in productos:

            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

        tabla.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

    # =========================================================
    # VENTAS
    # =========================================================

    def mostrar_ventas(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Registro de Ventas",
            font=("Arial", 20, "bold"),
            bg="#F4F7FB",
            fg="#2C3E50"
        ).pack(
            pady=(25, 15)
        )

        # =====================================================
        # FORMULARIO
        # =====================================================

        formulario = tk.Frame(
            self.contenido,
            bg="white",
            highlightthickness=1,
            highlightbackground="#D9E2EC"
        )

        formulario.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            formulario,
            text="Usuario",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=(18, 5),
            sticky="w"
        )

        tk.Label(
            formulario,
            text="Producto",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=(18, 5),
            sticky="w"
        )

        # =====================================================
        # COMBOBOX USUARIOS
        # =====================================================

        self.usuario_var = tk.StringVar()

        self.combo_usuario = ttk.Combobox(
            formulario,
            textvariable=self.usuario_var,
            state="readonly",
            width=32
        )

        self.combo_usuario.grid(
            row=1,
            column=0,
            padx=15,
            pady=(0, 18)
        )

        usuarios = (
            self.restaurante_servicio
            .obtener_usuarios()
        )

        self.combo_usuario["values"] = [
            f"{usuario.identificacion} - {usuario.nombre}"
            for usuario in usuarios
        ]

        # =====================================================
        # COMBOBOX PRODUCTOS
        # =====================================================

        self.producto_var = tk.StringVar()

        self.combo_producto = ttk.Combobox(
            formulario,
            textvariable=self.producto_var,
            state="readonly",
            width=40
        )

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=15,
            pady=(0, 18)
        )

        self.actualizar_productos_combo()

        # =====================================================
        # BOTÓN REGISTRAR VENTA
        # =====================================================

        self.boton_venta = ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        )

        self.boton_venta.grid(
            row=1,
            column=2,
            padx=15,
            pady=(0, 18)
        )

        # =====================================================
        # TABLA DE VENTAS
        # =====================================================

        tk.Label(
            self.contenido,
            text="Ventas registradas",
            font=("Arial", 14, "bold"),
            bg="#F4F7FB",
            fg="#2C3E50"
        ).pack(
            anchor="w",
            padx=30,
            pady=(15, 5)
        )

        contenedor_tabla = tk.Frame(
            self.contenido,
            bg="white"
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

        columnas = (
            "usuario",
            "producto",
            "fecha",
            "cantidad",
            "total"
        )

        self.tabla_ventas = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla_ventas.heading(
            "total",
            text="Total"
        )

        self.tabla_ventas.column(
            "usuario",
            width=180
        )

        self.tabla_ventas.column(
            "producto",
            width=180
        )

        self.tabla_ventas.column(
            "fecha",
            width=160
        )

        self.tabla_ventas.column(
            "cantidad",
            width=80
        )

        self.tabla_ventas.column(
            "total",
            width=100
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.actualizar_tabla_ventas()

    # =========================================================
    # REGISTRAR VENTA
    # =========================================================

    def registrar_venta(self):

        seleccion_usuario = (
            self.usuario_var.get().strip()
        )

        seleccion_producto = (
            self.producto_var.get().strip()
        )

        if not seleccion_usuario:

            messagebox.showwarning(
                "Usuario requerido",
                "Debe seleccionar un usuario."
            )

            return

        if not seleccion_producto:

            messagebox.showwarning(
                "Producto requerido",
                "Debe seleccionar un producto."
            )

            return

        try:

            identificacion = (
                seleccion_usuario
                .split(" - ")[0]
            )

            codigo_producto = (
                seleccion_producto
                .split(" - ")[0]
            )

            venta = (
                self.restaurante_servicio
                .registrar_venta(
                    identificacion_usuario=identificacion,
                    codigo_producto=codigo_producto,
                    cantidad=1
                )
            )

            # Actualizar tabla de ventas
            self.actualizar_tabla_ventas()

            # Actualizar productos
            self.actualizar_productos_combo()

            messagebox.showinfo(
                "Venta registrada",
                (
                    "La venta fue registrada correctamente.\n\n"
                    f"Producto: {codigo_producto}\n"
                    f"Cantidad: {venta.cantidad}\n"
                    f"Total: ${venta.total:.2f}"
                )
            )

        except ValueError as error:

            messagebox.showwarning(
                "No se pudo registrar la venta",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Ocurrió un error:\n{error}"
            )

    # =========================================================
    # ACTUALIZAR TABLA DE VENTAS
    # =========================================================

    def actualizar_tabla_ventas(self):

        if not hasattr(self, "tabla_ventas"):
            return

        for elemento in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(elemento)

        ventas = (
            self.restaurante_servicio
            .obtener_ventas()
        )

        for venta in ventas:

            nombre_usuario = (
                self.restaurante_servicio
                .obtener_nombre_usuario(
                    venta.identificacion_usuario
                )
            )

            nombre_producto = (
                self.restaurante_servicio
                .obtener_nombre_producto(
                    venta.codigo_producto
                )
            )

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    nombre_usuario,
                    nombre_producto,
                    venta.fecha,
                    venta.cantidad,
                    f"${venta.total:.2f}"
                )
            )

    # =========================================================
    # ACTUALIZAR COMBO DE PRODUCTOS
    # =========================================================

    def actualizar_productos_combo(self):

        if not hasattr(self, "combo_producto"):
            return

        productos = (
            self.restaurante_servicio
            .obtener_productos()
        )

        valores = []

        for producto in productos:

            valores.append(
                (
                    f"{producto.codigo} - "
                    f"{producto.nombre} - "
                    f"${producto.precio:.2f} - "
                    f"Stock: {producto.stock}"
                )
            )

        self.combo_producto["values"] = valores

        # Si había un producto seleccionado,
        # comprobar que todavía existe
        seleccionado = self.producto_var.get()

        if seleccionado:

            codigo = seleccionado.split(" - ")[0]

            existe = any(
                producto.codigo == codigo
                for producto in productos
            )

            if not existe:
                self.producto_var.set("")