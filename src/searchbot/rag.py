from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaLLM
from . import bot
from . import retriever
from . import template


def search(query, bot_name='baidu', lang='chinese', verbose=False, llm=OllamaLLM(model='llama3.1', temperature=0.3)):
    # Set the language template
    if lang == 'chinese':
        prompt_template = template.chinese
    else:
        prompt_template = template.english

    # Create the prompt
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Create the retriever
    search_bot = bot.make_bot(bot_name, verbose=verbose)  # Default to Baidu bot
    r = retriever.SearchBotRetriever(bot=search_bot)

    # Construct the RAG chain
    rag_chain = (
            {"context": r, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )

    # Invoke the RAG chain with the query
    answer = rag_chain.invoke(query)
    return answer
