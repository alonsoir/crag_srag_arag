import os
import shutil
import subprocess

import os


def procesar_dorks(carpeta_destino):
    dorks_dict = {}

    # Recorrer todos los archivos en la carpeta destino
    for root, dirs, files in os.walk(carpeta_destino):
        for file in files:
            if file.endswith(".txt"):
                categoria = os.path.splitext(file)[0]
                ruta_archivo = os.path.join(root, file)

                # Leer las líneas del archivo
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    dorks = [linea.strip() for linea in f.readlines() if linea.strip()]

                # Agregar la categoría y sus dorks al diccionario
                if categoria in dorks_dict:
                    dorks_dict[categoria].extend(dorks)
                else:
                    dorks_dict[categoria] = dorks

    return dorks_dict






def clonar_y_copiar_txts(repo_url, carpeta_destino):
    # Nombre temporal para clonar el repositorio
    nombre_temp = "repositorio_temp"

    # Clonar el repositorio
    subprocess.run(["git", "clone", repo_url, nombre_temp], check=True)

    # Crear la carpeta destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Recorrer el repositorio clonado y copiar los archivos .txt
    for root, dirs, files in os.walk(nombre_temp):
        for file in files:
            if file.endswith(".txt"):
                ruta_archivo = os.path.join(root, file)
                shutil.copy(ruta_archivo, carpeta_destino)
                print(f"Copiado: {file}")

    # Eliminar el repositorio temporal clonado
    shutil.rmtree(nombre_temp)


# URL del repositorio y carpeta destino
repo_url = "https://github.com/HackShiv/OneDorkForAll.git"
carpeta_destino = "./txt_files"

# Llamar a la función para clonar el repositorio y copiar los archivos
clonar_y_copiar_txts(repo_url, carpeta_destino)

# Procesar los archivos y obtener el diccionario de dorks
dorks_dict = procesar_dorks(carpeta_destino)

# Mostrar el diccionario resultante (opcional)
for categoria, dorks in dorks_dict.items():
    print(f"Categoría: {categoria}, Número de dorks: {len(dorks)}")
