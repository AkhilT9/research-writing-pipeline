from crewai import Crew
from agents import researcher, writer
from tasks import research_task, writing_task

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)
