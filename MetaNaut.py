import os
import sys
import datetime
import openpyxl
import docx
from PIL import Image
from PIL.ExifTags import TAGS

def save_metadata(filename, metadata):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(metadata)

def extract_metadata(ruta_completa, extracted_folder):
    print(f"Extrayendo metadatos de: {ruta_completa}")
    metadata = ""
    if ruta_completa.lower().endswith('.docx'):
        try:
            doc = docx.Document(ruta_completa)
            propiedades = doc.core_properties
            metadata += "Metadatos DOCX:\n"
            metadata += f"  Creador: {propiedades.author}\n"
            metadata += f"  Fecha de creación: {propiedades.created}\n"
            metadata += f"  Último modificador: {propiedades.last_modified_by}\n"
            metadata += f"  Fecha de última modificación: {propiedades.modified}\n"
            metadata += f"  Título: {propiedades.title}\n"
            metadata += f"  Asunto: {propiedades.subject}\n"
            metadata += f"  Categoría: {propiedades.category}\n"
            print("Metadatos extraídos exitosamente.")
        except Exception as e:
            metadata += f"Error al leer DOCX: {e}\n"
    elif ruta_completa.lower().endswith('.xlsx'):
        try:
            wb = openpyxl.load_workbook(ruta_completa)
            propiedades = wb.properties
            metadata += "Metadatos XLSX:\n"
            metadata += f"  Creador: {propiedades.creator}\n"
            metadata += f"  Fecha de creación: {propiedades.created}\n"
            metadata += f"  Último modificador: {propiedades.lastModifiedBy}\n"
            metadata += f"  Fecha de última modificación: {propiedades.modified}\n"
            metadata += f"  Título: {propiedades.title}\n"
            metadata += f"  Asunto: {propiedades.subject}\n"
            metadata += f"  Categoría: {propiedades.category}\n"
            metadata += f"  Palabras clave: {propiedades.keywords}\n"
            metadata += f"  Descripción: {propiedades.description}\n"
            print("Metadatos extraídos exitosamente.")
        except Exception as e:
            metadata += f"Error al leer XLSX: {e}\n"
    elif ruta_completa.lower().endswith('.txt'):
        try:
            tamaño = os.path.getsize(ruta_completa)
            metadata += f"Tamaño del archivo: {tamaño} bytes\n"
            fecha_modificacion = os.path.getmtime(ruta_completa)
            fecha_formateada = datetime.datetime.fromtimestamp(fecha_modificacion).strftime('%Y-%m-%d %H:%M:%S')
            metadata += f"Fecha de última modificación: {fecha_formateada}\n"
            print("Metadatos extraídos exitosamente.")
        except Exception as e:
            metadata += f"Error al leer TXT: {e}\n"
    elif ruta_completa.lower().endswith('.jpg'):
        try:
            image = Image.open(ruta_completa)
            exif_data = image._getexif()
            if exif_data:
                metadata += "Metadatos JPG:\n"
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata += f"  {tag_name}: {value}\n"
                print("Metadatos extraídos exitosamente.")
            else:
                metadata += "No se encontraron metadatos EXIF en la imagen.\n"
        except Exception as e:
            metadata += f"Error al leer JPG: {e}\n"
    else:
        metadata += f"Tipo de archivo no soportado: {ruta_completa}\n"

    # Guardar metadatos en archivo .txt
    base_name = os.path.basename(ruta_completa)
    file_name, _ = os.path.splitext(base_name)
    metadata_file = os.path.join(extracted_folder, f"{file_name}.txt")
    save_metadata(metadata_file, metadata)

def main():
    if len(sys.argv) < 2:
        print("Uso: python Metadatter.py [nombre de la carpeta]")
        sys.exit(1)

    carpeta = sys.argv[1]
    if not os.path.exists(carpeta):
        print(f"La carpeta {carpeta} no existe.")
        sys.exit(1)

    extracted_folder = f"Extracted-{carpeta}"
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)
        print(f"Carpeta '{extracted_folder}' creada.")

    for archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, archivo)
        extract_metadata(ruta_completa, extracted_folder)

if __name__ == "__main__":
    main()