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
├── requirements.txt         # Dependências do projeto
├── .gitignore               # Exclusões do Git
└── src/                     # diretório principal com a implementação
    ├── aux_functions.py     # funções auxiliares usadas pelso agentes
    ├── data/                # Arquivos de dados Excel
    ├── main.py              # Arquivo principal de execução com os agentes
    ├── outputs/             # Diretório para armazenar arquivos de resultados
    └── tools.py             # Ferramentas especializadas
```

## Funcionamento do Sistema

O sistema utiliza 4 agentes especializados que trabalham em sequência:

1. **Data Loader Agent** - Carrega dados dos arquivos Excel
2. **Data Consolidation Agent** - Consolida dados em um DataFrame único
3. **Calculation Agent** - Calcula valores de VR
4. **Report Agent** - Gera relatório final em Excel

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
GOOGLE_API_KEY=sua_chave_aqui
```

## Uso

Execute o processamento completo:
```bash
python main.py
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
- **VR MENSAL 05.2025.xlsx** - Dados mensais de VR
- **Basesindicatoxvalor.xlsx** - Base sindical x valores
- **Basediasuteis.xlsx** - Base de dias úteis
- **ADMISSÃOABRIL.xlsx** - Admissões de abril

## Saída

O sistema gera:
- **VR MENSAL 05.2025.xlsx** - Relatório final para operadora de VR

## Contribuidores

- **Carlos Antônio Campos Jorge**
- **Claudio Fagundes Pereira**
- **David de Freitas Neto**
- **Filipe do Rego Barros Luz**
- **Kattson Alves Bastos**
- **Letícia Ferreira Murça Reis**
- **Raphael Vinholes Bichiarov**
- **Renato Azevedo Sant’Anna**
- **Thayron Sabino Alves dos Santos**

## Licença

Este projeto é parte do Desafio 4 da iniciativa I2A2.
