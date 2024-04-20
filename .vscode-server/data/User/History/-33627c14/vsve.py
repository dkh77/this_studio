import os
from dotenv import load_dotenv
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

os.environ['GROQ_API_KEY'] = config['GROQ_API_KEY']

def run():
    inputs = {
        'company_name': 'Tesla',
    }
    FinancialAnalystCrew().crew().kickoff(inputs = inputs)


if __name__ == "__main__":
    run()