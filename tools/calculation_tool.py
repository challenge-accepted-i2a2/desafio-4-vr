
import pandas as pd

def calculate_vr(df, all_data):
    """Calculates the VR amount for each employee."""
    # Load relevant dataframes
    dias_uteis_sindicato_df = all_data["BASEDIASUTEIS"]
    desligados_df = all_data["DESLIGADOS"]

    # Clean column names for merging
    dias_uteis_sindicato_df.columns = ["Sindicato", "DIAS_UTEIS"]
    desligados_df.rename(columns={
        "MATRICULA ": "MATRICULA",
        "DATA DEMISSÃO": "DATA_DEMISSAO",
        "COMUNICADO DE DESLIGAMENTO": "COMUNICADO_DESLIGAMENTO"
    }, inplace=True)

    # Merge with dias uteis per union
    df = pd.merge(df, dias_uteis_sindicato_df, on="Sindicato", how="left")
    df["DIAS_UTEIS"] = df["DIAS_UTEIS"].fillna(0) # Fill NaN for those without a matching union

    # Apply desligamento rules
    df = pd.merge(df, desligados_df[["MATRICULA", "DATA_DEMISSAO", "COMUNICADO_DESLIGAMENTO"]], on="MATRICULA", how="left")

    # Convert DATA_DEMISSAO to datetime
    df["DATA_DEMISSAO"] = pd.to_datetime(df["DATA_DEMISSAO"], errors='coerce')

    # Define the reference date for desligamento rule (15th of the month)
    reference_date_15th = pd.to_datetime("2025-05-15")

    def apply_desligamento_rule(row):
        if pd.notna(row["DATA_DEMISSAO"]) and row["COMUNICADO_DESLIGAMENTO"] == 'OK':
            if row["DATA_DEMISSAO"].day <= reference_date_15th.day:
                return 0  # Do not consider for payment
            else:
                total_days_in_month = 31 # For May
                days_after_15th = total_days_in_month - reference_date_15th.day
                return row["DIAS_UTEIS"] * (days_after_15th / total_days_in_month)
        return row["DIAS_UTEIS"]

    df["DIAS_UTEIS_AJUSTADO"] = df.apply(apply_desligamento_rule, axis=1)

    # Adjust for vacation days
    df["DIAS_UTEIS_AJUSTADO"] = df["DIAS_UTEIS_AJUSTADO"] - df["DIAS DE FÉRIAS"]
    df["DIAS_UTEIS_AJUSTADO"] = df["DIAS_UTEIS_AJUSTADO"].apply(lambda x: max(0, x)) # Ensure non-negative days

    # Calculate total VR value
    df["VALOR_VR_TOTAL"] = df["DIAS_UTEIS_AJUSTADO"] * df["VALOR"]

    # Calculate company and employee cost
    df["CUSTO_EMPRESA"] = df["VALOR_VR_TOTAL"] * 0.80
    df["CUSTO_PROFISSIONAL"] = df["VALOR_VR_TOTAL"] * 0.20

    return df


