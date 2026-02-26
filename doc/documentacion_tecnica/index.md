# Documentación de técnica Automatización de archivos
Bienvenido a la documentación de técnica de Automatización de archivos. En esta documentación orientada para desarrolladores de se explica el proceso de desarrollo de un proyecto de software de manera sencilla y eficiente.

```mermaid
graph LR
    Start([Inicio]) --&gt; Scan[Escanear Carpeta]
    Scan --&gt; Check{¿Hay archivos .tmp?}
    Check -- No --&gt; End([Fin])
    Check -- Sí --&gt; Delete[Borrar Archivos]
    Delete --&gt; Scan
```
