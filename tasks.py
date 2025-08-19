from crewai import Task
from agents import explainer, literature_agent, gap_analyzer

task1 = Task(
    description="Read the research paper and explain the main topic, concepts, and technical terms.",
    agent=explainer,
    expected_output="A layman-friendly explanation of the paper's topic"
)

task2 = Task(
    description="Find related research papers or background knowledge connected to this topic.",
    agent=literature_agent,
    expected_output="A short list of related research themes or past work"
)

task3 = Task(
    description="Analyze the paper and identify gaps or open questions that the paper does not address.",
    agent=gap_analyzer,
    expected_output="A bullet-point list of potential research gaps or unanswered questions"
)