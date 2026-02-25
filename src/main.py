from pydantic import BaseModel, field_validator, model_validator 
from pathlib import Path
from typing import Callable, Any, List, Optional, Dict
import time
from tareas import cargar_configuracion, definir_carpetas

class proceso:
    """
    Nodo individual de un Pipeline con soporte para Navegación de Atributos (Smart-Context).
    """

    def __init__(self, funcion: Callable, nombre_funcion: str, *args, **kwargs) -> None:
        self.funcion = funcion
        self.args = args
        self.kwargs = kwargs
        self.puntero: Optional['proceso'] = None 
        self.resultado: Any = None
        self.nombre_funcion = nombre_funcion
        self.tiempo_ejecucion: float = 0.0
        self.exitoso: bool = False
    
    def _resolver_referencia(self, referencia: str, contexto: Dict[str, Any]) -> Any:
        """
        Resuelve referencias complejas como 'Proceso.atributo.metodo'.
        """
        partes = referencia.split(".")
        nombre_proceso = partes[0]
        objeto = contexto.get(nombre_proceso)

        # Navegamos por los atributos/métodos (ej: Config.ruta_destino)
        for atributo in partes[1:]:
            if objeto is None:
                return None
            
            if hasattr(objeto, atributo):
                valor = getattr(objeto, atributo)
                # Si es un método (como .dict() o .json()), lo ejecutamos automáticamente
                objeto = valor() if callable(valor) else valor
            else:
                return None
        
        return objeto

    def ejecutar(self, contexto: Dict[str, Any], ultimo_resultado: Any = None) -> Any:
        """
        Ejecuta la función resolviendo dependencias de contexto y atributos.
        """
        inicio = time.time()
        
        args_procesados = []
        for arg in self.args:
            if isinstance(arg, str) and arg.startswith("ctx:"):
                referencia = arg.replace("ctx:", "")
                args_procesados.append(self._resolver_referencia(referencia, contexto))
            else:
                args_procesados.append(arg)

        try:
            if args_procesados:
                self.resultado = self.funcion(*args_procesados, **self.kwargs)
            elif ultimo_resultado is not None:
                self.resultado = self.funcion(ultimo_resultado, **self.kwargs)
            else:
                self.resultado = self.funcion(**self.kwargs)
            
            self.exitoso = True
        except Exception as e:
            self.resultado = f"Error en {self.nombre_funcion}: {str(e)}"
            self.exitoso = False
        finally:
            self.tiempo_ejecucion = time.time() - inicio
        
        return self.resultado


class PipeLines:
    """
    Gestor de procesos con Almacén de Estados y Navegación de Atributos.
    """
    def __init__(self) -> None:
        self.cabeza: Optional[proceso] = None 
        self.resultados_por_nombre: Dict[str, Any] = {}

    def agregar_proceso(self, funcion: Callable, nombre_funcion: str, *args, **kwargs) -> None:
        nuevo_proceso = proceso(funcion, nombre_funcion, *args, **kwargs)
        if self.cabeza is None:
            self.cabeza = nuevo_proceso
            return
        actual = self.cabeza
        while actual.puntero:
            actual = actual.puntero
        actual.puntero = nuevo_proceso

    def ejecutar_todos(self) -> Dict[str, Any]:
        actual = self.cabeza 
        ultimo_res = None

        print(f"\n{'='*20} Iniciando Pipeline {'='*20}")
        while actual:
            print(f"[*] Ejecutando: {actual.nombre_funcion}...")
            ultimo_res = actual.ejecutar(self.resultados_por_nombre, ultimo_res)
            self.resultados_por_nombre[actual.nombre_funcion] = ultimo_res
            
            status = "✓" if actual.exitoso else "✗"
            print(f"[{status}] Finalizado en {actual.tiempo_ejecucion:.4f}s")
            actual = actual.puntero
        
        print(f"{'='*20} Pipeline Finalizado {'='*20}\n")
        return self.resultados_por_nombre

    def obtener_resumen(self) -> None:
        actual = self.cabeza
        print(f"{'Proceso':<25} | {'Estado':<10} | {'Resultado (Resumen)':<20}")
        print("-" * 65)
        while actual:
            estado = "OK" if actual.exitoso else "ERROR"
            res_str = str(actual.resultado)[:20] + "..." if len(str(actual.resultado)) > 20 else str(actual.resultado)
            print(f"{actual.nombre_funcion:<25} | {estado:<10} | {res_str:<20}")
            actual = actual.puntero


if __name__ == "__main__":
    RUTA_CONFIG = Path("./config.yaml")
    pipeline = PipeLines()

    # 1. Cargamos configuración (Retorna un objeto FileConfig)
    pipeline.agregar_proceso(cargar_configuracion, "Config Inicial", RUTA_CONFIG)
    
    # 2. Función que SOLO necesita un string (la ruta), no todo el objeto
    def verificar_ruta(ruta: str):
        return f"Verificando acceso a: {ruta}"

    # USANDO LA NUEVA FUNCIONALIDAD: Accedemos directamente a .ruta_destino del resultado anterior
    pipeline.agregar_proceso(definir_carpetas, "Definir las carpetas", "ctx:Config Inicial.archivos")

    # Ejecución
    pipeline.ejecutar_todos()
    pipeline.obtener_resumen()
