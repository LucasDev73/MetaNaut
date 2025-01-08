# MetaNaut

MetaNaut es una herramienta diseñada para extraer metadatos de archivos en una carpeta, incluyendo imágenes, documentos de Word y Excel, PDFs, y más. Genera un archivo de texto individual con el mismo nombre que el archivo original, facilitando así las tareas relacionadas con la ciberseguridad.

## ¿Por qué usar MetaNaut?

- **Análisis Rápido**: Extrae metadatos de múltiples formatos de archivo en un solo paso.
- **Facilita la Ciberseguridad**: Los metadatos pueden revelar información crítica sobre los archivos, ayudando a identificar vulnerabilidades.
- **Organización Eficiente**: Cada archivo de texto generado mantiene la asociación con su archivo original, facilitando su revisión y análisis.

## Instalación

### Requisitos Previos

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Clonar el Repositorio

Para clonar el repositorio en tu máquina local, usa el siguiente comando:

`git clone https://github.com/LucasDev73/MetaNaut.git`

`cd MetaNaut`

### Instalar Dependencias

Asegúrate de estar en la carpeta del proyecto y ejecuta:

`pip install -r requirements.txt`

Esto instalará todas las dependencias necesarias para ejecutar MetaNaut.

## ¿Cómo funciona?

Para ejecutar el script y extraer metadatos de los archivos en una carpeta específica, utiliza el siguiente comando:

`python MetaNaut.py "ruta/a/la/carpeta"`


### Ejemplo

Si tienes una carpeta llamada "documentos" en tu directorio actual, puedes ejecutar:

`python MetaNaut.py documentos `


Esto procesará todos los archivos dentro de la carpeta "documentos" y generará archivos de texto con los metadatos extraídos en una nueva carpeta llamada `Extracted-documentos`.

1. **Selecciona una carpeta**: Elige la carpeta que contiene los archivos de los que deseas extraer metadatos.
2. **Ejecuta MetaNaut**: La herramienta procesará todos los archivos y generará los resultados automáticamente.
3. **Revisa los resultados**: Encuentra todos los metadatos organizados en archivos de texto individuales.

## Contribuciones

Estoy abierto a comentarios y sugerencias para mejorar MetaNaut. Si deseas colaborar o aprender más sobre esta herramienta, no dudes en contactarme.

¡Feliz codificación! 🚀
