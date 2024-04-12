from dotenv import load_dotenv
from langchain_openai import OpenAI #ESSA LIB ESTÁ FUNCIONANDO APENAS COM O MODELO 3.5 INSTRUCT
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from tools import pre_precess
from langchain_openai import ChatOpenAI # COM ESSA LIB É POSSÍVEL UTILZAR OUTROS TODOS OS MODELOS DA OPENAI
load_dotenv()


def f1(ano, llm):

    prompt = PromptTemplate(
        input_variables=['ano'],
        template="Quem ganhou o campeonato de Formula 1 em {ano}"
    )

    f1_chain = LLMChain(llm = llm, prompt=prompt)

    response = f1_chain({'ano':ano})
    return response

#llm = OpenAI(temperature=0.5, model='gpt-3.5-turbo-instruct') # VERSÃO ATUALIZADA ATÉ SET/21; LIMTTADO A 4K TOKENS DE INPUT
llm = ChatOpenAI(temperature=0.8,model="gpt-3.5-turbo-0125")   # VERSÃO ATUALIZADA ATÉ SET/21; LIMITADO A 16K TOKENS DE INPUT
if __name__ == "__main__":
    pre_precess()
    response = f1(2023, llm)
    print(response['text'])