from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import requests
import os

from third_parties.linkedin import scrap_linkedin_profile

load_dotenv()


if __name__ == "__main__":
    print("Hello foo")

    summary_template = """
        giving the info provided below:
        {information}    
        I want to create:
        1. summary
        2. create a joke
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    llm = ChatOllama(model="llama3.2")

    # chain = summary_prompt_template | llm | StrOutputParser
    chain = summary_prompt_template | llm

    linkedin_data = scrap_linkedin_profile("https://www.linkedin.com/in/michael-huang-006a1017/", True)

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

