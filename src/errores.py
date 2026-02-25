from pathlib import Path 

class ErrorArchivoConfiguracionSinEncontrar(Exception):
    """
    Clase para cuando no se encuentre **el archivo de configuracion**.
    """
    def __init__(self, archivo: Path) -> None:
        mensaje = f"No se encontro el archivo de configuracion {archivo}"
        super().__init__(mensaje)

class ParametrosFaltantesConfiguracion(Exception):
    """
    Clase para cuando existen campos que se requieren en la configuracion.
    """
    def __init__(self, campo: str) -> None:
        mensaje = f"No se encontro el campo {campo} en el archivo de configuracion"
        super().__init__(mensaje)

class ListaVaciaConfiguracionArchivos(Exception):
    """
    Clase para cuando nuestra lista de archivos esta vacia.
    """
    def __init__(self) -> None:
        mensaje = f"La lista de archivos de la configuracion esta vacia"
        super().__init__(mensaje)
