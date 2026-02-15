from pydantic import BaseModel, field_validator, model_validator 
from pathlib import Path
from typing import Callable, Any
import shutil 
import yaml
import sys


class proceso:
    """
    Nuestro nodo que hiria dentro de nuestro PipeLine.
    """
    def __init__(self, funcion: Callable[[Any | None], Any | None], *args, **kwargs) -> None:
        """ El nodo de proceso.
        Args:
            - funcion (Callable): Nuestra función a agregar
            - args, kwargs: Nuetros argumentos
        """
        self.funcion = funcion
        self.args = args
        self.kwargs = kwargs
        self.puntero = None 
        self.resultado = None


class PipeLines:
    """
    Nuestra lista enlazada de procesos.
    """
    def __init__(self) -> None:
        """
        Definimos nuestra etiqueta `self.cabeza`
        """
        self.cabeza = None 

    def agregar_proceso(self, funcion: Callable[[Any | None], Any | None], *args, **kwargs) -> None:
        """
        Esta es la función que nos deja agregar funciones a la PipeLine.

        Args: Este recibe los mismos parámetros que le nodo o clase `proceso`
        """
        nuevo_proceso = proceso(funcion, *args, **kwargs)

        if self.cabeza is None: # En caso de que no existe ningun elemento apuntando hacía la cabeza.
            self.cabeza = nuevo_proceso
            return
         
        nuevo_proceso.puntero = self.cabeza
        self.cabeza = nuevo_proceso

    def mostrar_procesos(self) -> None:
        """
        Esta es una función "opcional" que nos permite visualizar los elementos de nuestra PipeLine.
        """
        proceso_actual = self.cabeza

        while proceso_actual:   # Nos situamos en la cabeza y hacemos un while antes de que la cebeza llegue a su final (a `None`).
            print(f"[{proceso_actual.funcion.__name__}]")   # Con `__name__` nos permite visualizar el nombre del proceso
            proceso_actual = proceso_actual.puntero

        return 
    
    def ejecutar_procesos(self) -> None:
        """

        """
        proceso_actual = self.cabeza 
        resultados = []

        while proceso_actual:
            resultado = proceso_actual.funcion(*proceso_actual.args, **proceso_actual.kwargs)
            resultados.append(resultado)
            proceso_actual = proceso_actual.puntero

def cargar_configuracion(ruta: Path) -> None:
    datos = {
        "ruta_destino": "./tests/",
        "crear_carpeta_archivos_organizados": True,
        "archivos": ["exe", "txt", "img", "png", "jpg", "doc", "pdf"],
        "lista_de_archivos_prohibidos": ["./tests/script_test.py"]
    }
    try:
        with open(ruta, "r") as a:
            datos_leidos = yaml.safe_load(a)

            return datos_leidos

    except FileNotFoundError:
        print("No se encontro el archivo de configuracion.")
        with open(ruta, "w") as a:
            while True:
                respuesta_archivo = input("¿Desea crear un archivo de configuración el archivo de configuración? [s/n]: ")

                if respuesta_archivo == "s":
                    yaml.dump(datos, a, default_flow_style=False)
                    datos = yaml.safe_load(a)

                    return datos

                elif respuesta_archivo == "n":
                    sys.exit()

                else:
                    print(f"Opcion invalidad: {respuesta_archivo}")


if __name__ == "__main__":
    RUTA_DESTINO = Path("./config.yaml")

    pipeline = PipeLines()

    datos = cargar_configuracion(RUTA_DESTINO)
    if datos is None:
        print("No se pudo cargar la configuración")
        sys.exit(1)
    pipeline.agregar_proceso(lambda: None) # Debes agregar una función válida aquí

    print(datos)
