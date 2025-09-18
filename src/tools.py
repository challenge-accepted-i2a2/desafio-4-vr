# tools.py
from crewai_tools import BaseTool
import pandas as pd

# Importe as funções originais do seu script
from vr_automation import load_data, consolidate_and_exclude, calculate_vr, generate_output_excel

# Para passar dados complexos (DataFrames) entre agentes, vamos usar um "data cache" simples.
# Em um sistema de produção, isso poderia ser um Redis, um banco de dados, ou arquivos em disco.
data_cache = {}

class DataLoadTool(BaseTool):
    name: str = "Ferramenta de Carregamento de Dados de RH"
    description: str = "Use esta ferramenta para carregar todos os arquivos Excel iniciais necessários para o cálculo do VR. O resultado é armazenado internamente para a próxima etapa."

    def _run(self) -> str:
        print("\nExecutando Ferramenta de Carregamento de Dados...")
        dataframes = load_data()
        data_cache['loaded_data'] = dataframes
        # Retorna uma confirmação e um resumo do que foi carregado
        return f"Dados carregados com sucesso. {len(dataframes)} arquivos processados: {list(dataframes.keys())}"

class ConsolidateTool(BaseTool):
    name: str = "Ferramenta de Consolidação e Exclusão"
    description: str = "Use esta ferramenta para consolidar as bases de funcionários e aplicar regras de elegibilidade. Requer que os dados já tenham sido carregados."

    def _run(self) -> str:
        print("\nExecutando Ferramenta de Consolidação...")
        if 'loaded_data' not in data_cache:
            return "Erro: Os dados precisam ser carregados primeiro usando a Ferramenta de Carregamento."
        
        dfs = data_cache['loaded_data']
        consolidated_df = consolidate_and_exclude(dfs)
        data_cache['consolidated_data'] = consolidated_df
        return f"Dados consolidados com sucesso. {len(consolidated_df)} registros processados. {consolidated_df['ELEGIVEL'].sum()} funcionários são elegíveis."

class CalculateVRTool(BaseTool):
    name: str = "Ferramenta de Cálculo de Vale-Refeição"
    description: str = "Use esta ferramenta para executar o cálculo principal do VR para cada funcionário elegível. Requer que os dados já tenham sido consolidados."

    def _run(self) -> str:
        print("\nExecutando Ferramenta de Cálculo de VR...")
        if 'loaded_data' not in data_cache or 'consolidated_data' not in data_cache:
            return "Erro: Os dados precisam ser carregados e consolidados primeiro."

        dfs = data_cache['loaded_data']
        consolidated_df = data_cache['consolidated_data']
        final_df = calculate_vr(consolidated_df, dfs)
        data_cache['final_data'] = final_df
        total_vr = final_df['TOTAL_VR'].sum()
        return f"Cálculo de VR finalizado com sucesso. Valor total a ser pago: R$ {total_vr:,.2f}"

class GenerateExcelTool(BaseTool):
    name: str = "Ferramenta de Geração de Relatório Excel"
    description: str = "Use esta ferramenta para gerar o arquivo Excel final com os resultados do cálculo do VR. Esta é a última etapa do processo."

    def _run(self) -> str:
        print("\nExecutando Ferramenta de Geração de Excel...")
        if 'final_data' not in data_cache:
            return "Erro: O cálculo do VR precisa ser executado primeiro."
            
        final_df = data_cache['final_data']
        output_filename = 'VR_MENSAL_05.2025_RESULTADO.xlsx'
        generate_output_excel(final_df, output_filename=output_filename)
        return f"Relatório Excel '{output_filename}' gerado com sucesso."