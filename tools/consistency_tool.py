import pandas as pd

def check_and_clean_consistency(df):
    """Performs consistency checks and cleaning on a DataFrame."""
    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Remove leading/trailing spaces from string values in all columns
    for col in df.columns:
        if df[col].dtype == "object": # Check if the column contains strings
            df[col] = df[col].astype(str).str.strip()

    # Drop rows where all values are NaN
    df.dropna(how='all', inplace=True)

    return df

def apply_consistency_checks_to_all_data(all_data):
    """Applies consistency checks to all DataFrames in the dictionary."""
    cleaned_data = {}
    for name, df in all_data.items():
        cleaned_data[name] = check_and_clean_consistency(df.copy()) # Operate on a copy
    return cleaned_data
