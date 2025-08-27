
import pandas as pd

def consolidate_data(all_data):
    """Consolidates data from multiple sources into a single DataFrame."""
    # Start with the active employees
    base_df = all_data["ATIVOS"].copy()

    # Merge with admissions
    admissoes_df = all_data["ADMISSAOABRIL"]
    base_df = pd.merge(base_df, admissoes_df[["MATRICULA", "Admissão"]], on="MATRICULA", how="left")


    # Merge with union information
    sindicato_valor_df = all_data["BASESINDICATOVALOR"]

    # Clean column name for sindicato_valor_df
    sindicato_valor_df.columns = sindicato_valor_df.columns.str.strip()
    sindicato_valor_df.rename(columns={
        sindicato_valor_df.columns[0]: "Sindicato_Nome"
    }, inplace=True)

    list_sindicatos = sindicato_valor_df['Sindicato_Nome'].values
    
    #Função para verificar se texto_b está contido em algum texto_a
    def verificar_textos(list_sindicatos, base_df):
        resultados = []

        for texto_b in base_df['Sindicato']:
            texto_encontrado = None
            for texto_a in list_sindicatos:
                #print(f"texto a:{texto_a} , texto_b: {texto_b}")
                if texto_a.lower() in texto_b.lower():
                    texto_encontrado = texto_a
                    break
                elif ' SP '.lower() in texto_b.lower():
                    texto_encontrado = 'São Paulo'
                elif '  RJ '.lower() in texto_b.lower():
                    texto_encontrado = 'Rio de Janeiro'
                elif ' PR '.lower() in texto_b.lower():
                    texto_encontrado = 'Paraná'
            resultados.append({
                'Estado': texto_encontrado if texto_encontrado else 'Não encontrado'
            })

        return pd.DataFrame(resultados)

    # # Executar verificação
    df_estado = verificar_textos(list_sindicatos, base_df)
    base_df['Estado'] = df_estado.Estado

    # Merge based on the 'Sindicato' column from ATIVOS.xlsx and the cleaned 'Sindicato_Nome' from Basesindicatoxvalor.xlsx
    # Ensure the 'Sindicato' column from ATIVOS.xlsx is preserved and used for merging
    base_df = pd.merge(base_df, sindicato_valor_df, left_on="Estado", right_on="Sindicato_Nome", how="left")
    return base_df
