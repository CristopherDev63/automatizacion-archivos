# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

## Proceso general
```mermaid 
graph TB
    %% Recursos Externos
    Config_File[(config.yaml<br/>Archivo de Config)]

    subgraph Sistema_Pipeline [Programa de Automatización]
        direction TB
        Main[<b>main.py</b><br/>Clases PipeLines y Proceso]
        Modelos[<b>modelos.py</b><br/>Validación Pydantic]
        Tareas[<b>tareas.py</b><br/>Lógica: cargar_config y definir_carpetas]
        Errores[<b>errores.py</b><br/>Excepciones Personalizadas]
    end

    %% Flujo de ejecución basado en tu código
    Main -->|1. Solicita carga| Tareas
    Tareas -->|2. Lee datos crudos| Config_File
    Tareas -->|3. Instancia y Valida| Modelos
    Modelos -.->|Si falla| Errores
    
    %% La "magia" de tu Smart-Context
    Main -->|4. Inyecta 'ctx:Config Inicial.archivos'| Tareas
```
Después de haber entendido el orden general vamos con le temario.

## temario
- [Arquitectura y Componentes](arquitectura_componentes.md)
- [Guia de Configuración]()
- [Flujo de Ejecución]()
- [Guia Extensibilidad]()
- [Referencia de Errores y Soluciones]()

