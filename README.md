# Sistema de Gestión de Inventario en Python

## Descripción

Este proyecto es un **sistema de gestión de inventario en consola**
desarrollado en Python.\
Permite administrar productos mediante un menú interactivo que facilita
operaciones básicas como:

-   Agregar productos
-   Mostrar inventario
-   Buscar productos
-   Actualizar información
-   Eliminar productos
-   Calcular estadísticas del inventario
-   Guardar datos en archivos CSV
-   Cargar inventario desde archivos CSV

El sistema utiliza **listas, diccionarios, funciones, manejo de archivos
CSV y manejo de errores** para crear una pequeña aplicación funcional de
gestión de datos.

------------------------------------------------------------------------

# Características principales

## Gestión de productos

El programa permite:

-   Añadir productos con **nombre, precio y cantidad**
-   Mostrar todos los productos en formato de tabla
-   Buscar productos por nombre
-   Actualizar precio o cantidad de un producto
-   Eliminar productos del inventario

## Estadísticas automáticas

El sistema calcula automáticamente:

-   Total de unidades en el inventario
-   Valor total del inventario
-   Producto más caro
-   Producto con mayor cantidad en stock

Estas métricas se calculan utilizando **expresiones lambda y funciones
integradas de Python**.

## Persistencia de datos

El sistema puede:

-   Guardar el inventario en un archivo **CSV**
-   Cargar datos desde un **CSV**
-   Validar errores de formato en los archivos

------------------------------------------------------------------------

# Estructura del proyecto

El proyecto está organizado en módulos para mantener el código limpio y
reutilizable.

    project/
    │
    ├── main.py          # Programa principal con el menú interactivo
    ├── functions.py     # Funciones para manipular el inventario
    ├── files.py         # Funciones para guardar y cargar CSV
    └── README.md        # Documentación del proyecto

------------------------------------------------------------------------

# Requisitos

-   Python **3.8 o superior**
-   Librerías estándar de Python:
    -   `csv`

No se requieren librerías externas.

------------------------------------------------------------------------

# Cómo ejecutar el programa

1.  Clona o descarga el proyecto.
2.  Abre una terminal en la carpeta del proyecto.
3.  Ejecuta:

``` bash
python main.py
```

------------------------------------------------------------------------

# Menú del sistema

Al ejecutar el programa aparecerá el siguiente menú:

    SISTEMA DE GESTION DE INVENTARIO

    1. Add Product
    2. Show All
    3. Search
    4. Update
    5. Delete
    6. Statistics
    7. Save to CSV
    8. Load from CSV
    9. Exit

Cada opción permite realizar una acción específica sobre el inventario.

------------------------------------------------------------------------

# Ejemplo de uso

Agregar un producto:

    Seleccione una opcion: 1
    Nombre del producto: Laptop
    Precio: 1200
    Cantidad: 5

Mostrar inventario:

    Nombre                | Precio     | Cantidad
    ---------------------------------------------
    Laptop                | $ 1200.00  | 5

------------------------------------------------------------------------

# Manejo de errores

El programa incluye validación para:

-   Valores negativos
-   Entradas incorrectas del usuario
-   Archivos CSV mal formateados
-   Archivos inexistentes
-   Problemas de escritura o permisos

Esto evita que el programa se cierre inesperadamente.

------------------------------------------------------------------------

# Conceptos de Python utilizados

Este proyecto demuestra el uso de:

-   Funciones
-   Listas y diccionarios
-   Expresiones lambda
-   Generadores
-   Manejo de errores (`try / except`)
-   Lectura y escritura de archivos CSV
-   Organización modular del código

------------------------------------------------------------------------

# Posibles mejoras futuras

Algunas mejoras que se podrían implementar:

-   Interfaz gráfica (Tkinter o PyQt)
-   Base de datos (SQLite o MySQL)
-   Control de usuarios
-   Historial de movimientos de inventario
-   Exportación a Excel

------------------------------------------------------------------------

# Autor

Riwi
**Dylan Gamero**.
