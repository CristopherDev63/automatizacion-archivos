from errores import ErrorArchivoConfiguracionSinEncontrar
from errores import ParametrosFaltantesConfiguracion
from errores import ListaVaciaConfiguracionArchivos
from modelos import FileConfig
from pathlib import Path 
import sys, yaml

def cargar_configuracion(ruta: Path) -> FileConfig:
    """
    Esta función sirve para cargar la configuración de un archivo.
    Args:
        - ruta(Path): Este es la ruta de nuestro archivo de configuración.
    Returns:
        - datos(Dict[str, str]): Esta es la configuración leida.
    """
    datos = {
        "ruta_origen": "./tests/",
        "ruta_destino": "./tests/",
        "crear_carpeta_archivos_organizados": True,
        "archivos": ["exe", "txt", "img", "png", "jpg", "doc", "pdf"],
        "lista_de_archivos_prohibidos": ["./tests/script_test.py"]
    }
    try:
        if not ruta.exists():
            raise ErrorArchivoConfiguracionSinEncontrar(ruta)

        with open(ruta, "r") as a:
            datos_leidos = yaml.safe_load(a)
            datos_leidos = FileConfig(**datos_leidos)

            return datos_leidos

    except ErrorArchivoConfiguracionSinEncontrar as e:
        print(e)
        with open(ruta, "w") as a:
            while True:
                respuesta_archivo = input("¿Desea crear un archivo de configuración el archivo de configuración? [s/n]: ")

                if respuesta_archivo == "s":
                    yaml.dump(datos, a, default_flow_style=False)
                    datos_validos = FileConfig(**datos)

                    return datos_validos

                elif respuesta_archivo == "n":
                    sys.exit()

                else:
                    print(f"Opcion invalidad: {respuesta_archivo}")

    except ParametrosFaltantesConfiguracion as e:
        print(e)

    except ListaVaciaConfiguracionArchivos as e:
        print(e)


def definir_carpetas(extensiones: list[str]) -> None:
    categorias = {
        "Documentos": ["sv", "doc", "docx", "pdf", "txt", "xls", "xlsx"],
        "Imagenes": ["jpg", "jpeg", "png", "gif", "bmp"],
        "Videos": ["mp4", "mkv", "avi", "mov", "wmv"],
    }

    for categoria, ext in categorias.items():
        for extension in extensiones:
            if extension in ext:
                print(f"{categoria}: {extension}")

