# Desafio 4 VR - Sistema de Automação de Vale Refeição

Este projeto é um sistema automatizado para processamento de dados de Vale Refeição (VR) utilizando tecnologia de agentes de IA multiagentes com CrewAI. O sistema processa dados de funcionários de múltiplas fontes Excel e gera relatórios consolidados para operadoras de VR.

## Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **CrewAI** - Framework de agentes de IA colaborativos
- **Pandas** - Manipulação e análise de dados
- **OpenPyXL** - Manipulação de arquivos Excel
- **OpenAI GPT-4** - Modelo de linguagem para os agentes

## Estrutura do Projeto

```
desafio-4-vr/
├── data/                    # Arquivos de dados Excel
├── tools/                   # Ferramentas especializadas
├── agents.py               # Definição dos agentes de IA
├── tasks.py                # Definição das tarefas
├── main.py                 # Arquivo principal de execução
├── run_pipeline.py         # Script de pipeline
├── run_pipeline_debug.py   # Script de pipeline com debug
├── requirements.txt        # Dependências do projeto
└── .gitignore             # Exclusões do Git
```

## Funcionamento do Sistema

O sistema utiliza 7 agentes especializados que trabalham em sequência:

1. **Data Loader Agent** - Carrega dados dos arquivos Excel
2. **Consistency Agent** - Verifica e limpa inconsistências
3. **Data Consolidation Agent** - Consolida dados em um DataFrame único
4. **Exclusion Agent** - Aplica regras de exclusão de funcionários
5. **Validation Agent** - Valida e corrige dados
6. **Calculation Agent** - Calcula valores de VR
7. **Report Agent** - Gera relatório final em Excel

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/challenge-accepted-i2a2/desafio-4-vr
cd desafio-4-vr
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env com:
OPENAI_KEY_API=sua_chave_openai_aqui
```

## Uso

Execute o processamento completo:
```bash
python main.py
```

Ou use o pipeline:
```bash
python run_pipeline.py
```

Para debug:
```bash
python run_pipeline_debug.py
```

## Arquivos de Dados

O sistema processa os seguintes arquivos Excel da pasta `data/`:
- **ATIVOS.xlsx** - Funcionários ativos
- **DESLIGADOS.xlsx** - Funcionários desligados
- **FÉRIAS.xlsx** - Funcionários em férias
- **AFASTAMENTOS.xlsx** - Funcionários afastados
- **APRENDIZ.xlsx** - Funcionários aprendizes
- **ESTÁGIO.xlsx** - Estagiários
- **EXTERIOR.xlsx** - Funcionários no exterior
- **VRMENSAL05.2025.xlsx** - Dados mensais de VR
- **Basesindicatoxvalor.xlsx** - Base sindical x valores
- **Basediasuteis.xlsx** - Base de dias úteis
- **ADMISSÃOABRIL.xlsx** - Admissões de abril

## Saída

O sistema gera:
- **VR_Report.xlsx** - Relatório final para operadora de VR
- **VR_Report.csv** - Versão CSV do relatório
- Arquivos intermediários em formato pickle para cada etapa

## Contribuidores

- **Carlos Jorge** (cacjorge)
- **Kattson Bastos** (KattsonBastos)
- **Letícia Ferreira Murça** (leticiaferreiramurca)

## Licença

Este projeto é parte do Desafio 4 da iniciativa I2A2.