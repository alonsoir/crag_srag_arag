import os
import random
import sys
import argparse
from typing import List

from googlesearch import GoogleSearch
from results_parser import ResultsProcessor
from file_downloader import FileDownloader
from ia_agent import OpenAIGenerator, GPT4AllGenerator, IAagent
from dotenv import load_dotenv, set_key
import os
import shutil
import subprocess
import json
import pprint


def clonar_y_copiar_txts(repo_url, carpeta_destino):
    # Nombre temporal para clonar el repositorio
    nombre_temp = "repositorio_temp"
    print(f"Clonando el repositorio {repo_url} en {nombre_temp}")
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
                #print(f"Copiado: {file}")

    # Eliminar el repositorio temporal clonado
    shutil.rmtree(nombre_temp)


def create_json_structure(file_path):
    """
    Crea una estructura JSON a partir de un fichero.txt con la siguiente estructura:
    # Categoría 1
    dork1
    dork2
    ...
    """
    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        json_structure = {}

        for line in lines:
            if line.startswith('#'):
                category = line.strip('#').strip()
                json_structure[category] = []
            else:
                if line:
                    json_structure[category].append(line.strip())

    return json.dumps(json_structure, indent=4)


def env_config():
    """
    Solicita al usuario la API KEY de Google y el ID del buscador personalizado
    y actualiza o crea un archivo .env con estos valores.
    """
    api_key = input("Introduce tu API KEY de Google: ")
    engine_id = input("Introduce el ID del buscador personalizado de Google: ")
    set_key(".env", "API_KEY_GOOGLE", api_key)
    set_key(".env", "SEARCH_ENGINE_ID", engine_id)
    print("Archivo .env configurado satisfactoriamente.")


def openai_config():
    """
    Solicita al usuario su API KEY de OpenAI y guarda este valor en el archivo .env.
    """
    api_key = input("Introduce la API KEY de OpenAI: ")
    set_key(".env", "OPENAI_API_KEY", api_key)
    print("Archivo .env configurado satisfactoriamente.")


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


def parse_txt_to_dict(file_path):
    """
    Crea un diccionario a partir de un fichero.txt con la siguiente estructura:
    # Categoría 1
    dork1
    dork2
    ...
    """
    data_dict = {}
    current_category = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Ignorar líneas vacías

            if line.startswith('#'):
                # Nueva categoría encontrada
                current_category = line[1:].strip()
                data_dict[current_category] = []
            elif current_category:
                # Añadir la línea a la categoría actual
                data_dict[current_category].append(line)
            else:
                print("Error: Línea fuera de categoría")

    return data_dict


def show_dorks(file_path):
    try:
        # Abrir y leer el fichero JSON como una cadena
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Convertir la cadena JSON a un diccionario
        data = json.loads(file_content)

        # Listar las claves del JSON
        if isinstance(data, dict):
            for key in data.keys():
                print(key)
        else:
            print("El contenido del archivo JSON no es un diccionario.")

    except FileNotFoundError:
        print(f"Error: El fichero '{file_path}' no existe.")
    except json.JSONDecodeError as e:
        print(f"Error: El fichero '{file_path}' no contiene un JSON válido. {str(e)}")


def merge_dictionaries(data_dict, dorks_dict):
    """
    Combina los diccionarios data_dict y dorks_dict.
    """
    for categoria, dorks in dorks_dict.items():
        if categoria in data_dict:
            data_dict[categoria].extend(dorks)
        else:
            data_dict[categoria] = dorks
    return data_dict


