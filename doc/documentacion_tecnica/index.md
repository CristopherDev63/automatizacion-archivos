# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

## Proceso general
```mermaid 
graph TD 
    %% Definicion de estilos 
    classDef proceso fill:#84B179,stroke:black,stroke-width:2px, color: black
    classDef decision fill:#A2CB8B,stroke:black,stroke-width:2px, color: black
    classDef archivo fill:#C7EABB,stroke:black,stroke-width:2px, color: black
    classDef movimiento fill:#E8F5BD,stroke:black,stroke-width:2px, color: black
    classDef verificacion fill:#F8F3E1,stroke:#black,stroke-width:2px, color black

    Start([Inicio]) --> Config[Cargar el archivo de configuración]:::proceso
    Config --> Tarea_leer_config[Tarea: Leer la configuración y cargarlo]:::proceso
    Tarea_leer_config --> Desicion_orden_contrato{¿Todos los parametros estan llenos y correctos?}:::decision
    Desicion_orden_contrato --> |no| mensaje_error[Arroja un error y detiene el proceso]:::proceso
```
