
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