def main(query, configure_env, start_page, pages, lang, output_json, output_html, download, gen_dork,
         show_categories, show_dorks, random_dork,force_update):
    """
    Realiza una búsqueda en Google utilizando una API KEY y un SEARCH ENGINE ID almacenados en un archivo .env.

    Args:
        query (str): Consulta de búsqueda que se realizará en Google.
        configure_env (bool): Si es True, se solicita configurar el .env. 
        start_page (int): Página inicial de los resultados de búsqueda. 
        pages (int): Número de páginas de resultados a retornar.
        lang (str): Código de idioma para los resultados de búsqueda.
        output_json (str): Ruta del archivo para exportar los resultados en formato JSON.
        output_html (str): Ruta del archivo para exportar los resultados en formato HTML.
        download (str): Cadena con extensiones de archivo para descargar, separadas por comas.
        gen_dork (str): Descripción para generar un dork automáticamente usando IA.
        gen_dictionary (str): Ruta del archivo.txt que contiene los dorks.
        show_categories (str): Ruta del archivo JSON para mostrar las categorías de los dorks.
        show_dorks (str): Ruta del archivo JSON para mostrar los dorks.
        random_dork (str): Ruta del archivo JSON para mostrar un dork aleatorio.
    """
    # Verificar la existencia del archivo .env y configuración del entorno
    global merge_dict
    if configure_env or not os.path.exists(".env"):
        env_config()
        sys.exit(1)

    # Cargar las variables de entorno
    load_dotenv()

    # Extraer valores de las variables de entorno
    google_api_key = os.getenv("API_KEY_GOOGLE")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")


        # Verificar si se ha solicitado generar un dork
    merge_dict = generate_dorks_dictionary("some_dorks.txt", force_update)

    if show_categories:
        print(f"Showing dork categories")
        for key in merge_dict.keys():
            print(f"category: {key}")

    if show_dorks:
        print(f"Showing dorks...")
        for key in merge_dict.keys():
            print(f"category: {key}")
            for dork in merge_dict[key]:
                print(f"dork: {dork}")

    if random_dork:
        # Seleccionar una categoría al azar
        category = random.choice(list(merge_dict.keys()))

        # Seleccionar un dork al azar de la categoría seleccionada
        query = random.choice(merge_dict[category])
        print(f"Selected dork: {query} from category: {category}")

    # Si se solicita generar un dork utilizando inteligencia artificial
    if gen_dork:
        print(f"Tratando de generar dorks con esta consulta: {gen_dork}")
        # Solicitar confirmación para usar OpenAI
        respuesta = ""
        while respuesta.lower() not in ("y", "yes", "n", "no"):
            respuesta = input("¿Quieres utilizar GPT-4 de OpenAI? (yes/no): ")

        if respuesta.lower() in ("y", "yes"):
            # Configurar OpenAI si no está ya configurado
            if "OPENAI_API_KEY" not in os.environ:
                openai_config()
                load_dotenv()  # Recargar variables de entorno
            print("Utilizando OpenAI en remoto.")
            openai_gen = OpenAIGenerator()
            ia_agent = IAagent(openai_gen)
        else:
            # Utilizar una generación local si el usuario prefiere no usar OpenAI
            print("Utilizando GPT4All y ejecutando la generación en local. Puede tardar varios minutos...")
            gpt4all_generator = GPT4AllGenerator()
            ia_agent = IAagent(gpt4all_generator)

        # Generar y mostrar el dork
        respuesta = ia_agent.generate_gdork(gen_dork)
        print(f"\nResultado:\n {respuesta}")
        sys.exit(1)  # Finaliza después de generar el dork

    # Verificar la disponibilidad de las claves de API
    if not google_api_key or not search_engine_id:
        print(
            "ERROR: Falta la API_KEY o el SEARCH_ENGINE_ID. Por favor, ejecuta la opción --configure para configurar el archivo .env.")
        sys.exit(1)

    if query:
        print(f"Buscando dorks con esta consulta: {query}")
    # Verificar la presencia de una consulta
    if not query:
        print("Indica una consulta con el comando -q. Utiliza el comando -h para mostrar la ayuda.")
        sys.exit(1)

    # Realizar la búsqueda en Google
    gsearch = GoogleSearch(google_api_key, search_engine_id)
    resultados = gsearch.search(query, start_page=start_page, pages=pages, lang=lang)

    rparser = ResultsProcessor(resultados)

    # Mostrar los resultados en la línea de comandos
    rparser.mostrar_pantalla()

    # Exportar resultados en formato HTML si se especifica
    if output_html:
        rparser.exportar_html(output_html)

    # Exportar resultados en formato JSON si se especifica
    if output_json:
        rparser.exportar_json(output_json)

    # Descarga los documentos especificados que se encuentren en los resultados
    if download:
        file_types = download.split(",")
        urls = [resultado['link'] for resultado in resultados]
        fdownloader = FileDownloader("Descargas")
        fdownloader.filtrar_descargar_archivos(urls, file_types)


