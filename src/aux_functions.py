import pandas as pd
from datetime import date, timedelta
import numpy as np

def load_data():
    dataframes = {}
    files = {
        'ADMISSAOABRIL': 'ADMISSÃOABRIL.xlsx',
        'AFASTAMENTOS': 'AFASTAMENTOS.xlsx',
        'APRENDIZ': 'APRENDIZ.xlsx',
        'ATIVOS': 'ATIVOS.xlsx',
        'BASEDIAUTEIS': 'Basediasuteis.xlsx',
        'BASESINDICATOXVALOR': 'Basesindicatoxvalor.xlsx',
        'DESLIGADOS': 'DESLIGADOS.xlsx',
        'ESTAGIO': 'ESTÁGIO.xlsx',
        'EXTERIOR': 'EXTERIOR.xlsx',
        'FERIAS': 'FÉRIAS.xlsx',
        'VRMENSAL': 'VRMENSAL05.2025.xlsx'
    }

    for name, filename in files.items():
        path = f'./{filename}'
        if name == 'BASEDIAUTEIS':
            dataframes[name] = pd.read_excel(path, header=1)
            dataframes[name].columns = [col.strip() for col in dataframes[name].columns] # Strip spaces from column names
        elif name == 'BASESINDICATOXVALOR':
            dataframes[name] = pd.read_excel(path, header=0)
            dataframes[name].columns = [col.strip() for col in dataframes[name].columns] # Strip spaces from column names
        else:
            dataframes[name] = pd.read_excel(path)
    return dataframes

def consolidate_and_exclude(dfs):
    ativos = dfs['ATIVOS'].copy()
    admissoes = dfs['ADMISSAOABRIL'].copy()
    desligados = dfs['DESLIGADOS'].copy()

    admissoes = admissoes.rename(columns={'Admissão': 'DATA ADMISSAO', 'Cargo': 'TITULO DO CARGO'})
    desligados = desligados.rename(columns={'MATRICULA ': 'MATRICULA', 'DATA DEMISSÃO': 'DATA DESLIGAMENTO'})

    main_df = ativos.copy()

    main_df = pd.merge(main_df, admissoes[['MATRICULA', 'DATA ADMISSAO']], on='MATRICULA', how='left', suffixes=('_ativos', '_admissoes'))
    
    new_hires_not_in_ativos = admissoes[~admissoes['MATRICULA'].isin(main_df['MATRICULA'])]
    main_df = pd.concat([main_df, new_hires_not_in_ativos], ignore_index=True, sort=False)

    main_df['DATA ADMISSAO'] = pd.to_datetime(main_df['DATA ADMISSAO'])

    main_df = pd.merge(main_df, desligados[['MATRICULA', 'DATA DESLIGAMENTO', 'COMUNICADO DE DESLIGAMENTO']], on='MATRICULA', how='left')

    main_df['ELEGIVEL'] = True

    main_df.loc[main_df['TITULO DO CARGO'].str.contains('DIRETOR', na=False, case=False), 'ELEGIVEL'] = False

    estagio_matriculas = dfs['ESTAGIO']['MATRICULA'].unique()
    main_df.loc[main_df['MATRICULA'].isin(estagio_matriculas), 'ELEGIVEL'] = False

    aprendiz_matriculas = dfs['APRENDIZ']['MATRICULA'].unique()
    main_df.loc[main_df['MATRICULA'].isin(aprendiz_matriculas), 'ELEGIVEL'] = False

    afastados_matriculas = dfs['AFASTAMENTOS']['MATRICULA'].unique()
    main_df.loc[main_df['MATRICULA'].isin(afastados_matriculas), 'ELEGIVEL'] = False

    exterior_matriculas = dfs['EXTERIOR']['Cadastro'].unique()
    main_df.loc[main_df['MATRICULA'].isin(exterior_matriculas), 'ELEGIVEL'] = False

    return main_df

