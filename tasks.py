from crewai import Task
from agents import researcher, writer

research_task = Task(
    description="Research the topic: {topic}",
    expected_output="Accurate research summary of the topic",
    agent=researcher
)

writing_task = Task(
    description="Explain the topic {topic} in simple words using the research",
    expected_output="Simple and clear explanation of the topic",
    agent=writer
)
