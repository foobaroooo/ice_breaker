import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# this 3 lines fixes ModuleNotFoundError: No module named 'tools'
# TODO - investigate why this is needed. Maybe a PYTHONPATH issue?
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )

    # prompt template with a clear "outpout indicator"
    template = """Give the full name of a person {person_name} I want to find out the URL to their Twitter/X profile page. 
    Extract the user name.    Your answer should only include Twitter username"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["person_name"]
    )

    # description is SUPER important, must be concise and clear to agent
    tools_for_agent = [
        Tool(
            name="Crawl Twitter/X person profile",
            func=get_profile_url_tavily,
            description="Get the username to the Twitter profile page to a person by their full name",
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
    twitter_username = lookup(name="Richard Chen twitter")
