
import os
import pandas as pd
from tools.data_loader import load_all_data
from tools.consistency_tool import apply_consistency_checks_to_all_data
from tools.data_consolidation_tool import consolidate_data
from tools.exclusion_tool import apply_exclusions
from tools.validation_tool import validate_and_correct_data
from tools.calculation_tool import calculate_vr
from tools.report_generator import generate_final_report

if __name__ == "__main__":
    data_dir = './data'
    output_report_path = os.path.join(data_dir, "VR_Report.csv")

    print("--- Starting Data Loading ---")
    all_data = load_all_data(data_dir)
    if not all_data:
        print("No data loaded. Exiting.")
        exit()
    print("--- Data Loading Complete ---")

    print("--- Starting Consistency Check ---")
    all_data = apply_consistency_checks_to_all_data(all_data)
    print("--- Consistency Check Complete ---")

    print("--- Starting Data Consolidation ---")
    consolidated_data = consolidate_data(all_data)
    print("--- Data Consolidation Complete ---")

    print("--- Starting Exclusion Application ---")
    excluded_data = apply_exclusions(consolidated_data, all_data)
    print("--- Exclusion Application Complete ---")
 
    print("--- Starting Data Validation ---")
    validated_data = validate_and_correct_data(excluded_data, all_data)
    print("--- Data Validation Complete ---")
    
    print("--- Starting VR Calculation ---")
    calculated_vr_data = calculate_vr(validated_data, all_data)
    print("--- VR Calculation Complete ---")

    print("--- Starting Report Generation ---")
    generate_final_report(calculated_vr_data, output_report_path)
    print("--- Report Generation Complete ---")

    print(f"\nVR Automation process completed. Final report saved to {output_report_path}")


