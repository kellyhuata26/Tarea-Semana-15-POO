import tkinter as tk
from tkinter import ttk, messagebox


class LoginView(tk.Frame):

    def __init__(
        self,
        parent,
        servicio,
        al_iniciar_sesion
    ):
        super().__init__(
            parent,
            bg="#F4F7FB"
        )

        self.servicio = servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = tk.Frame(
            self,
            bg="white",
            padx=45,
            pady=35,
            highlightthickness=1,
            highlightbackground="#D9E2EC"
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            contenedor,
            text="🍽",
            font=("Arial", 42),
            bg="white"
        ).pack(pady=(0, 5))

        tk.Label(
            contenedor,
            text="Restaurante App",
            font=("Arial", 22, "bold"),
            fg="#173F5F",
            bg="white"
        ).pack()

        tk.Label(
            contenedor,
            text="Sistema de gestión de restaurante",
            font=("Arial", 10),
            fg="#6B7280",
            bg="white"
        ).pack(
            pady=(3, 25)
        )

        tk.Label(
            contenedor,
            text="Usuario",
            font=("Arial", 10, "bold"),
            fg="#374151",
            bg="white"
        ).pack(anchor="w")

        self.entrada_usuario = ttk.Entry(
            contenedor,
            width=34
        )

        self.entrada_usuario.pack(
            pady=(5, 15)
        )

        tk.Label(
            contenedor,
            text="Contraseña",
            font=("Arial", 10, "bold"),
            fg="#374151",
            bg="white"
        ).pack(anchor="w")

        self.entrada_password = ttk.Entry(
            contenedor,
            width=34,
            show="*"
        )

        self.entrada_password.pack(
            pady=(5, 20)
        )

        self.boton_ingresar = ttk.Button(
            contenedor,
            text="Ingresar",
            command=self.iniciar_sesion
        )

        self.boton_ingresar.pack(
            fill="x"
        )

        tk.Label(
            contenedor,
            text="Usuario: kelly  |  Contraseña: 1234",
            font=("Arial", 8),
            fg="#6B7280",
            bg="white"
        ).pack(
            pady=(15, 0)
        )

        self.entrada_usuario.focus()

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get().strip()
        password = self.entrada_password.get()

        if not usuario or not password:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        try:

            persona = self.servicio.validar_login(
                usuario,
                password
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

            return

        if persona is None:

            messagebox.showerror(
                "Acceso denegado",
                "El usuario o la contraseña son incorrectos."
            )

            return

        self.al_iniciar_sesion(persona)