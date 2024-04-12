from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from vectordb import url_to_retriever
from bot import llm # estou carregando o mesmo llm do arquivo bot.py


prompt = ChatPromptTemplate.from_template(""" Responda a pergunta com base apenas no contexto {context} pergunta: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)
retriver = url_to_retriever("https://pt.wikipedia.org/wiki/Campeonato_Mundial_de_F%C3%B3rmula_1_de_2023")
retriver_chain = create_retrieval_chain(retriver, document_chain)

response = retriver_chain.invoke({"input": "Quem foi o piloto campeão de Formula 1 no ano de 2023"})
print(response['answer'])