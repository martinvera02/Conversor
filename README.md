# PDF a JSON - Conversor Profesional

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![pdfplumber](https://img.shields.io/badge/pdfplumber-PDF_Processing-green)

## Descripción

**PDF a JSON** es una aplicación de escritorio sencilla pero poderosa que convierte documentos en formato PDF a archivos JSON estructurados. Esta herramienta permite a los usuarios seleccionar un archivo PDF, previsualizar su contenido y exportarlo en formato JSON según diferentes criterios de estructuración: por líneas, párrafos o páginas. 

La aplicación ofrece una interfaz gráfica moderna y fácil de usar, creada con `Tkinter` y `ttk` para una experiencia profesional y fluida.

---

## Características

- **Interfaz gráfica (GUI)** fácil de usar.
- **Conversión de PDFs** a JSON con opciones de estructuración.
- **Vista previa del PDF** antes de la conversión.
- **Selección del directorio de salida** para guardar el archivo JSON generado.
- **Soporte para estructuración personalizada**: 
  - Por líneas
  - Por párrafos
  - Por páginas

---

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas antes de ejecutar la aplicación:

1. **Python 3.8+**: Puedes descargarlo [aquí](https://www.python.org/downloads/).
2. **pdfplumber**: Biblioteca para manejar y extraer texto de PDFs.
   ```bash
   pip install pdfplumber
