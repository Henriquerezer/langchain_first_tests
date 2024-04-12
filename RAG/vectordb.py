from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


def url_to_retriever(url):
    loader = WebBaseLoader(url)

    docs = loader.load()


    embeddings = OpenAIEmbeddings()
    text_split = RecursiveCharacterTextSplitter()
    documents = text_split.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    retriever = vector.as_retriever()
    return retriever

retriver = url_to_retriever("https://pt.wikipedia.org/wiki/Campeonato_Mundial_de_F%C3%B3rmula_1_de_2023")
