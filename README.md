# aprendizaje_autonomo2_password_generator

Buenas noches Profe, el video de la Explicacion no pude subirlo por el Canvas porque es muy pesado. Aqui le adjunto el link de Google Drive, para que pueda verlo:
https://drive.google.com/drive/folders/1jHg3slqx3xXCwLg5wEV5DjgqpSA2XN0f


# Generador de Contraseñas Seguras

## Objetivo del Sistema
El objetivo de este sistema es proporcionar una herramienta interactiva en entorno de consola orientada a la gestión y creación de credenciales seguras. El programa mitiga los riesgos asociados al uso de claves débiles o predecibles mediante la automatización de contraseñas robustas formadas por caracteres alfanuméricos y símbolos especiales, adaptándose a las necesidades de longitud del usuario.

---

## Descripción de Funcionalidades

El sistema cuenta con un menú interactivo basado en una estructura de control cíclica que permite realizar las siguientes acciones de forma iterativa:

1. Generación Automatizada de Contraseñas (Opción 1):
   - Permite definir una longitud personalizada para la clave.
   - Cuenta con una configuración adaptativa que asigna por defecto una longitud estándar de 12 caracteres si el usuario no especifica una.
   - Aplica validaciones estrictas de longitud mínima (4 caracteres) y máxima (128 caracteres) para cumplir con buenas prácticas de seguridad informática.
   - Utiliza aleatoriedad mediante la librería `random` combinando mayúsculas, minúsculas, números y caracteres especiales.

2. Validación de Ingreso Manual (Opción 2):
   - Permite al usuario auditar o registrar una contraseña de forma manual.
   - El sistema analiza la entrada y calcula la longitud total de caracteres de manera dinámica.
   - Ejecuta las mismas directrices de control (no permite entradas vacías, límites de 4 a 128 caracteres) garantizando la integridad de los datos.

3. Manejo de Errores y Excepciones:
   - Valida que las entradas de longitud correspondan estrictamente a números enteros positivos mediante métodos nativos (`isdigit`).
   - Controla opciones de menú incorrectas sin romper el flujo principal de ejecución del programa.

---

## Información del Proyecto

* **Fecha:** Junio 2026
* **Lenguaje de Programación:** Python 3
* **Tecnologías / Librerías:** `random` (Módulo nativo de Python para la selección pseudoaleatoria)

---

## Cómo Ejecutar el Programa

1. Asegúrate de tener instalado Python en tu entorno local.
2. Clona o descarga el repositorio.
3. Ejecuta el script principal desde tu terminal o consola de comandos:
   ```bash
   python nombre_de_tu_archivo.py
