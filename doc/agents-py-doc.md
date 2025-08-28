# agents.py - Definição dos Agentes de IA

## Descrição
O arquivo `agents.py` define a classe `VRAgents` que contém todos os agentes especializados de IA utilizados no sistema de processamento de Vale Refeição. Cada agente tem um papel específico no pipeline de dados.

## Classe VRAgents

### Inicialização
```python
def __init__(self):
    self.openai_api_key = os.getenv("OPENAI_KEY_API")
    self.llm = LLM(
        model="openai/gpt-4",
        temperature=0.8,
        max_tokens=150,
        top_p=0.9,
        frequency_penalty=0.1,
        presence_penalty=0.1,
        stop=["END"],
        seed=42
    )
```

### Configuração do Modelo LLM
- **Modelo**: OpenAI GPT-4
- **Temperature**: 0.8 (controla criatividade)
- **Max Tokens**: 150 (limite de tokens por resposta)
- **Top P**: 0.9 (controle de diversidade)
- **Frequency/Presence Penalty**: 0.1 (reduz repetições)
- **Seed**: 42 (reprodutibilidade)

## Agentes Especializados

### 1. Data Loader Agent
```python
def data_loader_agent(self):
    return Agent(
        role='Data Loader',
        goal='Load all necessary Excel files into pandas DataFrames',
        backstory='Expert in handling various Excel file formats and loading them efficiently.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Carrega arquivos Excel e converte para DataFrames pandas
**Especialidade**: Manipulação eficiente de múltiplos formatos Excel

### 2. Consistency Agent
```python
def consistency_agent(self):
    return Agent(
        role='Data Consistency Checker',
        goal='Perform consistency checks and cleaning on all loaded DataFrames',
        backstory='Meticulous in identifying and rectifying data inconsistencies, ensuring data quality.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Identifica e corrige inconsistências nos dados
**Especialidade**: Garantia de qualidade e integridade dos dados

### 3. Data Consolidation Agent
```python
def data_consolidation_agent(self):
    return Agent(
        role='Data Consolidator',
        goal='Consolidate data from multiple DataFrames into a single, unified DataFrame',
        backstory='Skilled in merging and combining disparate datasets accurately.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Mescla múltiplos DataFrames em um dataset unificado
**Especialidade**: Combinação precisa de datasets díspares

### 4. Exclusion Agent
```python
def exclusion_agent(self):
    return Agent(
        role='Exclusion Handler',
        goal='Apply exclusion rules to remove ineligible employees from the consolidated data',
        backstory='Proficient in identifying and filtering out specific employee categories based on predefined rules.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Aplica regras de negócio para excluir funcionários inelegíveis
**Especialidade**: Filtros baseados em regras predefinidas

### 5. Validation Agent
```python
def validation_agent(self):
    return Agent(
        role='Data Validator',
        goal='Validate and correct inconsistencies in the processed data',
        backstory='Meticulous in identifying and rectifying data errors, ensuring data quality and integrity.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Valida dados processados e corrige erros
**Especialidade**: Garantia de qualidade e integridade final

### 6. Calculation Agent
```python
def calculation_agent(self):
    return Agent(
        role='VR Calculator',
        goal='Calculate the correct VR amount for each eligible employee based on various factors',
        backstory='Expert in complex financial calculations, especially concerning employee benefits and payroll adjustments.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Calcula valores corretos de VR para cada funcionário
**Especialidade**: Cálculos financeiros complexos de benefícios

### 7. Report Agent
```python
def report_agent(self):
    return Agent(
        role='Report Generator',
        goal='Generate the final Excel report in the required format for the VR operator',
        backstory='Experienced in creating clear, accurate, and formatted reports for various stakeholders.',
        verbose=True,
        allow_delegation=False,
        llm=self.llm
    )
```
**Função**: Gera relatório final formatado para operadora de VR
**Especialidade**: Criação de relatórios claros e precisos

## Características Comuns dos Agentes

- **Verbose**: True (logs detalhados de execução)
- **Allow Delegation**: False (não delegam tarefas para outros agentes)
- **LLM Compartilhado**: Todos usam a mesma configuração do GPT-4

## Dependências
- `crewai.Agent` - Classe base para agentes
- `crewai.LLM` - Interface para modelos de linguagem
- `dotenv` - Carregamento de variáveis de ambiente
- `os` - Acesso a variáveis de ambiente

## Configuração Requerida
O arquivo requer a variável de ambiente:
```
OPENAI_KEY_API=sua_chave_api_openai
```

## Uso
```python
from agents import VRAgents

vra_agents = VRAgents()
data_loader = vra_agents.data_loader_agent()
```