# Proyecto de Gestión de Licencias Médicas

Este proyecto es un sistema completo para el control y gestión de licencias, desarrollado en HTML, JavaScript y Python. Utiliza una base de datos en phpMyAdmin (XAMPP) y está diseñado para incluir funcionalidades de login y registro, así como una base de datos para almacenar información sobre las licencias.

## Características
- **Login y Registro**: Sistema de autenticación de usuarios.
- **Gestión de Licencias**: Creación, edición, y eliminación de licencias.
- **Base de Datos**: Integración con phpMyAdmin para almacenamiento de datos.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

### Librerías de Python

1. Flask
2. mysql-connector-python
3. Werkzeug

- XAMPP instalado y configurado.
- Python 3.x.
- Navegador web moderno.

## Instalación
1. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate   # En Windows
   ```

2. Instala las dependencias:
   ```bash
   pip install flask mysql-connector-python werkzeug
   ```

3. Clona este repositorio en tu máquina local.
4. Configura la base de datos en phpMyAdmin utilizando el archivo `database.sql`.

### Base de Datos

1. Asegúrate de tener MySQL instalado y configurado.
2. Crea la base de datos y las tablas ejecutando el archivo `database.sql`:
   ```bash
   mysql -u root -p < database.sql
   ```

### Ejecución

1. Inicia la aplicación:
   ```bash
   python app.py
   ```
2. Accede a la aplicación en tu navegador en `http://127.0.0.1:5001`.

### Notas

- Asegúrate de configurar correctamente las credenciales de la base de datos en el archivo `app.py` si es necesario.
- Si encuentras algún problema, verifica que todas las dependencias estén instaladas correctamente.

## Uso
1. Accede al sistema a través de tu navegador web.
2. Regístrate o inicia sesión para comenzar a gestionar licencias.