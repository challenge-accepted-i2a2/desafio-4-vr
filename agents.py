
from crewai import Agent
from dotenv import load_dotenv
import os
#from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM


load_dotenv()

class VRAgents:
    def __init__(self):
        # self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        # # Explicitly specify the model with the provider prefix for litellm compatibility
        # self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=self.gemini_api_key)
        
        self.openai_api_key = os.getenv("OPENAI_KEY_API")
        # Explicitly specify the model with the provider prefix for litellm compatibility
        self.llm = LLM(
            model="openai/gpt-4", # call model by provider/model_name
            temperature=0.8,
            max_tokens=150,
            top_p=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.1,
            stop=["END"],
            seed=42
        )


    def data_loader_agent(self):
        return Agent(
            role='Data Loader',
            goal='Load all necessary Excel files into pandas DataFrames',
            backstory='Expert in handling various Excel file formats and loading them efficiently.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    def consistency_agent(self):
        return Agent(
            role='Data Consistency Checker',
            goal='Perform consistency checks and cleaning on all loaded DataFrames',
            backstory='Meticulous in identifying and rectifying data inconsistencies, ensuring data quality.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def data_consolidation_agent(self):
        return Agent(
            role='Data Consolidator',
            goal='Consolidate data from multiple DataFrames into a single, unified DataFrame',
            backstory='Skilled in merging and combining disparate datasets accurately.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def exclusion_agent(self):
        return Agent(
            role='Exclusion Handler',
            goal='Apply exclusion rules to remove ineligible employees from the consolidated data',
            backstory='Proficient in identifying and filtering out specific employee categories based on predefined rules.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def validation_agent(self):
        return Agent(
            role='Data Validator',
            goal='Validate and correct inconsistencies in the processed data',
            backstory='Meticulous in identifying and rectifying data errors, ensuring data quality and integrity.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def calculation_agent(self):
        return Agent(
            role='VR Calculator',
            goal='Calculate the correct VR amount for each eligible employee based on various factors',
            backstory='Expert in complex financial calculations, especially concerning employee benefits and payroll adjustments.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def report_agent(self):
        return Agent(
            role='Report Generator',
            goal='Generate the final Excel report in the required format for the VR operator',
            backstory='Experienced in creating clear, accurate, and formatted reports for various stakeholders.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )


