from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task 
from langchain_groq import ChatGroq


@CrewBase
class FinancialAnalystCrew():
    """FinancialAnalystCrew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature = 0, model_name = "mixtral-8x7b-32768")

    @agent
    def company_researcher():
        return Agent(
            config = self.agents_config['company_researcher'],
            llm = self.groq_llm
        )