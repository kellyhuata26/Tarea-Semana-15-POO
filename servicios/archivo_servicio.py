import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, carpeta_datos):
        self.carpeta_datos = Path(carpeta_datos)
        self.carpeta_datos.mkdir(parents=True, exist_ok=True)

    def leer(self, nombre_archivo):
        ruta = self.carpeta_datos / nombre_archivo

        if not ruta.exists():
            return []

        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)

            if not isinstance(contenido, list):
                raise ValueError(
                    f"El archivo {nombre_archivo} debe contener una lista."
                )

            return contenido

        except json.JSONDecodeError as error:
            raise ValueError(
                f"El archivo {nombre_archivo} contiene JSON inválido."
            ) from error

    def guardar(self, nombre_archivo, datos):
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with ruta.open("w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError as error:
            raise PermissionError(
                f"No hay permisos para escribir en {ruta}."
            ) from error