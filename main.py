import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Restaurante App - Semana 15")
        self.geometry("1100x700")
        self.minsize(950, 600)
        self.configure(bg="#F4F7FB")

        # Ubicación de la carpeta del proyecto
        self.carpeta_base = Path(__file__).resolve().parent

        # Carpeta donde están los archivos JSON
        self.carpeta_datos = self.carpeta_base / "datos"

        # Crear servicio para manejar los archivos JSON
        self.archivo_servicio = ArchivoServicio(
            self.carpeta_datos
        )

        # Crear servicio principal del restaurante
        self.restaurante_servicio = RestauranteServicio(
            self.archivo_servicio
        )

        # Usuario que inició sesión
        self.usuario_actual = None

        # Mostrar pantalla de inicio de sesión
        self.mostrar_login()

    # =====================================================
    # LIMPIAR LA VENTANA
    # =====================================================

    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()

    # =====================================================
    # MOSTRAR LOGIN
    # =====================================================

    def mostrar_login(self):

        self.limpiar_ventana()

        self.title(
            "Restaurante App - Inicio de sesión"
        )

        login_view = LoginView(
            self,
            self.restaurante_servicio,
            self.iniciar_aplicacion
        )

        login_view.pack(
            fill="both",
            expand=True
        )

    # =====================================================
    # INICIAR APLICACIÓN DESPUÉS DEL LOGIN
    # =====================================================

    def iniciar_aplicacion(self, usuario):

        self.usuario_actual = usuario

        self.limpiar_ventana()

        self.title(
            f"Restaurante App - {usuario.nombre}"
        )

        main_view = MainView(
            self,
            self.restaurante_servicio,
            usuario,
            self.cerrar_sesion
        )

        main_view.pack(
            fill="both",
            expand=True
        )

    # =====================================================
    # CERRAR SESIÓN
    # =====================================================

    def cerrar_sesion(self):

        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar la sesión actual?"
        )

        if confirmar:

            self.usuario_actual = None

            self.mostrar_login()


# =========================================================
# INICIO DEL PROGRAMA
# =========================================================

if __name__ == "__main__":

    aplicacion = Aplicacion()

    aplicacion.mainloop()