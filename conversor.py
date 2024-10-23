import json
import pdfplumber
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

# Función para extraer el texto del PDF
def extraer_texto_pdf(archivo_pdf):
    with pdfplumber.open(archivo_pdf) as pdf:
        contenido = []
        for i, pagina in enumerate(pdf.pages):
            texto = pagina.extract_text()
            if texto:
                contenido.append(f"Página {i + 1}:\n{texto}")
    return "\n\n".join(contenido)

# Procesa el texto y estructura la información
def procesar_texto(texto, estructuracion):
    lineas = texto.split('\n')
    if estructuracion == "Por líneas":
        data_estructurada = {
            "contenido": lineas
        }
    elif estructuracion == "Por párrafos":
        parrafos = texto.split("\n\n")
        data_estructurada = {
            "parrafos": parrafos
        }
    else:  # Por páginas
        data_estructurada = {
            "paginas": texto.split("Página")
        }
    return data_estructurada

# Guarda el diccionario en un archivo JSON
def guardar_json(data, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(data, archivo_json, indent=4)

# Función para seleccionar el PDF y mostrar vista previa
def seleccionar_pdf():
    archivo_pdf = filedialog.askopenfilename(
        title="Seleccionar PDF", 
        filetypes=[("PDF Files", "*.pdf")]
    )
    if archivo_pdf:
        try:
            texto_extraido = extraer_texto_pdf(archivo_pdf)
            texto_vista_previa.delete(1.0, tk.END)
            texto_vista_previa.insert(tk.END, texto_extraido[:1000] + "\n...")  # Mostrar los primeros 1000 caracteres
            label_archivo.config(text=f"Archivo seleccionado: {archivo_pdf.split('/')[-1]}")
            boton_convertir.config(state=tk.NORMAL)
            return archivo_pdf
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al procesar el archivo PDF: {e}")

# Función para convertir el PDF a JSON
def convertir_a_json():
    archivo_pdf = label_archivo.cget("text").replace("Archivo seleccionado: ", "")
    if archivo_pdf:
        try:
            texto_extraido = extraer_texto_pdf(archivo_pdf)
            estructuracion = combo_estructuracion.get()
            data_estructurada = procesar_texto(texto_extraido, estructuracion)

            # Selección del directorio de salida
            directorio_salida = filedialog.askdirectory(title="Seleccionar directorio de salida")
            if directorio_salida:
                archivo_json = f"{directorio_salida}/{archivo_pdf.split('/')[-1].replace('.pdf', '.json')}"
                guardar_json(data_estructurada, archivo_json)
                messagebox.showinfo("Éxito", f"Archivo JSON generado con éxito:\n{archivo_json}")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó directorio de salida.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# Crear la ventana principal con estilos profesionales
ventana = tk.Tk()
ventana.title("PDF a JSON - Conversor Profesional")
ventana.geometry("700x500")
ventana.configure(bg="#f7f7f7")

# Agregar un estilo moderno con ttk
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 10), padding=5)
style.configure("TCombobox", font=("Helvetica", 10))

# Encabezado
label_encabezado = ttk.Label(ventana, text="Conversor de PDF a JSON", font=("Helvetica", 18, "bold"), background="#f7f7f7")
label_encabezado.pack(pady=20)

# Crear botón para seleccionar el archivo PDF
boton_seleccionar = ttk.Button(ventana, text="Seleccionar PDF", command=seleccionar_pdf)
boton_seleccionar.pack(pady=10)

# Mostrar el archivo seleccionado
label_archivo = ttk.Label(ventana, text="No se ha seleccionado ningún archivo", background="#f7f7f7")
label_archivo.pack()

# ComboBox para seleccionar cómo estructurar el JSON
label_estructuracion = ttk.Label(ventana, text="Estructurar JSON:", background="#f7f7f7")
label_estructuracion.pack(pady=5)
combo_estructuracion = ttk.Combobox(ventana, values=["Por líneas", "Por párrafos", "Por páginas"])
combo_estructuracion.current(0)  # Selección por defecto
combo_estructuracion.pack()

# Vista previa del contenido del PDF
label_vista_previa = ttk.Label(ventana, text="Vista previa del PDF:", background="#f7f7f7")
label_vista_previa.pack(pady=5)
texto_vista_previa = scrolledtext.ScrolledText(ventana, width=80, height=10, font=("Courier", 10))
texto_vista_previa.pack()

# Botón para convertir el PDF a JSON
boton_convertir = ttk.Button(ventana, text="Convertir a JSON", command=convertir_a_json, state=tk.DISABLED)
boton_convertir.pack(pady=20)

# Pie de página
label_pie = ttk.Label(ventana, text="© 2024 - Conversor Profesional PDF a JSON", background="#f7f7f7", font=("Helvetica", 9))
label_pie.pack(side="bottom", pady=10)

# Ejecutar la aplicación
ventana.mainloop()
