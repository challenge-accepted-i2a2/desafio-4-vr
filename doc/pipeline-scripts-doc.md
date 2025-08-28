# run_pipeline.py e run_pipeline_debug.py - Scripts de Pipeline

## Descrição Geral
Os arquivos `run_pipeline.py` e `run_pipeline_debug.py` são scripts auxiliares que executam o pipeline de processamento de Vale Refeição definido no projeto. Eles diferem apenas no nível de verbosidade e na configuração de debug.

## Arquivo: run_pipeline.py

### Objetivo
Executar o pipeline completo de forma simplificada, sem logs extensivos de debug.

### Funcionalidades Principais
1. Importa os módulos necessários (`main`, `os`)
2. Define ou ajusta variáveis de ambiente, se necessário
3. Dispara a execução do pipeline chamando `main.py`
4. Exibe mensagem final de sucesso ou erro

### Fluxo de Execução
```python
import os
from main import main  # Assume que main.py possui função main()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro na execução do pipeline: {e}")
```

### Parâmetros
- **N/A** (utiliza configurações padrão de `main.py`)

### Uso
```bash
python run_pipeline.py
```

## Arquivo: run_pipeline_debug.py

### Objetivo
Executar o pipeline com nível de log detalhado para fins de diagnóstico.

### Funcionalidades Principais
1. Ativa variáveis de debug (por exemplo, `DEBUG=True`)
2. Importa `main.py` e executa o processo
3. Gera logs detalhados em console ou arquivo

### Fluxo de Execução
```python
import os
from main import main

os.environ["DEBUG"] = "1"

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro no debug do pipeline: {e}")
```

### Parâmetros/Opcões de Debug
- `DEBUG` - Variável de ambiente para habilitar logs detalhados

### Uso
```bash
python run_pipeline_debug.py
```

## Diferenças entre os Scripts
| Aspecto | run_pipeline.py | run_pipeline_debug.py |
|---------|-----------------|-----------------------|
| Verbosidade de Log | Baixa | Alta (debug) |
| Variáveis de Ambiente | Padrão | `DEBUG=1` |
| Público-alvo | Execução diária em produção | Diagnóstico, testes |

## Dependências
- `main.py` - Script principal do sistema

## Boas Práticas
- Utilize `run_pipeline_debug.py` apenas em ambientes de teste
- Para produção, utilize `run_pipeline.py` para minimizar logs

## Extensões Futuras
- Adicionar parâmetros CLI para selecionar etapas específicas
- Integrar com sistemas de agendamento (Cron, Airflow)
