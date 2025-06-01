import os
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini"
    )

    # prompt template with a clear "outpout indicator"
    template = """Give the full name of a person {person_name} I want to find out the URL to their LinkedIn profile page. 
    Your answer should only include a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["person_name"]
    )

    # description is SUPER important, must be concise and clear to agent
    tools_for_agent = [
        Tool(
            name="Crawl LinkedIn person profile",
            func=get_profile_url_tavily,
            description="Get the Url to the LinkedIn profile page given a person name"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result=agent_executor.invoke(
        input={"input": prompt_template.format_prompt(person_name=name)}
    )

    linkedin_profile_url=result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Michael Huang")
