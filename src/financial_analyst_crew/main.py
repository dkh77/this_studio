import os
import traceback
from dotenv import load_dotenv
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

# def run():
#     print("Running the main function...")
#     try:
#         inputs = {'company_name': 'Tesla'}
#         print("Creating Financial Analyst Crew...")
#         crew = FinancialAnalystCrew()
#         print("Financial Analyst Crew created, kicking off the crew...")
#         result = crew.crew().kickoff(inputs=inputs)
#         print("Crew operation completed:", result)
#     except Exception as e:
#         print(f"Overall error occurred: {e}")
#         traceback.print_exc()

# if __name__ == "__main__":
#     run()

def run():
    print("Running the main function...")
    try:
        inputs = {'company_name': 'AMZN'}
        print("Input being passed to the crew:", inputs)
        crew = FinancialAnalystCrew()
        print("Creating Financial Analyst Crew...")
        print("Financial Analyst Crew created, kicking off the crew...")
        result = crew.crew().kickoff(inputs=inputs)
        print("Crew operation completed:", result)
    except Exception as e:
        print(f"Overall error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run()