from crewai import LLM

bedrock_llm = LLM(
    model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    temperature=0.3
)
