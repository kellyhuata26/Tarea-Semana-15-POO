class Usuario:
    def __init__(self, identificacion, nombre, usuario, password):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.password = password

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["usuario"],
            datos["password"]
        )

    def a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }