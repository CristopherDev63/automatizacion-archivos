# Gestor de Archivos (plantilla)
*La forma fácil y escalable para tener un gestor **automatizado** de archivos dentro de tu computadora*.
El proyecto esta hecho en **Python** en es totalmente escalable y de código libre.

Para ver la documentación completa haga click [aquí](doc/principal.md)

---
## Instalación de las dependencias
### Instalación de los requerimientos
Dentro de tu proyecto tendrás un archivo con el nombre y extensión `requerimientos.txt` y ese archivos nos ayudara a instalar las dependencias de Python.
``` bash
pip install -r requerimientos.txt
```
Activamos nuestro entorno virtual.
```bash
source venv/bin/activate
```

---
## Funciones 
- Tiene archivos de configuración como `config.yaml` para configurar los parámetros del programa
- Cada proceso se registra en un `registros.log` para ver cada proceso con fechas.
- Contiene una lista de procesos escalable (Pipeline para los técnicos).
- Contiene sistemas para detectar fallos dentro **de los archivos de configuración y en la hora de evitar archivos repetidos**.
---



## Correr el proyecto

Ahora poder correr el proyecto, nos tenemos que posicionar dentro del directorio `src/` para ir dentro de nuestros archivos de código y meternos al archivo `main.py`o podemos correrlo desde la terminal.
``` bash
python main.py
```
--- 

