# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

## Proceso general
```mermaid 
    %% Definicion de estilos 
    classDef proceso fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef archivo fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef movimiento fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef verificacion fill:#ffebee,stroke:#b71c1c,stroke-width:2px


graph TD 
    Start([Inicio]) --> Config[Cargar el archivo de configuración]:::proceso
    Config --> Tarea_leer_config[Tarea: Leer la configuración y cargarlo]:::proceso
    Tarea_leer_config --> Desicion_orden_contrato{¿Todos los parametros estan llenos y correctos?}:::decision
    Desicion_orden_contrato --> |no| mensaje_error[Arroja un error y detiene el proceso]:::proceso
```
