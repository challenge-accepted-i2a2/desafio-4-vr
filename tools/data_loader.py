
import pandas as pd

def load_excel_data(file_path):
    """Loads data from an Excel file into a pandas DataFrame."""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def load_all_data(data_dir):
    """Loads all specified Excel files into a dictionary of DataFrames."""

    files = {
        'ATIVOS': f'{data_dir}/ATIVOS.xlsx',
        'VRMENSAL': f'{data_dir}/VRMENSAL05.2025.xlsx',
        'EXTERIOR': f'{data_dir}/EXTERIOR.xlsx',
        'DESLIGADOS': f'{data_dir}/DESLIGADOS.xlsx',
        'FERIAS': f'{data_dir}/FÉRIAS.xlsx',
        'APRENDIZ': f'{data_dir}/APRENDIZ.xlsx',
        'AFASTAMENTOS': f'{data_dir}/AFASTAMENTOS.xlsx',
        'BASESINDICATOVALOR': f'{data_dir}/Basesindicatoxvalor.xlsx',
        'ESTAGIO': f'{data_dir}/ESTÁGIO.xlsx',
        'BASEDIASUTEIS': f'{data_dir}/Basediasuteis.xlsx',
        'ADMISSAOABRIL': f'{data_dir}/ADMISSÃOABRIL.xlsx'
    }
    
    all_data = {}
    for name, path in files.items():
        df = load_excel_data(path)
        if df is not None:
            all_data[name] = df
            df.to_pickle(f'{data_dir}/loaded_data.pkl')
    return all_data


