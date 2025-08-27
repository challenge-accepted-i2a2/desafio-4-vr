
from crewai import Task
from tools.custom_tools import DataLoaderTool, DataConsolidationTool, ExclusionTool, ValidationTool, CalculationTool, ReportGeneratorTool, ConsistencyTool

class VRTasks:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data_task(self, agent):
        return Task(
            description=f"Load all Excel files from {self.data_dir} into pandas DataFrames.",
            agent=agent,
            expected_output="A dictionary containing all loaded pandas DataFrames. Formatted as markdown without '```",
            output_file="./data/loaded_data.pkl", # Store loaded data for subsequent tasks
            human_input=True,
            tools=[DataLoaderTool()]
        )

    def consistency_check_task(self, agent, all_data):
        return Task(
            description="Apply consistency checks and cleaning to all loaded DataFrames.",
            agent=agent,
            expected_output="A dictionary containing cleaned pandas DataFrames.",
            output_file="./data/cleaned_data.pkl",
            context=[all_data],
            tools=[ConsistencyTool()]
        )

    def consolidate_data_task(self, agent, all_data):
        return Task(
            description="Consolidate the loaded DataFrames into a single, unified DataFrame.",
            agent=agent,
            expected_output="A single pandas DataFrame containing consolidated employee data.",
            output_file="./data/consolidated_data.pkl",
            context=[all_data],
            tools=[DataConsolidationTool()]
        )

    def apply_exclusion_task(self, agent, consolidated_data, all_data):
        return Task(
            description="Apply exclusion rules to the consolidated data to remove ineligible employees.",
            agent=agent,
            expected_output="A pandas DataFrame with ineligible employees removed.",
            output_file="./data/excluded_data.pkl",
            context=[consolidated_data, all_data],
            tools=[ExclusionTool()]
        )

    def validate_data_task(self, agent, excluded_data, all_data):
        return Task(
            description="Validate and correct inconsistencies in the excluded data.",
            agent=agent,
            expected_output="A clean and validated pandas DataFrame.",
            output_file="./data/validated_data.pkl",
            context=[excluded_data, all_data],
            tools=[ValidationTool()]
        )

    def calculate_vr_task(self, agent, validated_data, all_data):
        return Task(
            description="Calculate the correct VR amount for each eligible employee.",
            agent=agent,
            expected_output="A pandas DataFrame with calculated VR amounts, company cost, and employee cost.",
            output_file="./data/calculated_vr.pkl",
            context=[validated_data, all_data],
            tools=[CalculationTool()]
        )

    def generate_report_task(self, agent, calculated_vr_data, output_path):
        return Task(
            description=f"Generate the final Excel report at {output_path} in the required format.",
            agent=agent,
            expected_output="A confirmation message that the Excel report has been generated.",
            context=[calculated_vr_data, output_path],
            tools=[ReportGeneratorTool()]
        )


