import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from dotenv import load_dotenv
import os
load_dotenv()  

from crewai import Crew
from tasks import task1, task2, task3
from agents import explainer, literature_agent, gap_analyzer

def run_agents():
    crew = Crew(
        agents=[explainer, literature_agent, gap_analyzer],
        tasks=[task1, task2, task3],
        verbose=True
    )
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    final_result = run_agents()
    print("\n\n🔍 Final Research Companion Output:\n", final_result)
