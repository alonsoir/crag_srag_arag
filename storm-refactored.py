import getpass
import os

from dotenv import load_dotenv
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain as as_runnable
from langchain_openai import ChatOpenAI

from storm import Perspectives, RelatedSubjects, Outline

load_dotenv()


def _set_env(var: str):
    if os.environ.get(var):
        return
    os.environ[var] = getpass.getpass(var + ":")


def format_doc(doc, max_length=1000):
    related = "- ".join(doc.metadata["categories"])
    return f"### {doc.metadata['title']}\n\nSummary: {doc.page_content}\n\nRelated\n{related}"[
        :max_length
    ]


def format_docs(docs):
    return "\n\n".join(format_doc(doc) for doc in docs)





def main():

    # Set for tracing
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "STORM"

    fast_llm = ChatOpenAI(model="gpt-3.5-turbo")
    # Uncomment for a Fireworks model
    # fast_llm = ChatFireworks(model="accounts/fireworks/models/firefunction-v1", max_tokens=32_000)
    long_context_llm = ChatOpenAI(model="gpt-4-turbo-preview")

    direct_gen_outline_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a Wikipedia writer. Write an outline for a Wikipedia page about a user-provided topic. Be comprehensive and specific.",
            ),
            ("user", "{topic}"),
        ]
    )

    generate_outline_direct = (
        direct_gen_outline_prompt | fast_llm.with_structured_output(Outline)
    )

    example_topic = "Impact of million-plus token context window language models on RAG"

    initial_outline = generate_outline_direct.invoke({"topic": example_topic})

    print(initial_outline.as_str)

    gen_related_topics_prompt = ChatPromptTemplate.from_template(
        """I'm writing a Wikipedia page for a topic mentioned below. Please identify and recommend some Wikipedia pages on closely related subjects. I'm looking for examples that provide insights into interesting aspects commonly associated with this topic, or examples that help me understand the typical content and structure included in Wikipedia pages for similar topics.
    
    Please list the as many subjects and urls as you can.
    
    Topic of interest: {topic}
    """
    )

    expand_chain = gen_related_topics_prompt | fast_llm.with_structured_output(
        RelatedSubjects
    )

    related_subjects = expand_chain.ainvoke({"topic": example_topic})
    print(related_subjects)

    gen_perspectives_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You need to select a diverse (and distinct) group of Wikipedia editors who will work together to create a comprehensive article on the topic. Each of them represents a different perspective, role, or affiliation related to this topic.\
        You can use other Wikipedia pages of related topics for inspiration. For each editor, add a description of what they will focus on.
    
        Wiki page outlines of related topics for inspiration:
        {examples}""",
            ),
            ("user", "Topic of interest: {topic}"),
        ]
    )

    gen_perspectives_chain = gen_perspectives_prompt | ChatOpenAI(
        model="gpt-3.5-turbo"
    ).with_structured_output(Perspectives)

    wikipedia_retriever = WikipediaRetriever(
        load_all_available_meta=True, top_k_results=1
    )

    @as_runnable
    async def survey_subjects(topic: str):
        related_subjects = await expand_chain.ainvoke({"topic": topic})
        retrieved_docs = await wikipedia_retriever.abatch(related_subjects.topics, return_exceptions=True)

        all_docs = []
        for docs in retrieved_docs:
            if isinstance(docs, BaseException):
                continue
            all_docs.extend(docs)
        formatted = format_docs(all_docs)
        return await gen_perspectives_chain.ainvoke({"examples": formatted, "topic": topic})

        perspectives = await survey_subjects.ainvoke(example_topic)

        print(perspectives.dict())



if __name__ == "__main__":
    main()
