# File Organizer – Organiza tus archivos con Python

Este proyecto es un **organizador automático de archivos** hecho en Python.  
La idea surgió de mi necesidad personal: como artista digital, suelo acumular muchas referencias e imágenes de proyectos en carpetas desordenadas, y necesitaba una forma rápida de **mantener todo organizado por tipo de archivo** (JPG, PNG, PSD, PDF, etc.).

---

##  ¿Qué hace este script?

- Revisa los archivos en una carpeta llamada `downloads/`.  
- Crea subcarpetas automáticamente según la extensión de cada archivo.  
  - Ejemplo:  
    - `imagen.jpg` → `downloads/jpg/imagen.jpg`  
    - `documento.pdf` → `downloads/pdf/documento.pdf`  
    - `archivo_sin_extension` → `downloads/others/archivo_sin_extension`
- Muestra cuántos archivos fueron organizados.  

---

## Ejemplo de uso

**Antes de correr el script:**

downloads/

├── referencia1.jpg

├── boceto.png

├── texto.txt

├── notas.pdf


**Después de correr el script:**

downloads/

├── jpg/

│ └── referencia1.jpg

├── png/

│ └── boceto.png

├── txt/

│ └── texto.txt

├── pdf/

│ └── notas.pdf


**Mensaje en consola:**

Files organized! Number of files moved: 4

**Futuras mejoras/metas:**

- Soporte para organizar también por fecha.

- Interfaz gráfica simple para usuarios no técnicos.

- Configuración para elegir carpeta de destino desde consola.
