from crewai import Agent
from llm import bedrock_llm

researcher = Agent(
    role="Researcher",
    goal="Research the given topic accurately",
    backstory="Expert at finding concise and factual information.",
    llm=bedrock_llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write a clear and simple explanation",
    backstory="Skilled at converting research into easy language.",
    llm=bedrock_llm,
    verbose=True
)
