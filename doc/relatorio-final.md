# Relatório Técnico Completo - Desafio 4 VR

**Versão:** 1.0  
**Data:** 27/08/2025  
**Autores:** Carlos Jorge, Kattson Bastos, Letícia Ferreira Murça

---

## Sumário
1. Introdução
2. Visão Geral do Projeto
3. Estrutura do Repositório
4. Documentação de Arquivos
    1. Arquivos Raiz
    2. Pasta `tools/`
    3. Pasta `data/`
5. Pipeline de Processamento
6. Instruções de Instalação e Uso
7. Requisitos de Ambiente
8. Conclusão e Próximos Passos

---

## 1. Introdução
Este relatório documenta o sistema de automação de Vale Refeição (VR) desenvolvido para o **Desafio 4** da iniciativa I2A2. O sistema utiliza tecnologia de agentes de IA (CrewAI) para processar dados de funcionários e gerar relatórios para operadoras de VR.

## 2. Visão Geral do Projeto
- **Linguagem:** Python 3.x  
- **Framework de Agentes:** CrewAI  
- **Manipulação de Dados:** Pandas, OpenPyXL  
- **IA:** OpenAI GPT-4  
- **Entrada:** 11 arquivos Excel na pasta `data/`  
- **Saída:** `VR_Report.xlsx` (relatório final)  

## 3. Estrutura do Repositório
```
desafio-4-vr/
├── data/                      # Arquivos Excel de entrada
├── tools/                     # Ferramentas especializadas
├── .gitignore
├── agents.py
├── main.py
├── tasks.py
├── run_pipeline.py
├── run_pipeline_debug.py
├── requirements.txt
└── docs/                      # (gerado) Documentação Markdown
```

Todos os arquivos de documentação em Markdown encontram-se na pasta **docs/** e podem ser convertidos para Word ou PDF usando Pandoc ou ferramentas equivalentes.

## 4. Documentação de Arquivos
A tabela abaixo lista cada arquivo do repositório e sua respectiva função. Para detalhes completos, consulte os arquivos Markdown individuais localizados em `docs/`.

| Caminho | Descrição | Doc Markdown |
|---------|-----------|--------------|
| `README.md` | Visão geral do projeto | `README.md` |
| `main.py` | Ponto de entrada do pipeline de agentes | `main-py-doc.md` |
| `agents.py` | Definição dos 7 agentes de IA | `agents-py-doc.md` |
| `tasks.py` | Definição das tarefas do pipeline | `tasks-py-doc.md` |
| `run_pipeline.py` | Execução simplificada do pipeline | `pipeline-scripts-doc.md` |
| `run_pipeline_debug.py` | Execução em modo debug | `pipeline-scripts-doc.md` |
| `requirements.txt` | Dependências do projeto | `requirements-doc.md` |
| `.gitignore` | Padrões de exclusão do Git | (doc embutida) |
| `tools/` | Ferramentas especializadas | `tools-folder-doc.md` |
| `data/` | Arquivos Excel de entrada | (descrição em `tools-folder-doc.md`) |

### 4.1 Arquivos Raiz
Detalhamento completo nos documentos `README.md`, `main-py-doc.md`, `agents-py-doc.md`, `tasks-py-doc.md` e `pipeline-scripts-doc.md`.

### 4.2 Pasta `tools/`
Contém 8 arquivos Python, cada um implementando parte do processamento (carregamento, consistência, consolidação, exclusões, validação, cálculo e relatório). Veja `tools-folder-doc.md` para detalhes.

### 4.3 Pasta `data/`
Armazena 11 planilhas Excel e arquivos gerados (`*.pkl`, `VR_Report.xlsx`). A documentação das operações sobre estes arquivos encontra-se em `tools-folder-doc.md`.

## 5. Pipeline de Processamento
O pipeline é executado em 7 etapas sequenciais:
1. **Load Data**  
2. **Consistency Check**  
3. **Data Consolidation**  
4. **Apply Exclusion Rules**  
5. **Validation**  
6. **Calculation of VR**  
7. **Report Generation**  

Cada etapa gera um arquivo pickle intermediário, garantindo rastreabilidade total.

## 6. Instruções de Instalação e Uso
1. Clone o repositório e instale as dependências:  
```bash
git clone https://github.com/challenge-accepted-i2a2/desafio-4-vr
cd desafio-4-vr
pip install -r requirements.txt
```
2. Configure a variável de ambiente `OPENAI_KEY_API` em um arquivo `.env`.
3. Execute o pipeline:  
```bash
python main.py
```

## 7. Requisitos de Ambiente
- Python 3.8+  
- Pandoc (para converter Markdown → Word/PDF)  
- Dependências do arquivo `requirements.txt`

## 8. Conclusão e Próximos Passos
O sistema está pronto para uso em ambientes de produção e pode ser estendido para:
- Suporte a novos tipos de benefícios (VT, VA)
- Integração com APIs de RH
- Dashboard web em tempo real

---

### Conversão para Word/PDF
Para gerar o documento final em Word:
```bash
pandoc relatorio-final.md -o relatorio-final.docx
```
Para gerar em PDF:
```bash
pandoc relatorio-final.md -o relatorio-final.pdf
```

Fim do Relatório.