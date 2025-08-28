# main.py - Arquivo Principal do Sistema

## Descrição
O arquivo `main.py` é o ponto de entrada principal do sistema de automação de Vale Refeição. Ele orquestra a execução sequencial de todos os agentes de IA para processar dados de funcionários e gerar relatórios de VR.

## Funcionalidades Principais

### 1. Inicialização do Sistema
- Carrega variáveis de ambiente do arquivo `.env`
- Cria o diretório `./data` se não existir
- Inicializa instâncias das classes `VRAgents` e `VRTasks`

### 2. Definição dos Agentes
O sistema define 7 agentes especializados:
- `data_loader_agent` - Carregamento de dados
- `consistency_agent` - Verificação de consistência
- `data_consolidation_agent` - Consolidação de dados
- `exclusion_agent` - Aplicação de exclusões
- `validation_agent` - Validação de dados
- `calculation_agent` - Cálculo de valores VR
- `report_agent` - Geração de relatórios

### 3. Pipeline de Execução Sequencial

#### Etapa 1: Carregamento de Dados
```python
load_data_task = vr_tasks.load_data_task(data_loader_agent)
```
- Carrega todos os arquivos Excel da pasta `data/`
- Salva resultado em `loaded_data.pkl`

#### Etapa 2: Verificação de Consistência
```python
consistency_check_task = vr_tasks.consistency_check_task(consistency_agent, all_data)
```
- Aplica verificações de consistência nos dados carregados
- Salva dados limpos em `cleaned_data.pkl`

#### Etapa 3: Consolidação de Dados
```python
consolidate_data_task = vr_tasks.consolidate_data_task(data_consolidation_agent, all_data)
```
- Consolida dados de múltiplos DataFrames em um único DataFrame
- Salva resultado em `consolidated_data.pkl`

#### Etapa 4: Aplicação de Exclusões
```python
apply_exclusion_task = vr_tasks.apply_exclusion_task(exclusion_agent, consolidated_data, all_data)
```
- Remove funcionários inelegíveis baseado em regras de negócio
- Salva dados filtrados em `excluded_data.pkl`

#### Etapa 5: Validação de Dados
```python
validate_data_task = vr_tasks.validate_data_task(validation_agent, excluded_data, all_data)
```
- Valida e corrige inconsistências nos dados processados
- Salva dados validados em `validated_data.pkl`

#### Etapa 6: Cálculo de VR
```python
calculate_vr_task = vr_tasks.calculate_vr_task(calculation_agent, validated_data, all_data)
```
- Calcula valores de VR para cada funcionário elegível
- Considera custos da empresa e funcionário
- Salva dados calculados em `calculated_vr.pkl`

#### Etapa 7: Geração de Relatório
```python
generate_report_task = vr_tasks.generate_report_task(report_agent, calculated_vr_data, output_report_path)
```
- Gera relatório final em formato Excel
- Salva como `VR_Report.xlsx` na pasta `data/`

## Dependências
- `crewai` - Framework de agentes colaborativos
- `pandas` - Manipulação de dados
- `os` - Operações do sistema operacional
- `dotenv` - Carregamento de variáveis de ambiente

## Tratamento de Erros
O sistema implementa tratamento robusto de erros:
- Verifica se arquivos pickle podem ser carregados
- Exibe mensagens de erro detalhadas
- Encerra execução em caso de falha crítica

## Saída do Sistema
Ao final da execução bem-sucedida, o sistema:
- Gera mensagens de log para cada etapa
- Salva arquivos intermediários para debug
- Cria o relatório final `VR_Report.xlsx`
- Exibe mensagem de confirmação: "VR Automation process completed"

## Uso
```bash
python main.py
```

O processo é totalmente automatizado e não requer intervenção manual após inicialização.