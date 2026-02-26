# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

## Proceso general
```mermaid 
graph TD 

    Start([Inicio]) --> Config[Cargar el archivo de configuración]
    Config --> Tarea_leer_config[Tarea: Leer la configuración y cargarlo]
    Tarea_leer_config --> Desicion_orden_contrato{Contrato: ¿Todos los parametros estan llenos y correctos?}
    Desicion_orden_contrato --> |no| mensaje_error[Arroja un error y detiene el proceso]
    mensaje_error --> Fin([Fin])

    Desicion_orden_contrato --> |si| sacar_configuracion[Sacamos la configuración]
    sacar_configuracion --> generar_plan[Tarea: Generamos el plan de traslado de archivos]
    generar_plan --> Desicion_existencia_archivos{Tarea: ¿Tenemos archivos repetidos?}
    Desicion_existencia_archivos --> |no| proceso_preguntar_usuario{tarea: preguntar al usuario quiere sobreescribir los archivos o crear una copia}
    proceso_preguntar_usuario --> |sobreescribir| sobreescribir_archivo[eliminamos el archivo y lo trasladamos]
    proceso_preguntar_usuario --> |copiar| copiar_archivo[renombramos el archivo con un más numero o le colocamos el texto copia_n] 

```
