
# Advanced RAG control flow with LangGraph🦜🕸:

### Implementation of Reflective RAG, Self-RAG & Adaptive RAG tailored towards developers and production-oriented 
applications for learning LangGraph🦜🕸️, with Quix capability to ingest urls from a kafka topic using a consumer.

### Added a sample of a neo4j client to insert data into a neo4j database, local and remote.
The remote neo4j interacts with Chat-GPT-4 model to generate a response to the user.

This repository contains a refactored version of the original [LangChain's Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain),

See Original YouTube video:[Advance RAG control flow with Mistral and LangChain](https://www.youtube.com/watch?v=sgnrL7yo1TE)

of [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain

![Logo](https://github.com/emarco177/langgaph-course/blob/main/static/langgraph_adaptive_rag.png)

Alonso Isidoro Román (@alonso_isidoro):

### Added Quix support

Added Quix capability to ingest urls from a kafka topic using a consumer. 
Added Quix capability to insert urls to a kafka topic using a producer. 

I simply read from a csv file to produce urls into the topic, just to simulate the real process.
In real life, quix_producer should a web crawler looking for relevant data and publishing it to a kafka topic.

### Added Google Dorks with Python
Be sure to create a.env file with the following variables:

SEARCH_ENGINE_ID=

API_KEY_GOOGLE=
  ```bash
    poetry run python ninjadorks.py
  ```
### Added gpt4all samples
  ```bash
    poetry run python gpt3all_sample.py
    run next commands in another terminal:
    brew install mitmproxy
    mitmproxy --mode reverse:http://localhost:4891 --listen-host 127.0.0.1 --listen-port 8080
    echo "run next command in another terminal:"
    poetry run python gpt3all_sample_local_server.py
  ```
  First sample will download the model from the internet, the second sample will use the model from the local folder.
  Download the model from the internet using gpt4all, in my case i downloaded Mistral-7B-Instruct-v0.1.Q4_0.GGUF and then
  started the local server in port 4891. 8080 port is being used by mitmproxy.

### Added NinjaDorks samples. Kudos to Santiago Hernandez for the original code. @santiagohramos
  ```bash
  cd dorks
  poetry run python ninjadorks.py -q "filetype:sql MySQL dump (pass|password|passwd|pwd)" --download all --html resultados.html
  poetry run python ninjadorks.py -gd "filetype:sql MySQL dump (pass|password|passwd|pwd)" 
    Tratando de generar dorks con esta consulta: filetype:sql MySQL dump (pass|password|passwd|pwd)
    ¿Quieres utilizar GPT-4 de OpenAI? (yes/no): yes
    Utilizando OpenAI en remoto.
    
    Resultado:
     Google Dork: filetype:sql "MySQL dump" "pass" | "password" | "passwd" | "pwd"
     
  poetry run python ninjadorks.py -gd "filetype:sql MySQL dump (pass|password|passwd|pwd)"  
    Tratando de generar dorks con esta consulta: filetype:sql MySQL dump (pass|password|passwd|pwd)
    ¿Quieres utilizar GPT-4 de OpenAI? (yes/no): no
    Utilizando GPT4All y ejecutando la generación en local. Puede tardar varios minutos...
    
    Resultado:
      Google Dork: filetype:sql "MySQL" after:2023-01-01
    
    Para crear un Google Dork específico, necesita conocer los operadores avanzados en motores de búsqueda disponibles 
    y saber utilizarlos para encontrar información específica. Además, también necesita tener una gran memoria y 
    conocimientos en programación avanzada para generar un Google Dork efectivo.
    
Now i can update the dorks dictionary from a git repo.

(crag-srag-arag-py3.12) ┌<▪> ~/g/crag_srag_arag 
└➤ poetry run python dorks/ninjadorks.py --random_dork --force_update
created dork categories dictionary from some_dorks.txt
Clonando el repositorio https://github.com/HackShiv/OneDorkForAll.git en repositorio_temp
Cloning into 'repositorio_temp'...
remote: Enumerating objects: 90, done.
remote: Counting objects: 100% (90/90), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 90 (delta 52), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (90/90), 10.13 MiB | 1.87 MiB/s, done.
Resolving deltas: 100% (52/52), done.
There are 81 categories in the dictionary.
Selected dork: Wifi Passwords: from category: All Shodan dork
Buscando dorks con esta consulta: Wifi Passwords:
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ #  ┃ Titulo                                                              ┃ Descripcion                                                              ┃ Enlace                                                                    ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ How to view and change your WiFi network name and password ...      │ Xfinity app · Log in to the Xfinity app (download on the App Store or    │ https://es.xfinity.com/support/articles/view-change-wifi-password         │
│    │                                                                     │ Google Play). · Select the WiFi tab. · Select WiFi details. · On the     │                                                                           │
│    │                                                                     │ pop-up, select Edit ...                                                  │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 2  │ Find or Change Your WiFi Network Name & Password | Spectrum ...     │ Find or Change Your WiFi Network Name & Password · Sign in with your     │ https://www.spectrum.net/es/support/internet/finding-your-charter-wifi-n… │
│    │                                                                     │ Spectrum username and password. · Select Services, then select Internet. │                                                                           │
│    │                                                                     │ · Your WiFi info ...                                                     │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 3  │ Windows 10 keeps forgetting wi-fi credentials - Microsoft Community │ Jul 24, 2021 ... ... password and observe your device if its still       │ https://answers.microsoft.com/en-us/windows/forum/all/windows-10-keeps-f… │
│    │                                                                     │ forget the wifi credentials. If issue persist, let's download the        │                                                                           │
│    │                                                                     │ updated driver. What is the ...                                          │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 4  │ WiFi Passwords Map Instabridge - Aplicaciones en Google Play        │ Con millones de puntos de acceso WiFi seguros y actualizados,            │ https://play.google.com/store/apps/details?id=com.instabridge.android&hl… │
│    │                                                                     │ Instabridge es la forma más sencilla de navegar de forma gratuita. El    │                                                                           │
│    │                                                                     │ buscador sabe qué redes Wi- ...                                          │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 5  │ The Wifi Password in Spanish - Memrise lesson                       │ ¡espera! wait!; hang on! puedes. you can (singular informal). ir. to go. │ https://www.memrise.com/en-us/learn-spanish/spanish-course/1/basics/5568… │
│    │                                                                     │                                                                          │                                                                           │
│ 6  │ Quick Installation Guide                                            │ Enjoy! Both extended networks share the same Wi-Fi passwords as those of │ https://static.tp-link.com/res/down/doc/RE200(US)_V1_QIG.pdf              │
│    │                                                                     │ your ... Fill in the WiFi Password of your Main Router/AP: Range         │                                                                           │
│    │                                                                     │ Extender Network ...                                                     │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 7  │ Computer Login Guide - Updated                                      │ Note: Wi-Fi name (SSID) and Wi-Fi Password are located on the label      │ https://www.clevelandmetroschools.org/cms/lib/OH01915844/Centricity/Doma… │
│    │                                                                     │ inside the back cover of the device. • From a Windows computer:          │                                                                           │
│    │                                                                     │ Left-click Wireless ...                                                  │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 8  │ Locations San Salvador, San Salvador city, El Salvador - WiFi Space │ Download free WiFi passwords map ; Casa de Huéspedes El Rinconcito.      │ https://wifispc.com/locations/el-salvador/san-salvador/                   │
│    │                                                                     │ Alameda Juan Pablo II, San Salvador, El Salvador ; Equipo Maiz. Pasaje   │                                                                           │
│    │                                                                     │ Decapolis ; Zona Rosa.                                                   │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 9  │ How do i reset the Wifi-Password of the Black Hero 3 Plus Black ... │ Press the mode button until the "Reset Cam" option appears. Press the    │ https://community.gopro.com/s/question/0D53b000097NX1hCAG/how-do-i-reset… │
│    │                                                                     │ shutter button to select "Reset Cam." Press the mode button until "Yes"  │                                                                           │
│    │                                                                     │ appears. Press the ...                                                   │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
│ 10 │ Change Your WiFi Name and Password                                  │ Changing your WiFi password. 1. On the Adapt screen, tap New Home        │ https://espanol.centurylink.com/home/help/internet/fiber/premium-wifi/ch… │
│    │                                                                     │ Password under your current network info. 2. On the next screen, enter a │                                                                           │
│    │                                                                     │ new WiFi password. 3.                                                    │                                                                           │
│    │                                                                     │                                                                          │                                                                           │
└────┴─────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────┴───────────────────────────────────────────────────────────────────────────┘  ```

(crag-srag-arag-py3.12) ┌<▸> ~/g/crag_srag_arag 
└➤ poetry run python dorks/ninjadorks.py --random_dork 
created dork categories dictionary from some_dorks.txt
There are 81 categories in the dictionary.
Selected dork: inurl:wp-content/plugins/ from category: WordPress
Buscando dorks con esta consulta: inurl:wp-content/plugins/
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ #  ┃ Titulo                                                               ┃ Descripcion                                                              ┃ Enlace                                                                   ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ Index of /wp-content/plugins/jetpack/extensions/blocks/podcast ...   │ Index of                                                                 │ http://www.abae.gob.ve/wp-content/plugins/jetpack/extensions/blocks/pod… │
│    │                                                                      │ /wp-content/plugins/jetpack/extensions/blocks/podcast-player/templates.  │                                                                          │
│    │                                                                      │ [ICO], Name · Last modified · Size · Description. [PARENTDIR] ...        │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 2  │ Index of /wp-content/plugins/form-maker/images/demo                  │ Index of /wp-content/plugins/form-maker/images/demo. Name · Last         │ http://ofinase.go.cr/wp-content/plugins/form-maker/images/demo/          │
│    │                                                                      │ modified · Size · Description · Parent Directory, -. 1.png, 2021-02-16   │                                                                          │
│    │                                                                      │ 16:00, 1.3K.                                                             │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 3  │ Index of /wp-content/plugins/jetpack/jetpack_vendor/automattic ...   │ Name · Last modified · Size · Description. [PARENTDIR], Parent           │ http://www.abae.gob.ve/wp-content/plugins/jetpack/jetpack_vendor/automa… │
│    │                                                                      │ Directory, -. [ ], class-boost-api.php, 2024-06-05 21:18, 2.6K.          │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 4  │ Index of /wp-content/plugins/elementskit/modules/parallax/assets/css │ Index of /wp-content/plugins/elementskit/modules/parallax/assets/css.    │ https://www.bancofarmaceutico.es/wp-content/plugins/elementskit/modules… │
│    │                                                                      │ Icon Name Last modified Size Description. [PARENTDIR] Parent Directory - │                                                                          │
│    │                                                                      │ [TXT] ...                                                                │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 5  │ Index of /wp-content/plugins/jetpack/jetpack_vendor/automattic ...   │ 5 days ago ... Index of                                                  │ http://www.abae.gob.ve/wp-content/plugins/jetpack/jetpack_vendor/automa… │
│    │                                                                      │ /wp-content/plugins/jetpack/jetpack_vendor/automattic/jetpack-videopres… │                                                                          │
│    │                                                                      │ ...                                                                      │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 6  │ Index of /wp-content/plugins/elementskit/widgets/interactive-links   │ Index of /wp-content/plugins/elementskit/widgets/interactive-links. Name │ https://www.unaq.edu.mx/wp-content/plugins/elementskit/widgets/interact… │
│    │                                                                      │ · Last modified · Size · Description · Parent Directory, -.              │                                                                          │
│    │                                                                      │ interactive-links-ha.                                                    │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 7  │ Index of /wp-content/plugins/jetpack/jetpack_vendor/automattic ...   │ Name · Last modified · Size · Description. [PARENTDIR], Parent           │ http://www.abae.gob.ve/wp-content/plugins/jetpack/jetpack_vendor/automa… │
│    │                                                                      │ Directory, -. [ ], class-checkout-flow.php, 2024-06-05 21:18, 5.5K. [ ], │                                                                          │
│    │                                                                      │ class-my-account.php ...                                                 │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 8  │ Index of /wp-content/plugins/elementor/core/frontend/render-modes    │ 4 days ago ... Index of                                                  │ https://www.isaayahotelboutique.mx/wp-content/plugins/elementor/core/fr… │
│    │                                                                      │ /wp-content/plugins/elementor/core/frontend/render-modes. Name · Last    │                                                                          │
│    │                                                                      │ modified · Size · Description · Parent Directory, -.                     │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 9  │ Index of /portalnv/wp-content/plugins/wp-miniaudioplayer/js          │ Name · Last modified · Size · Description. [PARENTDIR], Parent           │ https://www.munimacul.cl/portalnv/wp-content/plugins/wp-miniaudioplayer… │
│    │                                                                      │ Directory, -. [ ], id3.min.js, 2023-09-28 11:00, 16K. [ ],               │                                                                          │
│    │                                                                      │ jquery.jplayer.swf, 2023-09-28 11: ...                                   │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
│ 10 │ Index of /wp-content/plugins/elementor/assets/lib/font-awesome/fonts │ Name · Last modified · Size · Description · Parent Directory, -.         │ https://www.isaayahotelboutique.mx/wp-content/plugins/elementor/assets/… │
│    │                                                                      │ FontAwesome.otf, 2024-06-06 12:53, 132K. fontawesome-webfont.eot,        │                                                                          │
│    │                                                                      │ 2024-06-06 12:53, 162K.                                                  │                                                                          │
│    │                                                                      │                                                                          │                                                                          │
└────┴──────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────┘

## Features

- **Refactored Notebooks**: The original LangChain notebooks have been refactored to enhance readability, maintainability,
- and usability for developers.
- **Production-Oriented**: The codebase is designed with a focus on production readiness, allowing developers to seamlessly 
- transition from experimentation to deployment.
- **Test Coverage**: Comprehensive test coverage ensures the reliability and stability of the application, 
- enabling developers to validate their implementations effectively.
- **Documentation**: Detailed documentation and branches guides developers through setting up the environment, 
- understanding the codebase, and utilizing LangGraph effectively.
- **Real time ingestion: The code use quix to ingest urls from kafka**
- **Interaction with NEO4j**: The code insert data into a neo4j database, local and remote, and then interact with
  Chat-GPT-4 model to generate a response to the user. Local version dont interact with the model, only the remote one.
- Create an account in the neo4j cloud and create a new project. (https://console.neo4j.io/)
- Download your neo4j instance into your machine. (https://neo4j.com/download/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/crag_srag_arag`

`OPENAI_API_KEY`

`TAVILY_API_KEY`

`QUIX_SDK_TOKEN`

`remote_neo4j_password`

`remote_neo4j_url`

`remote_neo4j_username`

## QUIX TOPIC

You have to create in the quix cloud or change auto_create_topics in App declaration.

input-topic = urls-from-csv
output = urls-from-csv

## Run Locally

Clone the project

```bash
  git clone https://github.com/alonsoir/crag_srag_arag.git
```

Go to the project directory

```bash
  cd crag_srag_arag
```

Install dependencies

```bash
  poetry install
```

Start the kafka ingest process and main process.

```bash
  poetry run python quix_producer.py
  poetry run python quix_ingestion.py
  poetry run python main.py
```

Run original ingestion and main process.

```bash
  poetry run python ingest.py
  poetry run python main.py
```
```bash

  export remote_neo4j_url=value1
  export remote_neo4j_username=value2
  export remote_neo4j_password=value2
  poetry run python knowledge-graph-rag.py
```
## Running Tests

To run tests, run the following command

```bash
  poetry run pytest . -s -v
```
## Acknowledgements

Original LangChain repository: [LangChain Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain)
By [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain
![Logo](https://github.com/emarco177/langgaph-course/blob/main/static/LangChain-logo.png)




## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.udemy.com/course/langgraph/?referralCode=FEA50E8CBA24ECD48212)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.udemy.com/user/eden-marco/)


[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alonso-isidoro-roman-8ab57445/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/alonso_Isidoro)

