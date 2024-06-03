import json

from dotenv import load_dotenv
import os
from googlesearch import GoogleSearch

# Cargar las variables de entorno desde el archivo .env para garantizar la seguridad y configurabilidad.
load_dotenv()

# Obtener las claves de configuración desde las variables de entorno.
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

# Definir la consulta de búsqueda que será usada para encontrar información específica en Google.
# https://www.exploit-db.com/google-hacking-database
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'

# Crear una instancia de GoogleSearch con la API y el ID del motor de búsqueda proporcionados.
gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)

# Realizar la búsqueda con la consulta definida, especificando el número de páginas a recuperar.
resultados = gsearch.search(query, pages=2)

# Imprimir los resultados obtenidos de la búsqueda.
print(json.dump(resultados, fp=open("resultados_dork_mysql_dump.json", "w"), indent=4))

print("file saved in results_dork_mysql_dump.json")
