from errores import ParametrosFaltantesConfiguracion
from errores import ListaVaciaConfiguracionArchivos
from pydantic import BaseModel, model_validator, field_validator
from typing import Any, List

class FileConfig(BaseModel):
    """
    Este es un un contrato de datos para verificar potenciales
    errores dentro de nuestro archivo de configuracion
    """
    ruta_origen: str
    ruta_destino: str 
    crear_carpeta_archivos_organizados: bool
    archivos: list[str]
    lista_de_archivos_prohibidos: List[str]

    @model_validator(mode="before")
    @classmethod
    def verificar_campos(cls, data: Any) -> Any:
        """
        Esta funcinion sirve para verificar que nuestros campos existan
        """
        campos_contrato = cls.model_fields.keys()   # Usamos Estos para acceder a nuestros variables o metodos de la clase 

        for campo in campos_contrato:
            if campo not in data or data[campo] is None:
                raise ParametrosFaltantesConfiguracion(campo)

        return data
    
    @field_validator("archivos", mode="before")
    @classmethod
    def verificar_lista_vacia(cls, v: Any) -> Any:
        """
        Esta función sirve para verificar que nuestra lista de archivos no este vacia
        """
        if not v:
            raise ListaVaciaConfiguracionArchivos()

        return v
