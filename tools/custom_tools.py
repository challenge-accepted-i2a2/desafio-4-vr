
from crewai.tools import BaseTool
from .data_loader import load_all_data
from .data_consolidation_tool import consolidate_data
from .exclusion_tool import apply_exclusions
from .validation_tool import validate_and_correct_data
from .calculation_tool import calculate_vr
from .report_generator import generate_final_report
from .consistency_tool import apply_consistency_checks_to_all_data

class DataLoaderTool(BaseTool):
    name: str = "Data Loader Tool"
    description: str = "Loads all necessary Excel files into pandas DataFrames."

    def _run(self, data_dir: str):
        return load_all_data(data_dir)

class ConsistencyTool(BaseTool):
    name: str = "Consistency Tool"
    description: str = "Applies consistency checks and cleaning to all DataFrames."

    def _run(self, all_data: dict):
        return apply_consistency_checks_to_all_data(all_data)

class DataConsolidationTool(BaseTool):
    name: str = "Data Consolidation Tool"
    description: str = "Consolidates data from multiple DataFrames into a single, unified DataFrame."

    def _run(self, all_data: dict):
        return consolidate_data(all_data)

class ExclusionTool(BaseTool):
    name: str = "Exclusion Tool"
    description: str = "Applies exclusion rules to remove ineligible employees from the consolidated data."

    def _run(self, base_df: dict, all_data: dict):
        # Convert dict to DataFrame if necessary, as it's passed as a dict from CrewAI
        import pandas as pd
        if isinstance(base_df, dict):
            base_df = pd.DataFrame(base_df)
        return apply_exclusions(base_df, all_data)

class ValidationTool(BaseTool):
    name: str = "Validation Tool"
    description: str = "Validates and corrects inconsistencies in the processed data."

    def _run(self, df: dict, all_data: dict):
        import pandas as pd
        if isinstance(df, dict):
            df = pd.DataFrame(df)
        return validate_and_correct_data(df, all_data)

class CalculationTool(BaseTool):
    name: str = "Calculation Tool"
    description: str = "Calculates the correct VR amount for each eligible employee based on various factors."

    def _run(self, df: dict, all_data: dict):
        import pandas as pd
        if isinstance(df, dict):
            df = pd.DataFrame(df)
        return calculate_vr(df, all_data)

class ReportGeneratorTool(BaseTool):
    name: str = "Report Generator Tool"
    description: str = "Generates the final Excel report in the required format for the VR operator."

    def _run(self, df: dict, output_path: str):
        import pandas as pd
        if isinstance(df, dict):
            df = pd.DataFrame(df)
        return generate_final_report(df, output_path)


