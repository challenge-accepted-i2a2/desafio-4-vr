# tasks.py - Definição das Tarefas do Sistema

## Descrição
O arquivo `tasks.py` define a classe `VRTasks` que contém todas as tarefas executadas pelos agentes no sistema de processamento de Vale Refeição. Cada tarefa é especializada e corresponde a uma etapa específica do pipeline.

## Classe VRTasks

### Inicialização
```python
def __init__(self, data_dir):
    self.data_dir = data_dir
```
**Parâmetro**: `data_dir` - Diretório onde estão localizados os arquivos de dados

## Tarefas Especializadas

### 1. Load Data Task
```python
def load_data_task(self, agent):
    return Task(
        description=f"Load all Excel files from {self.data_dir} into pandas DataFrames.",
        agent=agent,
        expected_output="A dictionary containing all loaded pandas DataFrames. Formatted as markdown without '```",
        output_file="./data/loaded_data.pkl",
        human_input=True,
        tools=[DataLoaderTool()]
    )
```
**Função**: Carrega todos os arquivos Excel da pasta data/
**Saída**: Dicionário com DataFrames pandas
**Arquivo de Saída**: `loaded_data.pkl`
**Ferramenta**: `DataLoaderTool()`
**Interação Humana**: Habilitada

### 2. Consistency Check Task
```python
def consistency_check_task(self, agent, all_data):
    return Task(
        description="Apply consistency checks and cleaning to all loaded DataFrames.",
        agent=agent,
        expected_output="A dictionary containing cleaned pandas DataFrames.",
        output_file="./data/cleaned_data.pkl",
        context=[all_data],
        tools=[ConsistencyTool()]
    )
```
**Função**: Aplica verificações de consistência nos dados carregados
**Contexto**: Dados carregados na etapa anterior
**Saída**: DataFrames limpos
**Arquivo de Saída**: `cleaned_data.pkl`
**Ferramenta**: `ConsistencyTool()`

### 3. Consolidate Data Task
```python
def consolidate_data_task(self, agent, all_data):
    return Task(
        description="Consolidate the loaded DataFrames into a single, unified DataFrame.",
        agent=agent,
        expected_output="A single pandas DataFrame containing consolidated employee data.",
        output_file="./data/consolidated_data.pkl",
        context=[all_data],
        tools=[DataConsolidationTool()]
    )
```
**Função**: Consolida múltiplos DataFrames em um único DataFrame
**Contexto**: Todos os dados carregados
**Saída**: DataFrame único consolidado
**Arquivo de Saída**: `consolidated_data.pkl`
**Ferramenta**: `DataConsolidationTool()`

### 4. Apply Exclusion Task
```python
def apply_exclusion_task(self, agent, consolidated_data, all_data):
    return Task(
        description="Apply exclusion rules to the consolidated data to remove ineligible employees.",
        agent=agent,
        expected_output="A pandas DataFrame with ineligible employees removed.",
        output_file="./data/excluded_data.pkl",
        context=[consolidated_data, all_data],
        tools=[ExclusionTool()]
    )
```
**Função**: Remove funcionários inelegíveis baseado em regras de negócio
**Contexto**: Dados consolidados + todos os dados originais
**Saída**: DataFrame com funcionários elegíveis
**Arquivo de Saída**: `excluded_data.pkl`
**Ferramenta**: `ExclusionTool()`

### 5. Validate Data Task
```python
def validate_data_task(self, agent, excluded_data, all_data):
    return Task(
        description="Validate and correct inconsistencies in the excluded data.",
        agent=agent,
        expected_output="A clean and validated pandas DataFrame.",
        output_file="./data/validated_data.pkl",
        context=[excluded_data, all_data],
        tools=[ValidationTool()]
    )
```
**Função**: Valida e corrige inconsistências nos dados processados
**Contexto**: Dados após exclusões + todos os dados originais
**Saída**: DataFrame validado e corrigido
**Arquivo de Saída**: `validated_data.pkl`
**Ferramenta**: `ValidationTool()`

### 6. Calculate VR Task
```python
def calculate_vr_task(self, agent, validated_data, all_data):
    return Task(
        description="Calculate the correct VR amount for each eligible employee.",
        agent=agent,
        expected_output="A pandas DataFrame with calculated VR amounts, company cost, and employee cost.",
        output_file="./data/calculated_vr.pkl",
        context=[validated_data, all_data],
        tools=[CalculationTool()]
    )
```
**Função**: Calcula valores corretos de VR para cada funcionário elegível
**Contexto**: Dados validados + todos os dados originais
**Saída**: DataFrame com valores de VR, custo empresa e funcionário
**Arquivo de Saída**: `calculated_vr.pkl`
**Ferramenta**: `CalculationTool()`

### 7. Generate Report Task
```python
def generate_report_task(self, agent, calculated_vr_data, output_path):
    return Task(
        description=f"Generate the final Excel report at {output_path} in the required format.",
        agent=agent,
        expected_output="A confirmation message that the Excel report has been generated.",
        context=[calculated_vr_data, output_path],
        tools=[ReportGeneratorTool()]
    )
```
**Função**: Gera relatório final em formato Excel
**Contexto**: Dados com VR calculado + caminho de saída
**Saída**: Mensagem de confirmação
**Arquivo de Saída**: Relatório Excel no caminho especificado
**Ferramenta**: `ReportGeneratorTool()`

## Ferramentas Importadas
```python
from tools.custom_tools import (
    DataLoaderTool,
    DataConsolidationTool, 
    ExclusionTool,
    ValidationTool,
    CalculationTool,
    ReportGeneratorTool,
    ConsistencyTool
)
```

## Características das Tarefas

### Estrutura Comum
- **Description**: Descrição detalhada da tarefa
- **Agent**: Agente responsável pela execução
- **Expected Output**: Formato esperado da saída
- **Output File**: Arquivo onde o resultado é salvo
- **Context**: Dados de entrada da tarefa
- **Tools**: Ferramentas especializadas utilizadas

### Fluxo de Dados
1. Cada tarefa gera um arquivo pickle com o resultado
2. Tarefas subsequentes usam estes arquivos como contexto
3. O pipeline mantém rastreabilidade completa dos dados

## Dependências
- `crewai.Task` - Classe base para tarefas
- `tools.custom_tools` - Ferramentas especializadas

## Uso
```python
from tasks import VRTasks

vr_tasks = VRTasks(data_dir='./data')
task = vr_tasks.load_data_task(agent)
```