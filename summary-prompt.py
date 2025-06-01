from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

information = """
Like-kind exchanges -- when you exchange real property used for business or held as an investment solely for other business or investment property that is the same type or “like-kind” -- have long been permitted under the Internal Revenue Code. Generally, if you make a like-kind exchange, you are not required to recognize a gain or loss under Internal Revenue Code Section 1031. If, as part of the exchange, you also receive other (not like-kind) property or money, you must recognize a gain to the extent of the other property and money received. You can’t recognize a loss.

Under the Tax Cuts and Jobs Act, Section 1031 now applies only to exchanges of real property and not to exchanges of personal or intangible property. An exchange of real property held primarily for sale still does not qualify as a like-kind exchange. A transition rule in the new law provides that Section 1031 applies to a qualifying exchange of personal or intangible property if the taxpayer disposed of the exchanged property on or before December 31, 2017, or received replacement property on or before that date. 

Thus, effective January 1, 2018, exchanges of machinery, equipment, vehicles, artwork, collectibles, patents and other intellectual property and intangible business assets generally do not qualify for non-recognition of gain or loss as like-kind exchanges. However, certain exchanges of mutual ditch, reservoir or irrigation stock are still eligible for non-recognition of gain or loss as like-kind exchanges.

Like-kind property
Properties are of like-kind if they’re of the same nature or character, even if they differ in grade or quality.

Real properties generally are of like-kind, regardless of whether they’re improved or unimproved. For example, an apartment building would generally be like-kind to another apartment building. However, real property in the United States is not like-kind to real property outside the United States.

Reporting a like-kind exchange
Form 8824, Like-Kind Exchanges, is used to report a like-kind exchange. Form 8824 Instructions provide information on general rules and how to complete the form.
"""

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

    # llm = ChatOpenAI(temperature=0, model="gpt-4o-mini",
    #                  api_key=os.getenv("OPENAI_API_KEY"))

    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm | StrOutputParser
    res = chain.invoke(input={"information": information})

    print(res)

