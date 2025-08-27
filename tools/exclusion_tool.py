
import pandas as pd

def apply_exclusions(base_df, all_data):
    """Applies exclusion rules to the base DataFrame."""
    # Exclude directors, interns, and apprentices
    base_df = base_df[~base_df["TITULO DO CARGO"].str.contains("DIRETOR|ESTAGIARIO|APRENDIZ", case=False, na=False)]

    # Exclude employees on leave
    afastamentos_df = all_data["AFASTAMENTOS"]
    base_df = base_df[~base_df["MATRICULA"].isin(afastamentos_df["MATRICULA"])]

    # Exclude employees working abroad
    exterior_df = all_data["EXTERIOR"]
    base_df = base_df[~base_df["MATRICULA"].isin(exterior_df["Cadastro"])]

    return base_df


