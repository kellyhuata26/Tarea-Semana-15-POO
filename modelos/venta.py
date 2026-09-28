class Venta:
    def __init__(
        self,
        identificacion_usuario,
        codigo_producto,
        fecha,
        cantidad=1,
        total=0.0
    ):
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.fecha = fecha
        self.cantidad = int(cantidad)
        self.total = float(total)

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["identificacion_usuario"],
            datos["codigo_producto"],
            datos["fecha"],
            datos.get("cantidad", 1),
            datos.get("total", 0.0)
        )

    def a_diccionario(self):
        return {
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "fecha": self.fecha,
            "cantidad": self.cantidad,
            "total": self.total
        }