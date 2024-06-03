import os
from dotenv import load_dotenv
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from unstructured.chunking.title import chunk_by_title
from unstructured.partition.email import partition_email

load_dotenv()


def simple_output_parser(output):
    return output.strip()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def preprocess_emails(directory):
    elements = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".eml"):
                elems = partition_email(filename=os.path.join(root, file))
                elements.extend(elems)
    return elements


def main():
    print("main...")

    email_elements = preprocess_emails("emails")

    chunked_elements = chunk_by_title(email_elements)

    documents = []
    for element in chunked_elements:
        metadata = element.metadata.to_dict()
        documents.append(Document(page_content=element.text, metadata=metadata))

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embeddings)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = OpenAI(
        model="gpt-3.5-turbo", temperature=0.7, max_tokens=400, stop=["\n", "\n\n"]
    )

    prompt_template = """
    Answer the user's question using the provided context. Stick to the facts, do not draw your own conclusions.
    Question: {question}
    Context: {context}
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    sequential_chain = SimpleSequentialChain(chains=[retriever, llm_chain])

    question = "What can you tell me about Cohere's Command+ models?"

    context_docs = retriever.retrieve(question)
    context = format_docs(context_docs)
    response = llm_chain.predict(context=context, question=question)

    print(response)


if __name__ == "__main__":
    main()
