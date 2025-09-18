# main.py
import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# Importe as ferramentas que criamos
from tools import DataLoadTool, ConsolidateTool, CalculateVRTool, GenerateExcelTool

# Configure o modelo de linguagem. Use a API da OpenAI ou outra compatível.
# Lembre-se de configurar sua chave de API no ambiente.
# os.environ["OPENAI_API_KEY"] = "SUA_CHAVE_AQUI"
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Ou "gemini-pro" para uma opção mais rápida
    google_api_key=os.getenv("GOOGLE_API_KEY"), # Você pode passar a chave diretamente aqui também
    temperature=0.2 # Ajuste a criatividade do modelo (0.0 a 1.0)
)

# --- AGENTES ---

# 1. Agente para Carregar Dados
data_loader_agent = Agent(
    role='Especialista em Ingestão de Dados de RH',
    goal='Localizar e carregar de forma eficiente todos os arquivos de dados brutos (Excel) necessários para o cálculo da folha de VR.',
    backstory=(
        'Você é um agente de software meticuloso, especializado em lidar com fontes de dados de RH. '
        'Sua principal função é garantir que todos os dados iniciais sejam carregados corretamente para que o processo possa começar sem erros.'
    ),
    tools=[DataLoadTool()],
    llm=llm,
    verbose=True
)

# 2. Agente para Consolidar e Limpar Dados
data_consolidator_agent = Agent(
    role='Analista de Elegibilidade de Benefícios',
    goal='Unificar as diferentes bases de dados de funcionários e aplicar as regras de negócio para determinar quem é elegível para receber o vale-refeição.',
    backstory=(
        'Como um analista de RH digital, você é especialista em regras de negócio. Sua tarefa é cruzar informações de admissões, '
        'desligamentos, afastamentos e categorias (estágio, aprendiz) para criar uma lista mestra limpa e precisa de funcionários elegíveis.'
    ),
    tools=[ConsolidateTool()],
    llm=llm,
    verbose=True
)

# 3. Agente para Calcular o VR
vr_calculator_agent = Agent(
    role='Especialista em Processamento de Folha de Pagamento',
    goal='Executar o cálculo detalhado do valor do VR para cada funcionário elegível, considerando todas as variáveis como dias úteis, valor por sindicato, férias, admissões e desligamentos.',
    backstory=(
        'Você é o coração da operação de cálculo. Um especialista em lógica financeira e de folha de pagamento, '
        'sua responsabilidade é garantir que cada valor seja calculado com precisão, seguindo todas as regras complexas do processo.'
    ),
    tools=[CalculateVRTool()],
    llm=llm,
    verbose=True
)

# 4. Agente para Gerar o Relatório Final
report_generator_agent = Agent(
    role='Gerador de Relatórios Financeiros',
    goal='Formatar e gerar o arquivo Excel final com os resultados do cálculo do VR, em um formato claro e pronto para ser utilizado pelo departamento financeiro.',
    backstory=(
        'Com foco em precisão e apresentação, você transforma os dados numéricos finais em um relatório profissional e acionável. '
        'Sua tarefa finaliza o processo, entregando o resultado de todo o trabalho da equipe.'
    ),
    tools=[GenerateExcelTool()],
    llm=llm,
    verbose=True
)

# --- TAREFAS ---

# Tarefas são sequenciais, o resultado de uma é pré-requisito para a outra.
load_task = Task(
    description='Carregue todos os arquivos Excel de RH do diretório local usando a ferramenta apropriada.',
    expected_output='Uma confirmação de que todos os dados foram carregados com sucesso e estão prontos para a próxima etapa.',
    agent=data_loader_agent
)

consolidate_task = Task(
    description='Utilize os dados carregados na etapa anterior para consolidar a lista de funcionários e aplicar as regras de exclusão para determinar a elegibilidade ao VR.',
    expected_output='Uma mensagem de sucesso indicando quantos funcionários foram processados e quantos são elegíveis, com os dados prontos para o cálculo.',
    agent=data_consolidator_agent
)

calculate_task = Task(
    description='Com base na lista de funcionários elegíveis, execute o cálculo completo do vale-refeição para cada um, aplicando todas as regras de negócio de dias, valores e descontos.',
    expected_output='Um resumo confirmando que o cálculo foi finalizado e o valor total do benefício a ser pago no mês.',
    agent=vr_calculator_agent
)

report_task = Task(
    description='Pegue os dados finais calculados e gere o relatório final no formato Excel. O nome do arquivo deve ser "VR_MENSAL_05.2025_RESULTADO.xlsx".',
    expected_output='Uma confirmação final de que o arquivo Excel foi gerado e salvo com sucesso no diretório.',
    agent=report_generator_agent
)

# --- MONTAGEM DA CREW ---

vr_crew = Crew(
    agents=[data_loader_agent, data_consolidator_agent, vr_calculator_agent, report_generator_agent],
    tasks=[load_task, consolidate_task, calculate_task, report_task],
    process=Process.sequential,
    verbose=2
)

# --- EXECUÇÃO ---

if __name__ == '__main__':
    print("Iniciando a Crew de Cálculo de VR...")
    result = vr_crew.kickoff()
    print("\n\n--- Processo Finalizado ---")
    print(result)