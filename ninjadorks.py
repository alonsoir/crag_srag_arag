import json

from googlesearch import GoogleSearch
from dotenv import load_dotenv, set_key
import os
import argparse
import sys

""""
    This version has problems with parameters...
"""
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


def main(query, configure_env=None, start_page=1, pages=1, lang="lang_es"):
    # Verificar la existencia del archivo .env
    if configure_env or not os.path.exists(".env"):
        env_config()
        sys.exit(1)
    # Cargar las variables de entorno desde el archivo .env para garantizar la seguridad y configurabilidad.
    load_dotenv()
    print(f"Dork: query")

    # Obtener las claves de configuración desde las variables de entorno.
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    # Definir la consulta de búsqueda que será usada para encontrar información específica en Google.
    # https://www.exploit-db.com/google-hacking-database
    # query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
    print(f"query is {query}")
    # Crear una instancia de GoogleSearch con la API y el ID del motor de búsqueda proporcionados.
    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)

    # Realizar la búsqueda con la consulta definida, especificando el número de páginas a recuperar.
    resultados = gsearch.search(query, pages=2)
    output_filename = f"{query}-dump.json"
    # Imprimir los resultados obtenidos de la búsqueda.
    #json.dump(resultados, fp=open(f"{output_filename}", "w"), indent=4)
    json.dump(resultados, fp=open("output.txt", "w"), indent=4)

    print(f"file saved in output-ninjadorks.txt")


if __name__ == "__main__":
    """
    Realiza una búsqueda en Google utilizando una API KEY y un SEARCH ENGINE ID almacenados en un archivo .env.

    Args:
        query (str): Consulta de búsqueda que se realizará en Google.
        configure_env (bool, optional): Si es True, se solicita configurar el .env. Defaults to None.
        start_page (int, optional): Página inicial de los resultados de búsqueda. Defaults to 1.
        pages (int, optional): Número de páginas de resultados a retornar. Defaults to 1.
        lang (str, optional): Código de idioma para los resultados de búsqueda. Defaults to 'lang_es'.
    """


    parser = argparse.ArgumentParser(
        description="Herramienta para realizar búsquedas avanzadas en Google de forma automática."
    )
    parser.add_argument(
        "-q",
        "--query",
        type=str,
        help="Especifica el dork que deseas buscar. Ejemplo: -q \"filetype:sql 'MySQL dump' (pass|password|passwd|pwd)\"",
    )
    parser.add_argument(
        "-c",
        "--configure",
        action="store_true",
        help="Configura o actualiza el archivo .env. Utiliza esta opción sin otros argumentos para configurar las claves.",
    )
    parser.add_argument(
        "--start-page",
        type=int,
        default=1,
        help="Página de inicio para los resultados de búsqueda. Por defecto es 1.",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Número de páginas de resultados a retornar. Por defecto es 1.",
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="lang_es",
        help="Código de idioma para los resultados de búsqueda. Por defecto es 'lang_es' (español).",
    )

    args = parser.parse_args()

    main(args)
