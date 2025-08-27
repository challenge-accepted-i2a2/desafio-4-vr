
import pandas as pd

def generate_final_report(df, output_path):
    """Generates the final Excel report for the VR operator."""
    # Select and reorder columns as per the VR Mensal 05.2025 template
    # Assuming the template has columns like: MATRICULA, VALOR_VR_TOTAL, CUSTO_EMPRESA, CUSTO_PROFISSIONAL
    
    output_df = df[[
        "MATRICULA", 
        "VALOR_VR_TOTAL", 
        "CUSTO_EMPRESA", 
        "CUSTO_PROFISSIONAL"
    ]].copy()

    try:
        output_df.to_csv(output_path, index=False)
        print(f"Final report generated successfully at {output_path}")
    except Exception as e:
        print(f"Error generating final report: {e}")


