# requirements.txt - Dependências do Projeto

## Descrição
O arquivo `requirements.txt` lista todas as dependências Python necessárias para executar o sistema de automação de Vale Refeição. Estas bibliotecas fornecem funcionalidades essenciais para agentes de IA, manipulação de dados e integração com APIs.

## Dependências Principais

### 1. crewai
```
crewai
```
**Função**: Framework principal para criação e orquestração de agentes de IA colaborativos
**Uso no Projeto**: Criação dos 7 agentes especializados e coordenação das tarefas
**Características**: 
- Sistema multi-agentes
- Execução sequencial de tarefas
- Comunicação entre agentes

### 2. crewai_tools
```
crewai_tools
```
**Função**: Conjunto de ferramentas especializadas para CrewAI
**Uso no Projeto**: Ferramentas customizadas para cada etapa do pipeline
**Características**:
- Integração nativa com CrewAI
- Ferramentas base para extensão

### 3. pandas
```
pandas
```
**Função**: Biblioteca para manipulação e análise de dados
**Uso no Projeto**: 
- Carregamento de arquivos Excel
- Processamento de DataFrames
- Manipulação de dados tabulares
- Operações de merge e consolidação

### 4. openpyxl
```
openpyxl
```
**Função**: Biblioteca para leitura e escrita de arquivos Excel (.xlsx)
**Uso no Projeto**:
- Leitura dos arquivos de dados de funcionários
- Geração do relatório final VR_Report.xlsx
- Suporte completo ao formato Excel moderno

### 5. pyautogen
```
pyautogen
```
**Função**: Framework para criação de agentes autônomos
**Uso no Projeto**: Suporte adicional para funcionalidades de agentes
**Características**:
- Agentes conversacionais
- Automação de tarefas complexas

### 6. dotenv (python-dotenv)
```
dotenv
```
**Função**: Carregamento de variáveis de ambiente de arquivos .env
**Uso no Projeto**: 
- Carregamento seguro da chave API da OpenAI
- Configuração de parâmetros do sistema
- Separação de configurações sensíveis do código

### 7. langchain_google_genai
```
langchain_google_genai
```
**Função**: Integração com modelos Google Generative AI via LangChain
**Uso no Projeto**: 
- Suporte alternativo para modelos Google (comentado no código)
- Flexibilidade na escolha de provedores de IA
- Integração com Gemini (se necessário)

## Instalação

### Método Padrão
```bash
pip install -r requirements.txt
```

### Instalação Individual
```bash
pip install crewai
pip install crewai_tools
pip install pandas
pip install openpyxl
pip install pyautogen
pip install python-dotenv
pip install langchain_google_genai
```

### Ambiente Virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Versões Compatíveis
O arquivo não especifica versões exatas, utilizando as versões mais recentes disponíveis. Para produção, recomenda-se fixar versões específicas:

```
crewai==0.25.0
pandas==2.1.4
openpyxl==3.1.2
python-dotenv==1.0.0
```

## Dependências do Sistema
Algumas bibliotecas podem requerer dependências do sistema operacional:
- **openpyxl**: Requer Python 3.7+
- **pandas**: Pode requerer compiladores C++ para instalação completa
- **crewai**: Requer Python 3.8+

## Uso no Projeto
Todas as dependências são utilizadas através dos módulos principais:
- **main.py**: Importa crewai, pandas, dotenv
- **agents.py**: Importa crewai, dotenv, langchain_google_genai  
- **tools/**: Utiliza crewai_tools como base para ferramentas customizadas

## Alternativas de Configuração
O projeto oferece flexibilidade na escolha de provedores de IA:
- **OpenAI GPT-4**: Configuração ativa
- **Google Gemini**: Configuração alternativa (comentada)

Para trocar entre provedores, ajuste o código em `agents.py` conforme necessário.