# Restaurante App - Semana 16

## Descripción del proyecto

**Restaurante App** es una aplicación de escritorio desarrollada en Python para la gestión básica de un restaurante.

El proyecto se ha desarrollado progresivamente durante las semanas anteriores de la asignatura de **Programación Orientada a Objetos**, manteniendo una arquitectura modular y utilizando archivos JSON para almacenar la información.

En la **Semana 15** se incorporan los fundamentos básicos del **manejo de eventos** mediante una interfaz gráfica desarrollada con **Tkinter**.

La principal operación implementada en esta semana es el registro de una venta, relacionando un usuario existente con un producto existente.

---

## Objetivo de la Semana 16

El objetivo principal de esta semana es comprender cómo una acción realizada por el usuario en una interfaz gráfica puede generar una respuesta dentro del sistema.

Para ello se implementa un botón **"Registrar venta"** utilizando el parámetro `command=` de Tkinter y un método callback.

El flujo principal de la aplicación es:

```text
Usuario
   ↓
Selecciona un usuario
   ↓
Selecciona un producto
   ↓
Presiona "Registrar venta"
   ↓
command=
   ↓
Callback registrar_venta()
   ↓
RestauranteServicio
   ↓
Validación de la operación
   ↓
Registro de la venta
   ↓
Persistencia en ventas.json
   ↓
Actualización de la interfaz
   ↓
Respuesta visual al usuario
 Funcionalidades incorporadas en la Semana 15

En esta versión se incorporaron las siguientes funcionalidades:

Se agregó la sección Ventas en la interfaz.
Se implementó el modelo Venta.
Se agregó el archivo ventas.json.
Se permite seleccionar un usuario registrado.
Se permite seleccionar un producto registrado.
Se agregó el botón Registrar venta.
Se utilizó command= para asociar el botón con un callback.
Se implementó el callback registrar_venta().
La interfaz delega la operación al RestauranteServicio.
Se validan el usuario y el producto seleccionados.
Se verifica que exista stock disponible.
Se descuenta el producto vendido del stock.
Se calcula el total de la venta.
Se registra la fecha y hora de la operación.
La venta se almacena en ventas.json.
Las ventas registradas se muestran en una tabla Treeview.
La información de la tabla se actualiza después de registrar una venta.
Las ventas permanecen almacenadas después de cerrar y volver a ejecutar la aplicación.
Se mantienen separados los datos, modelos, servicios e interfaz gráfica.
Se incorporan recursos visuales mediante la carpeta assets/.
 Arquitectura del proyecto

El proyecto mantiene una separación de responsabilidades entre los diferentes componentes del sistema.

├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── usuario.py
│   │   └── venta.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   ├── assets/              
│   └── main.py
└── README.md

Contiene los archivos JSON utilizados para almacenar la información del sistema.

usuarios.json

Almacena los usuarios registrados en la aplicación.

productos.json

Almacena los productos disponibles, incluyendo:

Código
Nombre
Precio
Stock
ventas.json

Almacena las ventas registradas en el sistema.

Cada venta contiene información relacionada con:

Identificación del usuario
Código del producto
Fecha y hora
Cantidad
Total
  modelos/

Contiene las clases que representan las entidades principales del restaurante.

usuario.py

Contiene la clase Usuario, utilizada para representar a los usuarios del sistema.

producto.py

Contiene la clase Producto, utilizada para representar los productos disponibles.

venta.py

Contiene la clase Venta, utilizada para representar una operación de venta y relacionar un usuario con un producto.

  servicios/

Contiene la lógica relacionada con el funcionamiento del sistema y la persistencia de los datos.

archivo_servicio.py

Se encarga de leer y guardar la información en los archivos JSON.

Permite trabajar con:

usuarios.json
productos.json
ventas.json

La interfaz gráfica no accede directamente a estos archivos.

restaurante_servicio.py

Contiene las operaciones y reglas principales del restaurante.

Entre sus responsabilidades se encuentran:

Validar el inicio de sesión.
Obtener usuarios.
Obtener productos.
Obtener ventas.
Buscar usuarios.
Buscar productos.
Registrar ventas.
Validar la disponibilidad del producto.
Descontar el stock.
Calcular el total.
Guardar las ventas.
Guardar los cambios del stock.
Interfaz gráfica

La interfaz gráfica se encuentra dentro de la carpeta ui/.

login_view.py

Contiene la pantalla de inicio de sesión.

Permite ingresar:

Usuario
Contraseña

La validación del inicio de sesión se realiza mediante RestauranteServicio.

main_view.py

Contiene la interfaz principal de la aplicación.

Desde esta ventana se puede acceder a:

Inicio
Usuarios
Productos
Ventas

También contiene la operación principal trabajada en la Semana 15:

Registrar venta.

  Manejo de eventos

Uno de los principales objetivos de la Semana 15 es comprender el funcionamiento de los eventos en una interfaz gráfica.

Para registrar una venta se utiliza un botón asociado mediante command=:

self.boton_venta = ttk.Button(
    formulario,
    text="Registrar venta",
    command=self.registrar_venta
)

Es importante observar que se utiliza:

command=self.registrar_venta

y no:

command=self.registrar_venta()

El primer caso permite que Tkinter ejecute el método cuando el usuario presiona el botón.

  Callback de la venta

El método:

registrar_venta()

funciona como callback.

El callback obtiene las selecciones realizadas por el usuario en la interfaz y posteriormente solicita al servicio que realice la operación.

El flujo es:

Botón
   ↓
command=self.registrar_venta
   ↓
registrar_venta()
   ↓
Obtiene usuario seleccionado
   ↓
Obtiene producto seleccionado
   ↓
RestauranteServicio.registrar_venta()
   ↓
Validaciones
   ↓
Guardar información
   ↓
Actualizar Treeview
   ↓
Mostrar mensaje al usuario

De esta manera, la interfaz se encarga de coordinar la interacción, mientras que la lógica de negocio permanece en RestauranteServicio.

  Registro de una venta

Para registrar una venta el usuario debe:

Iniciar sesión.
Ingresar a la sección Ventas.
Seleccionar un usuario.
Seleccionar un producto.
Presionar el botón Registrar venta.

El sistema realiza las siguientes comprobaciones:

Que se haya seleccionado un usuario.
Que se haya seleccionado un producto.
Que el usuario exista.
Que el producto exista.
Que la cantidad sea válida.
Que exista stock suficiente.

Si las validaciones son correctas:

Se crea la venta.
Se calcula el total.
Se registra la fecha y hora.
Se descuenta una unidad del stock.
Se guarda la información en ventas.json.
Se actualiza la tabla de ventas.
Se muestra un mensaje confirmando la operación.
  Persistencia de información

La aplicación utiliza archivos JSON para conservar la información.

Los principales archivos son:

usuarios.json
productos.json
ventas.json

La persistencia permite que las ventas no se pierdan cuando se cierra la aplicación.

Al volver a ejecutar main.py, el sistema carga nuevamente la información almacenada en los archivos JSON.

  Recursos visuales

La aplicación utiliza la carpeta:

assets/

para organizar los recursos visuales del sistema.

Dentro de ella se encuentran:

assets/
├── iconos/
│   ├── productos.png
│   ├── usuarios.png
│   └── ventas.png
│
└── logo/
    ├── restaurante_logo.png
    └── restaurante_logo.svg

Estos recursos se utilizan para mantener una interfaz organizada y coherente con la identidad visual del sistema.

  Instalación y ejecución
Requisitos

Para ejecutar el proyecto se necesita:

Python 3
Tkinter
Visual Studio Code u otro editor compatible con Python

Las librerías utilizadas corresponden principalmente a módulos incluidos en Python.

Ejecutar la aplicación

Primero se debe ingresar a la carpeta:

restaurante_app

Luego abrir una terminal y ejecutar:

python main.py

En sistemas donde sea necesario utilizar py, se puede ejecutar:

py main.py Usuario de prueba

Para comprobar el funcionamiento de la aplicación se puede utilizar:

Usuario: kelly
Contraseña: 1234
  Comprobación del funcionamiento

Para comprobar la funcionalidad de la Semana 15 se puede realizar la siguiente prueba:

1. Inicio de la aplicación

Ejecutar:

python main.py
2. Inicio de sesión

Ingresar:

Usuario: kelly
Contraseña: 1234
3. Navegación

Comprobar las secciones:

Inicio
Usuarios
Productos
Ventas
4. Registrar una venta

Ingresar a:

Ventas

Seleccionar:

Usuario
Producto

y presionar:

Registrar venta
5. Comprobar la respuesta

La venta debe aparecer inmediatamente en la tabla de ventas.

6. Comprobar la persistencia

Revisar el archivo:

datos/ventas.json

La nueva venta debe encontrarse almacenada allí.

7. Comprobar nuevamente

Cerrar la aplicación y ejecutar otra vez:

python main.py

La venta anteriormente registrada debe continuar apareciendo en la sección Ventas.

  Conceptos de Programación Orientada a Objetos utilizados

El proyecto aplica diferentes conceptos de Programación Orientada a Objetos, entre ellos:

Clases.
Objetos.
Métodos.
Constructores.
Encapsulamiento de responsabilidades.
Separación entre modelos, servicios e interfaz.
Creación de objetos a partir de información almacenada en JSON.

Además, en esta semana se incorpora el concepto de manejo de eventos mediante callbacks asociados a componentes de Tkinter.

  Alcance de la Semana 15

Esta versión se concentra en los fundamentos básicos del manejo de eventos.

No se implementan funcionalidades correspondientes a temas posteriores, como:

bind()
Eventos de teclado.
Eventos de mouse.
Doble clic.
TreeviewSelect.
Carrito de compras.
Facturación.
Base de datos.
Inventario avanzado.
  Autora

Kelly Daniela  Tanguila Huatatoca

Asignatura: Programación Orientada a Objetos

Semana: 15

Proyecto: Restaurante App

Tecnología principal: Python + Tkinter

Persistencia: Archivos JSON

  Conclusión

La Semana 15 permitió incorporar los fundamentos básicos del manejo de eventos al proyecto restaurante_app.

La operación de registro de ventas demuestra cómo una acción realizada por el usuario puede iniciar un evento mediante command=, ejecutar un callback, delegar la operación a RestauranteServicio, almacenar la información en ventas.json y finalmente actualizar la interfaz para mostrar el resultado.

De esta manera, se mantiene una separación clara entre la interfaz gráfica, los modelos, los servicios y la persistencia de información.