def calculate_vr(consolidated_df, dfs, month_year='2025-05'):
    ref_month_dt = pd.to_datetime(month_year)
    start_of_month = ref_month_dt.replace(day=1)
    end_of_month = (ref_month_dt + pd.offsets.MonthEnd(0))

    dias_uteis_sindicato = dfs['BASEDIAUTEIS'].set_index('SINDICADO')['DIAS UTEIS'].to_dict()
    valor_sindicato = dfs['BASESINDICATOXVALOR'].set_index('ESTADO')['VALOR'].to_dict()

    consolidated_df['DIAS_VR'] = 0
    consolidated_df['VALOR_VR_DIARIO'] = 0.0
    consolidated_df['TOTAL_VR'] = 0.0
    consolidated_df['Custo empresa'] = 0.0
    consolidated_df['Desconto profissional'] = 0.0

    ferias_df = dfs['FERIAS'].copy()
    ferias_df['MATRICULA'] = ferias_df['MATRICULA'].astype(int)
    ferias_map = ferias_df.set_index('MATRICULA')['DIAS DE FÉRIAS'].to_dict()

    for index, row in consolidated_df.iterrows():
        if row['ELEGIVEL']:
            sindicato = str(row['Sindicato'])
            matricula = row['MATRICULA']
            
            if pd.isna(sindicato) or sindicato == 'nan':
                consolidated_df.loc[index, 'ELEGIVEL'] = False
                continue

            estado = 'Não Definido'
            if 'PR' in sindicato: estado = 'Paraná'
            elif 'RS' in sindicato: estado = 'Rio Grande do Sul'
            elif 'RJ' in sindicato: estado = 'Rio de Janeiro'
            elif 'SP' in sindicato: estado = 'São Paulo'

            dias_uteis_base = dias_uteis_sindicato.get(sindicato, 0)
            valor_diario = valor_sindicato.get(estado, 0.0)

            dias_a_pagar = dias_uteis_base

            # Handle admissions
            if pd.notna(row['DATA ADMISSAO']) and row['DATA ADMISSAO'].month == ref_month_dt.month and row['DATA ADMISSAO'].year == ref_month_dt.year:
                admission_date = row['DATA ADMISSAO'].date()
                current_date = admission_date
                working_days_after_admission = 0
                while current_date <= end_of_month.date():
                    if current_date.weekday() < 5: # Monday to Friday
                        working_days_after_admission += 1
                    current_date += timedelta(days=1)
                dias_a_pagar = min(dias_a_pagar, working_days_after_admission)

            # Handle terminations
            if pd.notna(row['DATA DESLIGAMENTO']):
                data_desligamento = pd.to_datetime(row['DATA DESLIGAMENTO'])
                comunicado = row['COMUNICADO DE DESLIGAMENTO']
                
                if data_desligamento.month == ref_month_dt.month and data_desligamento.year == ref_month_dt.year:
                    if comunicado == 'OK' and data_desligamento.day <= 15:
                        dias_a_pagar = 0 # No payment if notified by day 15
                    else:
                        termination_date = data_desligamento.date()
                        current_date = start_of_month.date()
                        working_days_until_termination = 0
                        while current_date <= termination_date:
                            if current_date.weekday() < 5: # Monday to Friday
                                working_days_until_termination += 1
                            current_date += timedelta(days=1)
                        dias_a_pagar = min(dias_a_pagar, working_days_until_termination)

            # Handle vacations
            if matricula in ferias_map:
                dias_ferias = ferias_map[matricula]
                dias_a_pagar = max(0, dias_a_pagar - dias_ferias)

            consolidated_df.loc[index, 'DIAS_VR'] = dias_a_pagar
            consolidated_df.loc[index, 'VALOR_VR_DIARIO'] = valor_diario
            consolidated_df.loc[index, 'TOTAL_VR'] = dias_a_pagar * valor_diario
            consolidated_df.loc[index, 'Custo empresa'] = consolidated_df.loc[index, 'TOTAL_VR'] * 0.8
            consolidated_df.loc[index, 'Desconto profissional'] = consolidated_df.loc[index, 'TOTAL_VR'] * 0.2
        else:
            consolidated_df.loc[index, 'DIAS_VR'] = 0
            consolidated_df.loc[index, 'VALOR_VR_DIARIO'] = 0.0
            consolidated_df.loc[index, 'TOTAL_VR'] = 0.0
            consolidated_df.loc[index, 'Custo empresa'] = 0.0
            consolidated_df.loc[index, 'Desconto profissional'] = 0.0

    return consolidated_df

def generate_output_excel(final_df, output_filename='VR_MENSAL_05.2025.xlsx', month_year='2025-05'):
    output_df = pd.DataFrame()
    output_df['Matricula'] = final_df['MATRICULA']
    output_df['Admissão'] = final_df['DATA ADMISSAO']
    output_df['Sindicato do Colaborador'] = final_df['Sindicato']
    output_df['Competência'] = pd.to_datetime(month_year).replace(day=1)
    output_df['Dias'] = final_df['DIAS_VR']
    output_df['VALOR DIÁRIO VR'] = final_df['VALOR_VR_DIARIO']
    output_df['TOTAL'] = final_df['TOTAL_VR']
    output_df['Custo empresa'] = final_df['Custo empresa']
    output_df['Desconto profissional'] = final_df['Desconto profissional']
    output_df['OBS GERAL'] = '' # Placeholder for observations

    # Filter out ineligible employees and those with 0 VR days
    output_df = output_df[final_df['ELEGIVEL'] & (final_df['DIAS_VR'] > 0)]

    output_df.to_excel('outputs/'+output_filename, index=False)
    print(f'Generated output file: {output_filename}')

if __name__ == '__main__':
    dfs = load_data()
    consolidated_df = consolidate_and_exclude(dfs)
    final_df = calculate_vr(consolidated_df, dfs)
    print('--- Final DataFrame with VR Calculations ---')
    print(final_df[['MATRICULA', 'Sindicato', 'DATA ADMISSAO', 'DATA DESLIGAMENTO', 'ELEGIVEL', 'DIAS_VR', 'VALOR_VR_DIARIO', 'TOTAL_VR', 'Custo empresa', 'Desconto profissional']].head().to_markdown(index=False))
    total_vr_paid = final_df['TOTAL_VR'].sum()
    print(f'Total VR to be paid: {total_vr_paid:.2f}')
    generate_output_excel(final_df)

    target_total = 1380178.00
    tolerance = 0.05 * target_total # 5% tolerance
    if abs(total_vr_paid - target_total) < tolerance:
        print(f'Validation successful: Total VR ({total_vr_paid:.2f}) is close to target ({target_total:.2f}).')
    else:
        print(f'Validation warning: Total VR ({total_vr_paid:.2f}) is NOT close to target ({target_total:.2f}). Difference: {abs(total_vr_paid - target_total):.2f}')


