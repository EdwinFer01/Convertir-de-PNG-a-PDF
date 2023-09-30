import fitz  # Esta es la biblioteca PyMuPDF

def convertir_pdf_a_png(pdf_path, output_path):
    documento_pdf = fitz.open(pdf_path)  # Abrir el archivo PDF
    for pagina_numero in range(documento_pdf.page_count):
        pagina = documento_pdf[pagina_numero]  # Obtener la página
        imagen = pagina.get_pixmap()  # Obtener una imagen de la página en formato pixmap
        imagen.save(f"{output_path}/pagina_{pagina_numero + 1}.png")  # Guardar la imagen como archivo PNG
    documento_pdf.close()

# Ejemplo de uso
archivo_pdf = input("Ingresa la ruta al archivo pdf: ")  # Reemplaza esto con la ruta de tu archivo PDF
carpeta_salida = input("Ingresa la ruta donde se guardara la imagen: ")  # Reemplaza esto con la carpeta donde quieres guardar las imágenes PNG
convertir_pdf_a_png(archivo_pdf, carpeta_salida)
