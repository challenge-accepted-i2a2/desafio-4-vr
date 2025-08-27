
import pandas as pd

def validate_and_correct_data(df, all_data):
    """Validates and corrects data inconsistencies."""
    # Example: Handle missing values in key columns
    # For demonstration, let's assume 'MATRICULA' and 'VALOR' are crucial

    df.dropna(subset=["MATRICULA", "VALOR"], inplace=True)
    
    # Example: Correct inconsistent dates (this is a placeholder, actual logic depends on specific inconsistencies)
    # If 'Admissão' date is in the future, set it to a default or flag it
    if 'Admissão' in df.columns:
        df['Admissão'] = pd.to_datetime(df['Admissão'], errors='coerce')
        df = df[df['Admissão'].notna()]
        # Assuming current date is 2025-05-01 for this challenge context
        df = df[df['Admissão'] <= pd.to_datetime('2025-05-01')]

    # Handle vacation data (assuming 'FÉRIAS.xlsx' contains 'MATRICULA' and 'DIAS DE FÉRIAS')
    ferias_df = all_data["FERIAS"]
    if not ferias_df.empty:
        # Merge to get vacation days for each employee
        df = pd.merge(df, ferias_df[["MATRICULA", "DIAS DE FÉRIAS"]], on="MATRICULA", how="left")
        df["DIAS DE FÉRIAS"] = df["DIAS DE FÉRIAS"].fillna(0) # Fill NaN for those not on vacation

    # Placeholder for holiday application logic (requires a holiday calendar)
    # For now, we'll assume no specific holiday calendar is provided, so this is a conceptual step.
    # In a real scenario, you'd load a holiday calendar and adjust working days.
    
    return df


