
import pandas as pd
import os

data_dir = './data'

def load_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

ativos_df = load_excel_data(os.path.join(data_dir, 'ATIVOS.xlsx'))

print("ATIVOS.xlsx columns:", ativos_df.columns.tolist() if ativos_df is not None else "Error")