def carpeta_tiene_archivos(carpeta):
    # Listar el contenido de la carpeta
    contenido = os.listdir(carpeta)
    # Filtrar solo archivos
    archivos = [archivo for archivo in contenido if os.path.isfile(os.path.join(carpeta, archivo))]
    # Retornar True si hay archivos, False en caso contrario
    return len(archivos) > 0


def generate_dorks_dictionary(gen_dictionary, force_update=False):
    global merge_dict
    data_dict = parse_txt_to_dict(gen_dictionary)
    print(f"created dork categories dictionary from {gen_dictionary}")
    # URL del repositorio y carpeta destino
    repo_url = "https://github.com/HackShiv/OneDorkForAll.git"
    carpeta_destino = "./txt_files"
    if not carpeta_tiene_archivos(carpeta_destino) or force_update == True:
        # Llamar a la función para clonar el repositorio y copiar los archivos
        clonar_y_copiar_txts(repo_url, carpeta_destino)
    # Procesar los archivos y obtener el diccionario de dorks
    dorks_dict = procesar_dorks(carpeta_destino)
    # Mergear los diccionarios
    merge_dict = merge_dictionaries(data_dict, dorks_dict)
    print(f"There are {len(merge_dict.items())} categories in the dictionary.")
    return merge_dict
    # Mostrar el diccionario fusionado
    # for categoria, dorks in data_dict.items():
    #    print(f"Categoría: {categoria}, Dorks: {dorks}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Esta herramienta permite realizar Hacking con buscadores de manera automática.")
    parser.add_argument("-q", "--query", type=str, help="Especifica el dork que deseas buscar.")
    parser.add_argument("-c", "--configure", action="store_true",
                        help="Inicia el proceso para configurar o actualizar el archivo .env.")
    parser.add_argument("--start-page", type=int, default=1,
                        help="Define la página de inicio del buscador para obtener los resultados.")
    parser.add_argument("--pages", type=int, default=1, help="Número de páginas de resultados a retornar.")
    parser.add_argument("--lang", type=str, default="lang_es", help="Código de idioma para los resultados de búsqueda.")
    parser.add_argument("--json", type=str, default=None,
                        help="Exporta los resultados en formato JSON en el fichero especificado.")
    parser.add_argument("--html", type=str, default=None,
                        help="Exporta los resultados en formato HTML en el fichero especificado.")
    parser.add_argument("--download", type=str, default=None, help="Especifica las extensiones de archivo a descargar.")
    parser.add_argument("-gd", "--generate-dork", type=str, default=None,
                        help="Genera un dork automáticamente a partir de una descripción utilizando IA.")
    parser.add_argument("--dictionary", type=str, default=None,
                        help="Genera el diccionario de dorks a partir de un fichero de texto y de un repositorio de GitHub.")
    parser.add_argument("--show-categories", action="store_true", help="Muestra las categorías de los dorks.")
    parser.add_argument("--show_dorks", action="store_true", help="Muestra los dorks almacenados.")
    parser.add_argument("--random_dork", action="store_true", help="Selecciona un dork al azar.")
    parser.add_argument("--force_update", default=False, type=bool, help="Selecciona un dork al azar.")

    args = parser.parse_args()

    main(query=args.query,
         configure_env=args.configure,
         start_page=args.start_page,
         pages=args.pages,
         lang=args.lang,
         output_json=args.json,
         output_html=args.html,
         download=args.download,
         gen_dork=args.generate_dork,
         show_categories=args.show_categories,
         show_dorks=args.show_dorks,
         random_dork=args.random_dork,
         force_update=args.force_update)
