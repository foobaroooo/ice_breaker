from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import requests
import os

from third_parties.linkedin import scrap_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_breaker_with(name: str) -> str:

    # get the linkedin profile url
    linkedin_username_url = linkedin_lookup_agent(name=name)

    # scrap the linkedin profile data from the url
    linkedin_data = scrap_linkedin_profile(linkedin_profile_url=linkedin_username_url, mock=True)

    summary_template = """
        giving the information below about a person from LinkedIn, create a summary of their professional background and experience.
        
        {information}
        
        I want to create:
        1. summary of the person's professional background and experience
        2. a short introduction of the person
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # llm = ChatOllama(model="llama3.2")
    
    # chain = summary_prompt_template | llm | StrOutputParser
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()

    print("Hello ICE BREAKER")
    
    ice_breaker_with(name="Andrew Ng - AI Pioneer")