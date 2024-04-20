from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task 
from langchain_groq import ChatGroq
import yaml
import os

# @CrewBase
# class FinancialAnalystCrew():
#     """FinancialAnalystCrew"""
#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'

#     def __init__(self) -> None:
#         self.groq_llm = ChatGroq(temperature = 0, model_name = "mixtral-8x7b-32768",groq_api_key=os.getenv("GROQ_API_KEY"))

print("Current Working Directory:", os.getcwd())

@CrewBase
class FinancialAnalystCrew():
    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=os.getenv("GROQ_API_KEY"))
        with open('/teamspace/studios/this_studio/src/financial_analyst_crew/config/agents.yaml', 'r') as file:
            self.agents_config = yaml.safe_load(file)
        with open('/teamspace/studios/this_studio/src/financial_analyst_crew/config/tasks.yaml', 'r') as file:
            self.tasks_config = yaml.safe_load(file)



    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['company_researcher'],
            llm = self.groq_llm
        )
        print("Company Researcher Initialized.")
        return researcher
    
    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['company_analyst'],
            llm = self.groq_llm
        )
        print("Company Analyst Initialized.")
        return analyst

    @task 
    # def research_company_task(self) -> Task:
    #     return Task(
    #         config = self.tasks_config['research_company_task'],
    #         agent = self.company_researcher()
    #     )

    def research_company_task(self) -> Task:        
        print("Executing research company task...")
        task = Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )
        result = task.execute()  # Ensure your Task class has an execute method or equivalent
        print("Research task result:", result)
        return task
    
    # def research_company_task(self, inputs) -> Task:
    #     print("Executing research company task with inputs:", inputs)
    #     # If 'description' contains placeholders, they should be replaced here
    #     task_description = self.tasks_config['research_company_task']['description'].format(**inputs)
    #     task = Task(
    #         description=task_description,
    #         agent=self.company_researcher()
    #     )
    #     return task
    
 
    @task
    def analyze_company_task(self) -> Task:
        print("Executing analyze company task...")
        task = Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )
        result = task.execute()  # As above
        print("Analyze task result:", result)
        return task

    # def analyze_company_task(self, inputs) -> Task:
    #     print("Executing analyze company task with inputs:", inputs)
    #     # If 'description' contains placeholders, they should be replaced here
    #     task_description = self.tasks_config['analyze_company_task']['description'].format(**inputs)
    #     task = Task(
    #         description=task_description,
    #         agent=self.company_analyst()
    #     )
    #     return task

    @crew
    def crew(self) -> Crew:
        """Creates the FinancialAnalystCrew"""""
        return Crew(
            agents = self.agents,
            task = self.tasks,
            process = Process.sequential,
            verbose = 2
        )

    # def crew(self) -> Crew:
    #     inputs = {'company_name': 'Tesla'}  # Make sure inputs are defined if not passed as a parameter
    #     print("Creating the crew...")
    #     crew_instance = Crew(
    #         agents=[self.company_researcher(), self.company_analyst()],
    #         tasks=[self.research_company_task(inputs), self.analyze_company_task(inputs)],  # Include inputs here
    #         process=Process.sequential,
    #         verbose=2
    #     )
    #     print("Crew created with agents and tasks.")
    #     return crew_instance