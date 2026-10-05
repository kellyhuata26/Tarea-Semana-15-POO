class Usuario:
    def __init__(self, identificacion, nombre, usuario, password, rol="Cliente"):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.rol = rol

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["usuario"],
            datos["password"],
            datos.get("rol", "Cliente")
        )

    def a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password,
            "rol": self.rol
        }
