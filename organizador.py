import os
import shutil

# Diccionario para clasificar extensiones en categorías
CATEGORIAS = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Musica": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".wma", ".m4a"],
    "Programas": [".py", ".js", ".java", ".c", ".cpp", ".sh", ".bat", ".exe", ".jar"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "PDFs": [".pdf"],
    
}

def obtener_categoria(extension):
    """Devuelve el nombre de la categoría para una extensión de archivo dada."""
    for categoria, extensiones in CATEGORIAS.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros"

def organizar_carpeta(ruta_carpeta):
    """Organiza todos los archivos en la carpeta especificada según su tipo."""
    try:
        archivos = os.listdir(ruta_carpeta)
    except FileNotFoundError:
        print("La ruta ingresada no existe. Verificá e intentá de nuevo.")
        return
    except PermissionError:
        print("No tenés permisos para acceder a esa carpeta.")
        return

    for nombre_archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        # Saltar subdirectorios
        if os.path.isdir(ruta_archivo):
            continue
        _, extension = os.path.splitext(nombre_archivo)
        if not extension:
            categoria = "Sin extension"
        else:
            categoria = obtener_categoria(extension)

        nueva_carpeta = os.path.join(ruta_carpeta, categoria)
        if not os.path.exists(nueva_carpeta):
            try:
                os.makedirs(nueva_carpeta)
            except Exception as e:
                print(f"No se pudo crear la carpeta {nueva_carpeta}: {e}")
                continue

        destino = os.path.join(nueva_carpeta, nombre_archivo)
        try:
            shutil.move(ruta_archivo, destino)
            print(f"Movido: {nombre_archivo} --> {categoria}/")
        except Exception as e:
            print(f"Error al mover {nombre_archivo}: {e}")

def main():
    print("=== Organizador automático de archivos ===")
    ruta = input("Ingresá la ruta absoluta de la carpeta a organizar:\n> ").strip()

    if not os.path.isabs(ruta):
        print("Por favor, ingresá una ruta absoluta válida.")
        return

    if not os.path.exists(ruta):
        print("La ruta ingresada no existe. Verificá e intentá de nuevo.")
        return

    organizar_carpeta(ruta)
    print("Organización terminada.")

if __name__ == "__main__":
    main()