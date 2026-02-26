# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

```mermaid
graph TD
    A[Inicio] --> B{¿Decisión?}
    B -->|Sí| C[Acción 1]
    B -->|No| D[Acción 2]
    C --> E[Fin]
    D --> E
```

```mermaid 
graph TD 
    A[Inicio] --> B[Se carga el archivo de configuración]
    B --> |Tarea de proceso de datos| C[Se sacan los archivos de la configuración]
    C --> |Contratos| D[Comprobamos que todos los valores esten en orden]
    D --> |Tarea de sacar las exntesiones y organizarlas dentro de carpetas| E[Se crea plan de traslado de archivos]
    E --> |Tarea de verificación| G[Verificamos que no haya repetidos en le directorio]
    G --> |Tarea de traslado| F[Movemos todos los archivos] 
    F --> H[Fin]
```
