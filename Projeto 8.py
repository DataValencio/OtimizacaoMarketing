#!/usr/bin/env python
# coding: utf-8

# <div>
# Olá, Valencio!
# 
# Meu nome é Luiz. Fico feliz em revisar seu projeto. Ao longo do texto farei algumas observações sobre melhorias no código e também farei comentários sobre suas percepções sobre o assunto. Estarei aberto a feedbacks e discussões sobre o tema.
# 
# **Peço que mantenha e não altere os comentários que eu fizer por aqui para que possamos nos localizar posteriormente, ok?**
# 
# Mais uma coisa, vamos utilizar um código de cores para você entender o meu feedback no seu notebook. Funciona assim:
# 
# <div class="alert alert-block alert-success">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
# 
# Sucesso. Tudo foi feito corretamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentário do revisor: </b> <a class="tocSkip"></a>
# 
# Alerta não crítico, mas que pode ser corrigido para melhoria geral no seu código/análise.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentário do revisor: </b> <a class="tocSkip"></a>
#     
# Erro que precisa ser arrumado, caso contrário seu projeto **não** será aceito.
# </div>
# 
# Você pode interagir comigo através dessa célula:
# <div class="alert alert-block alert-info">
# <b>Resposta do Aluno.</b> <a class="tocSkip"></a>
# </div>

# <div class="alert alert-block alert-danger">
# <b> Comentário geral do revisor v1</b> <a class="tocSkip"></a>
# <s>
#     
# Obrigado por enviar o seu projeto e pelo esforço de chegar até aqui. O seu projeto possui alguns pontos bem interessantes, dos quais eu destaco:
#     
# - Código bem simples e estruturado 
# - Comentários sucintos e bem objetivos
# - Conclusões pertinentes em cada análise e etapa de avaliação
#    
# <br>
# Entretanto, deixei alguns comentários em alguns trechos que precisam de ajuste. Peço que trabalhe nesses pontos para avançarmos.
#     
# <br>
#     
# Qualquer dúvida, pode contar comigo.   
#     
#     
# **Até breve!**
# </s>
# </div>

# <div class="alert alert-block alert-success">
# <b> Comentário geral do revisor</b> <a class="tocSkip"></a>
# 
# Obrigado por enviar o seu projeto e fazer os ajustes sugeridos. Essa versão do seu trabalho ficou muito melhor! Espero que as sugestões sejam relevantes para projetos futuros.
#     
# <br>
# Te desejo uma jornada de muito sucesso e aprendizado.
#     
# <br>   
#     
# Qualquer dúvida, pode contar comigo.   
#     
# <br>  
#     
# **Até breve!**
# 
# </div>

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[31]:


visitas = pd.read_csv('/datasets/visits_log_us.csv')
pedidos = pd.read_csv('/datasets/orders_log_us.csv')
custos = pd.read_csv('/datasets/costs_us.csv')
print(visitas)
visitas.info()


# <div class="alert alert-block alert-success">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
#     
# - O import das bibliotecas foi feito de forma correta e em uma célula separada
# - Os dados foram carregados corretamente
# </div>

# In[32]:


print(pedidos)
pedidos.info()


# In[33]:


print(custos)
custos.info()


# <div class="alert alert-block alert-warning">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
#     
# - O método `info()` foi utilizado para estudo inicial do conjunto de dados
# - O método `head()` poderia ser utilizado para exibir uma amostra inicial dos seus dados. Dica: evite imprimir todo o dataframe, uma vez que o conjunto de dados pode ser grande. Neste caso, sempre opte por usar métodos como `head()` ou `sample()`
# </div>

# Demos uma olhada geral no tipo de dados. Agora vamos verificar se há valores ausentes e nulos.

# In[34]:


print(visitas.isna().sum())
print("\nvalores ausentes: ")
print("\n",visitas.isnull().sum())


# In[35]:


print(pedidos.isna().sum())
print("\nvalores ausentes: ")
print(pedidos.isnull().sum())


# In[36]:


print(custos.isna().sum())
print("\nvalores ausentes: ")
print(custos.isnull().sum())


# Não encontramos nenhum tipo de valor ausente ou nulo nos DF. Podemos continuar com nossa analise exploratoria.

# Vamos remover os espaços das colunas, e deixa-los com as iniciais minusculas para facilitar futuramente nossa analise.

# In[37]:


pedidos.columns = pedidos.columns.str.replace(' ', '_').str.lower()
visitas.columns = visitas.columns.str.replace(' ', '_').str.lower()


# Vamos alterar o tipo de dados das colunas que contenham as data e hora, e mudar o tipo de dado das colunas identificadoras dos usuarios.

# In[38]:


visitas['end_ts'] = pd.to_datetime(visitas['end_ts'])
visitas['start_ts'] = pd.to_datetime(visitas['start_ts'])
pedidos['buy_ts'] = pd.to_datetime(pedidos['buy_ts'])
custos['dt'] = pd.to_datetime(custos['dt'])


# In[39]:


visitas['uid'] = visitas['uid'].astype(object)
pedidos['uid'] = pedidos['uid'].astype(object)
custos['source_id'] = custos['source_id'].astype(object)


# In[40]:


visitas


# In[41]:


pedidos


# In[42]:


custos


# <div class="alert alert-block alert-success">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
#     
# - Os valores ausentes foram estudados
# - Os dados foram convertidos para os tipos corretos. Além disso, as colunas foram renomeadas para seguir a convenção `snake_case`
# 
# </div>

# # Passo 2. Faça relatórios e calcule as métricas:

# # Quantas pessoas usam-no cada dia, semana e mês?

# In[43]:


usuarios_diarios = visitas.groupby(visitas['start_ts'].dt.date)['uid'].nunique()
print("Usuários únicos por dia:")
print(usuarios_diarios.head(10))


# ### Por dia: 
# Os números diários variam na casa das centenas. A flutuação indica picos em alguns dias (como em 2017-06-08, com 868 usuários) e quedas em outros (350 em 2017-06-10), possivelmente refletindo fatores sazonais ou padrões de uso ao longo da semana.

# In[44]:


usuarios_semanais = visitas.groupby(visitas['start_ts'].dt.to_period('W'))['uid'].nunique()
print("\nUsuários únicos por semana:")
print(usuarios_semanais.head(10))


# ### Por semana: 
# A contagem semanal está na casa dos milhares. Observa-se um crescimento de 2021 na última semana de maio/início de junho para 4355 em meados de julho, sugerindo que, ao longo das semanas iniciais, mais usuários passaram a acessar.

# In[45]:


usuarios_mensais = visitas.groupby(visitas['start_ts'].dt.to_period('M'))['uid'].nunique()
print("\nUsuários únicos por mês:")
print(usuarios_mensais.head(10))


# ### Por mês: 
# É onde vemos o padrão mais claro de evolução:
# 
# Junho/2017: 13 mil usuários.
# Julho/2017: 14 mil.
# Queda em agosto (11 mil), seguida de uma forte subida em setembro (18 mil) e um pico em novembro (32 mil).
# Em dezembro/2017 (31 mil) e nos meses de 2018, há uma leve redução, mas ainda permanecendo em patamares altos (27 a 28 mil).

# # Quantas sessões ocorrem por dia? (um usuário pode realizar várias sessões).

# In[46]:


sessoes_diarias = visitas.groupby(visitas['start_ts'].dt.date).size()
print("Sessões por dia:")
print(sessoes_diarias.head(10))


# ### Sessões por dia:
# 
# Os valores diários (variando de 375 a 939) mostram quantas sessões ocorreram em cada data. Há variações significativas entre os dias — em alguns, há mais de 900 sessões, enquanto em outros o número fica em torno de 400.

# # Que comprimento tem cada sessão?

# In[47]:


visitas['duracao_sessao'] = visitas['start_ts'] - visitas['end_ts']

print(visitas[['start_ts', 'end_ts', 'duracao_sessao']].head(10))


# ### Comprimento de cada sessão
# 
# Alguns registros têm duração zero (0 days 00:00:00), sugerindo sessões instantâneas. No geral, as sessões parecem relativamente curtas (em torno de alguns minutos a, no máximo, algumas dezenas de minutos).

# # Com que frequência os usuários voltam?

# In[48]:


visitas_ordenadas = visitas.sort_values(['uid', 'start_ts'])
visitas_ordenadas['intervalo_retorno'] = visitas_ordenadas.groupby('uid')['start_ts'].diff()
print(visitas_ordenadas[['uid', 'start_ts', 'intervalo_retorno']].head(20))


# In[ ]:


estatisticas_intervalo = visitas_ordenadas['intervalo_retorno'].dropna().describe()
# Frequência de retorno dos usuários 
print(estatisticas_intervalo)


# ### Frequência de retorno dos usuários
# 
# Podemos concluir que, em média, os usuários retornam após cerca de 28 dias, mas há grande variabilidade – alguns retornam em poucas horas (ou no mesmo dia) e outros podem demorar quase um ano.

# ---

# # Quando as pessoas começam a comprar? (Na análise de KPIs, nós geralmente estamos interessados em saber o período de tempo entre o registro e a conversão - quando o usuário se torna um cliente. Por exemplo, se o registro e a primeira compra de um usuário ocorrem no mesmo dia, ele pode encaixar na categoria de Conversão 0d. Se a compra é realizada no dia seguinte, isso será a Conversão 1d. Você pode usar qualquer abordagem que permita comparar as conversões de diferentes coortes, para que você possa determinar qual coorte ou canal de marketing tem a maior eficiência)

# In[ ]:


# 1. Obter a data de registro de cada usuário (primeiro acesso)
registros = visitas.groupby('uid')['start_ts'].min().reset_index()
registros.rename(columns={'start_ts': 'registro_ts'}, inplace=True)

# 2. Obter a data da primeira compra de cada usuário
compras = pedidos.groupby('uid')['buy_ts'].min().reset_index()
compras.rename(columns={'buy_ts': 'primeira_compra_ts'}, inplace=True)

# 3. Unir os DataFrames de registros e compras (apenas usuários que realizaram compra)
conversoes = pd.merge(registros, compras, on='uid', how='inner')

# 4. Calcular a diferença em dias entre o registro e a primeira compra
conversoes['diferenca_dias'] = (conversoes['primeira_compra_ts'] - conversoes['registro_ts']).dt.days

# 5. Classificar a conversão em categorias (ex.: "0d", "1d", etc.)
conversoes['categoria_conversao'] = conversoes['diferenca_dias'].astype(str) + 'd'

resumo_conversoes = conversoes['categoria_conversao'].value_counts().sort_index()
print("\nResumo de conversões:")
print(resumo_conversoes.head(50))


# In[ ]:


plt.figure(figsize=(10, 6))
sns.histplot(conversoes['diferenca_dias'], bins=10, kde=False, color='skyblue')
plt.xlabel('Dias para conversão')
plt.ylabel('Número de usuários')
plt.title('Distribuição do tempo até a primeira compra')
plt.show()


# <div class="alert alert-block alert-success">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
#     
# - O intervalo até a primeira compra foi analisado
# - A distribuição dos dados foi plotada em um histograma
# </div>

# ### conversão
# 
# Conversão 0d: O maior volume de usuários (26.363) faz a primeira compra no mesmo dia em que se registra. Isso sugere que uma parcela significativa dos usuários toma a decisão de comprar imediatamente, indicando um processo de aquisição e conversão bem otimizado para essa fatia de clientes.
# 
# Conversão em 1–10 dias: Há registros como “10d = 140”. Esses números demonstram que, embora a maioria compre no mesmo dia, ainda há um grupo considerável que precisa de alguns dias para decidir.
# 
# Conversões acima de 100 dias: Embora os números (31, 23, 21 etc.) sejam relativamente pequenos se comparados ao pico de 0d, mostram que parte dos usuários só converte após vários meses. Isso pode representar clientes que precisaram de mais tempo para amadurecer a decisão de compra ou que foram impactados por outras campanhas de remarketing.

# # Quantos pedidos os clientes fazem durante um determinado período de tempo?

# In[ ]:


first_access = (
    visitas
    .groupby('uid')['start_ts']
    .min()
    .reset_index()
    .rename(columns={'start_ts': 'first_access'})
)
visitas['log_month'] = visitas['start_ts'].dt.to_period('M')

first_access['first_log_month'] = first_access['first_access'].dt.to_period('M')

visitas_coorte = pd.merge(
    visitas,
    first_access[['uid', 'first_log_month']],
    on='uid',
    how='left'
)

visitas_coorte['cohort_age'] = (
    visitas_coorte['log_month'].astype(int)
    - visitas_coorte['first_log_month'].astype(int)
)

cohort_data = (
    visitas_coorte
    .groupby(['first_log_month', 'cohort_age'])['uid']
    .nunique()
    .reset_index()
)

cohort_pivot = cohort_data.pivot(
    index='first_log_month',   
    columns='cohort_age',      
    values='uid'           
)

cohort_size = cohort_pivot[0]  
retention_matrix = cohort_pivot.divide(cohort_size, axis=0)

plt.figure(figsize=(12, 8))
sns.heatmap(
    retention_matrix,
    annot=True,
    fmt='.0%',
    cmap='YlGnBu'
)

plt.title('User Retention by Cohort')
plt.xlabel('Months Since First Login')
plt.ylabel('Cohort Month')
plt.yticks(rotation=0)
plt.show()


# <div class="alert alert-block alert-danger">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
# <s>
#     
# Aqui você precisa calcular a taxa de retenção dos usuários por cohort (análise: "com que frequência os usuários voltam?"). A rotina é a seguinte:
#     
# 1. Você precisa pegar a data do primeiro acesso de cada usuário
# 2. Para calcular o intervalo ou cohort de acesso para cada usuário, você precisa calcular o intervalo entre o acesso atual e o primeiro acesso:
#     
# ```python
# logs_first_log_month["cohort_age"] = logs_first_log_month["log_month"].astype(
#     int)- logs_first_log_month["first_log_month"].astype(int)
# ```
#  
# 3. A partir desses dados, você pode criar uma tabela dinâmica (`pivot_table`) que indexa por cada mês do conjunto de dados e calcula a quantidade de usuários que teve o primeiro acesso naquele mês e voltou a acessar no futuro (`cohort`): 1 mês depois, 2 meses depois, etc. 
# 4. A partir dessa tabela, você pode criar um gráfico de calor (`heatmap`), conforme sugestão abaixo.
# 
# ![image.png](attachment:image.png)
# </s>
# </div>

# ### Pedidos por dia/semana/mês
# 
# Dia/semana: Os valores variam de forma considerável (por dia, em torno de 60 a 160 pedidos; por semana, de 300 a quase 1000). Isso indica picos e vales que podem refletir ações pontuais de marketing, datas especiais ou padrões de consumo.
# 
# Mês: Nota-se um crescimento contínuo nos pedidos ao longo de 2017, com um pico em outubro de 2017 (5.679 pedidos). Essa tendência sugere que as campanhas (ou a adesão do público) foram mais fortes no final de 2017 e se mantendo no começo do ano de 2018.

# # Qual é o volume médio de uma compra?

# In[ ]:


volume_medio = pedidos['revenue'].mean()

print("Volume médio de uma compra:", volume_medio)


# ### Media de compra
# 
# Em média, cada pedido vale cerca de R$5. Esse valor pode indicar um ticket médio relativamente baixo (dependendo do modelo de negócio), mas se há alta recorrência de compras, ainda assim pode representar um bom volume de receita.

# <div class="alert alert-block alert-danger">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>    
# <s>
#     
# Aqui precisamos de pequenos ajustes no cálculo das métricas abaixo. Deixo como sugestão as etapas que você precisa executar para calcular as métricas de `LTV`, `CAC` e `ROI`. O dataframe gerado ao final pode ser usado para as duas tarefas.
# 
# <br> 
#    
#     
# **1. Calcule o primeiro pedido de cada usuário e extraia o mês.** 
# ```python
# first_orders_df = orders_df.groupby("..").agg({"Buy Ts": "min"}).reset_index().rename(columns={"Buy Ts": "first_purchase"})
# first_orders_df['first_purchase_month'] = first_orders_df['first_purchase'].dt.to_period("M")
# ```
# 
# **2. Faça o merge entre o primeiro pedido e os dados de source pelo `ID`.**
# ```pyhton
# user_source = visits_df[['..', 'Source Id']].drop_duplicates()
# first_orders_df = pd.merge(first_orders_df, user_source, on= '..')
# ```
# 
# **3. Calcule a receita mensal e faça o merge com a tabela criada anteriormente.**
# ```python
# revenue_df = orders_df.groupby(['Uid', 'month']).agg({'Revenue': 'sum'}).reset_index()
# buyers = first_orders_df.merge(revenue_df, on='Uid')
# ```
# 
# **4. Calcule a receita e os custos.**
# ```python
# revenue_grouped_df = buyers.groupby(['..', 'month']).agg({'Revenue': 'sum'}).reset_index()
# costs_grouped_df = costs_df.groupby(['..','month']).agg({'costs': 'sum'})
# ```
#     
# **5. Por fim, gere um dataframe por `source` e `month` com os dados de receita e custo.**
#     
#     
# ```python
# report = pd.merge(
#     costs_grouped_df, 
#     revenue_grouped_df, 
#     left_on=['...','month'], 
#     right_on=['...', 'month']
# )
# ```
# 
# O dataframe resultante dessas etapas é mostrado abaixo. Com esses dados, você consegue criar as métricas e executar as etapas restantes do seu projeto.
# ```
#       costs	month	Source Id	Revenue
# 0	1125.61	2017-06	  1	     2563.84
# 1	1072.88	2017-07	  1	     3947.25
# 2	951.81	2017-08	   1	     3325.64
# 3	1502.01	2017-09	  1	     8193.42
# 4	2315.75	2017-10	  1	     11466.14
# ```
# </s>
# </div>

# # Quanto dinheiro eles trazem para a empresa (LTV)?

# In[59]:


first_orders_df = (
    pedidos
    .groupby('uid', as_index=False)
    .agg({'buy_ts': 'min'})
    .rename(columns={'buy_ts': 'first_purchase'})
)

first_orders_df['first_purchase_month'] = first_orders_df['first_purchase'].dt.to_period('M')

user_source = visitas[['uid', 'source_id']].drop_duplicates()

first_orders_df = pd.merge(
    first_orders_df, 
    user_source, 
    on='uid',
    how='left'  
)

pedidos['month'] = pedidos['buy_ts'].dt.to_period('M')

revenue_df = (
    pedidos
    .groupby(['uid', 'month'], as_index=False)
    .agg({'revenue': 'sum'})
)

buyers = pd.merge(
    first_orders_df, 
    revenue_df, 
    on='uid',
    how='left'
)

revenue_grouped_df = (
    buyers
    .groupby(['source_id', 'month'], as_index=False)
    .agg({'revenue': 'sum'})
)


custos['dt'] = pd.to_datetime(custos['dt'])
custos['month'] = custos['dt'].dt.to_period('M')

costs_grouped_df = (
    custos
    .groupby(['source_id', 'month'], as_index=False)
    .agg({'costs': 'sum'})
)

report = pd.merge(
    costs_grouped_df,
    revenue_grouped_df,
    on=['source_id', 'month'],  
    how='outer'                 
).fillna(0)

print(report.head(10))


# In[60]:


first_orders_df['first_order_month'] = first_orders_df['first_purchase'].dt.to_period('M')

user_source = visitas[['uid', 'source_id']].drop_duplicates()
first_orders_df = pd.merge(
    first_orders_df,
    user_source,
    on='uid',
    how='left'
)
pedidos['buy_month'] = pedidos['buy_ts'].dt.to_period('M')

pedidos_coorte = pd.merge(
    pedidos,
    first_orders_df[['uid', 'first_order_month']],
    on='uid',
    how='left'
)
pedidos_coorte['age'] = (
    pedidos_coorte['buy_month'].astype(int)
    - pedidos_coorte['first_order_month'].astype(int)
)
cohort_ltv = (
    pedidos_coorte
    .groupby(['first_order_month', 'age'], as_index=False)
    .agg({'revenue': 'mean'})  # ou 'sum' se preferir
    .rename(columns={'revenue': 'ltv'})
)
output = cohort_ltv.pivot_table(
    index='first_order_month',
    columns='age',
    values='ltv',
    aggfunc='mean'  
)
output_cumsum = output.cumsum(axis=1).round(2).fillna('')

print(output_cumsum)


# In[ ]:


plt.figure(figsize=(10,6))
sns.heatmap(
    output_cumsum.replace('', 0).astype(float), 
    annot=True, 
    cmap='RdBu_r', 
    linewidths=1, 
    linecolor='black'
)
plt.title("LTV (acumulado) por Coorte")
plt.xlabel("Meses depois da primeira compra (age)")
plt.ylabel("Mês da primeira compra (coorte)")
plt.yticks(rotation=0)
plt.show()


# <div class="alert alert-block alert-danger">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
# <s>
#     
# Segue abaixo uma sugestão de como usar os dados da tabela acima para calcular o indicador de `LTV` por cohort:    
# ```python
# output = report.pivot_table(
#     index='first_order_month',
#     columns='age',
#     values='ltv',
#     aggfunc='mean'
# )
# output.cumsum(axis=1).round(2).fillna('')
# ```
#    
# Segue abaixo um exemplo do resultado esperado. Vale ressaltar que plotar o heatmap é opcional, mas deixa o resultado muito mais apresentável.
# 
# ![image.png](attachment:image.png)
# </s>
# </div>

# ---
# 
# # Quanto dinheiro foi gasto? no total/por origem/ao longo do tempo.

# In[ ]:


total_gasto = custos['costs'].sum()
gasto_por_origem = custos.groupby('source_id')['costs'].sum()
gasto_por_mes = custos.groupby(custos['dt'].dt.to_period('M'))['costs'].sum()

print("Total gasto:", total_gasto)
print()
print("\nGasto por origem:")
print(gasto_por_origem)
print("\nGasto por mês:")
print(gasto_por_mes)


# ### Gastos
# 
# Total: 329.131,62
# 
# Por origem: A maior parte do custo vem do source_id=3 (141.321,63) e source_id=4 (61.073,60), indicando que essas campanhas ou canais podem ter exigido mais investimentos.
# 
# Por mês: Há um crescimento nos gastos mês a mês de 2017-06 (18k) a 2017-12 (38k), seguido de um nível menor, porém ainda significativo, em 2018 (22k–33k).

# In[65]:


plt.figure(figsize=(10, 6))
gasto_por_mes.plot(kind='bar', color='skyblue')
plt.xlabel('Mês')
plt.ylabel('Valor total de gastos')
plt.title('Gastos por Mês')
plt.xticks(rotation=45)
plt.tight_layout()       

plt.show()


# # Quanto custou a aquisição de clientes para cada origem?

# In[66]:


primeiro_registro = visitas.sort_values('start_ts').groupby('uid').first().reset_index()
primeiro_registro = primeiro_registro[['uid', 'source_id']]

primeira_compra = pedidos.sort_values('buy_ts').groupby('uid').first().reset_index()
clientes_adquiridos = pd.merge(primeiro_registro, primeira_compra, on='uid', how='inner')

clientes_por_origem = clientes_adquiridos.groupby('source_id')['uid'].nunique()

gasto_por_origem = custos.groupby('source_id')['costs'].sum()

cpa_por_origem = gasto_por_origem / clientes_por_origem

print("Custos de aquisição de clientes (CPA) por origem:")
print(cpa_por_origem)


# # Os investimentos valeram a pena? (ROI)

# In[58]:


receita_por_origem = (
    pd.merge(pedidos, primeiro_registro[['uid', 'source_id']], on='uid', how='left')
    .groupby('source_id')['revenue']
    .sum()
)

# 2) Custos por origem (você já tem em 'gasto_por_origem')
# gasto_por_origem = custos.groupby('source_id')['costs'].sum()

# 3) Calcular ROI por origem
roi_por_origem = (receita_por_origem - gasto_por_origem) / gasto_por_origem

print("ROI por origem:")
print(roi_por_origem.head(20))


# In[61]:


coorte_size = (
    first_orders_df
    .groupby('first_order_month', as_index=False)
    .agg({'uid': 'nunique'})
    .rename(columns={'uid': 'new_users'})
)
custos['dt'] = pd.to_datetime(custos['dt'])
custos['cost_month'] = custos['dt'].dt.to_period('M')

cost_monthly = (
    custos
    .groupby('cost_month', as_index=False)
    .agg({'costs': 'sum'})
    .rename(columns={'cost_month': 'first_order_month', 'costs': 'total_cost'})
)
coorte_custo = pd.merge(
    coorte_size,
    cost_monthly,
    on='first_order_month',
    how='left'
).fillna({'total_cost': 0})

coorte_custo['cac'] = coorte_custo['total_cost'] / coorte_custo['new_users']


# In[62]:


ltv_matrix = output_cumsum.replace('', 0).astype(float).reset_index()

ltv_matrix = pd.merge(
    ltv_matrix,
    coorte_custo[['first_order_month','cac']],
    on='first_order_month',
    how='left'
).fillna({'cac': 0})


age_cols = [c for c in output.columns if isinstance(c, int)] '
for col in age_cols:
    romi_col = f'romi_{col}'
    ltv_matrix[romi_col] = ltv_matrix[col] / ltv_matrix['cac'] 



# In[63]:


romi_cols = [f'romi_{c}' for c in age_cols]
romi_df = ltv_matrix[['first_order_month'] + romi_cols].copy().set_index('first_order_month')

col_map = {f'romi_{c}': c for c in age_cols}
romi_df.rename(columns=col_map, inplace=True)

# Arredondar e exibir
romi_df = romi_df.round(2).fillna('')
print("=== ROMI POR COORTE ===")
print(romi_df)


# In[64]:


plt.figure(figsize=(10, 6))
sns.heatmap(
    romi_df.replace('', 0).astype(float),  # se houver strings vazias
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    linewidths=1,
    linecolor="black"
)
plt.title("ROMI por Coorte (LTV / CAC)")
plt.xlabel("Meses após a 1ª compra (age)")
plt.ylabel("Coorte (mês da 1ª compra)")
plt.yticks(rotation=0)
plt.show()


# ### ROI
# 
# A maior parte das coortes apresenta valores acima de 1 já nos primeiros meses (por exemplo, 2017-06 tem 1.14 no mês 1, 1.69 no mês 2 etc.), o que indica que, em média, cada R$1,00 investido já foi compensado e gerou retorno adicional.
# 
# ### Evolução ao Longo dos Meses:
# 
# - Coortes mais antigas (2017-06, 2017-07, 2017-09 etc.) têm mais meses para acumular receita, por isso seus valores chegam a patamares altos (≥ 5, ≥ 10).
# - Já as coortes recentes (2018-03, 2018-04, 2018-05) não tiveram tempo de “envelhecer”, então muitos campos ainda estão em 0 ou próximos de 1 no começo.
# 
# O ROI/ROMI das coortes está bastante positivo, mostrando que o investimento (CAC) costuma ser recuperado e superado em poucos meses.
# Coortes antigas (ex.: 2017-09) são especialmente lucrativas, sugerindo uma aquisição muito bem-sucedida nesse período.
# Coortes recentes não exibem tantos dados porque ainda estão nos primeiros meses de vida e não acumularam compras suficientes para dar um panorama completo de ROI.

# <div class="alert alert-block alert-danger">
# <b> Comentário do revisor: </b> <a class="tocSkip"></a>
# <s>
#     
# Aqui precisamos calcular o `ROI` / `ROMI` por cohort, pois os grupos podem ter valores diferentes de `LTV` e isso pode influenciar no resultado final. O cálculo da métrica pode ser feito como algo assim:
#     
# ```python
# your_agg_df['romi'] = your_agg_df['ltv'] / your_agg_df['cac']
# ```
# 
# O resultado pode ser apresentado como uma `pivot_table` por `cohort`, conforme você fez para outros indicadores em seu projeto. Adicionalmente, você pode analisar o `ROMI` por origem.
#     
# ```markdown
# |                   |      |    |    |   |   |   |   |   |   |   |    |    |
# |-------------------|------|----|----|---|---|---|---|---|---|---|----|----|
# | cohort            | 0    | 1  | 2  | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
# | first_order_month |      |    |    |   |   |   |   |   |   |   |    |    |
# | 2017-06           | 0.53 | .. | .. |   |   |   |   |   |   |   |    |    |
# | 2017-07           | 0.63 | .. |    |   |   |   |   |   |   |   |    |    |
# | 2017-08           | 0.49 | .. |    |   |   |   |   |   |   |   |    |    |
# | 2017-09           | 0.60 |    |    |   |   |   |   |   |   |   |    |    |
# | 2017-10           | 0.60 |    |    |   |   |   |   |   |   |   |    |    |
# | 2017-11           | 0.55 |    |    |   |   |   |   |   |   |   |    |    |
# | 2017-12           | 0.54 |    |    |   |   |   |   |   |   |   |    |    |
# | 2018-01           | 0.42 |    |    |   |   |   |   |   |   |   |    |    |
# | 2018-02           | 0.46 |    |    |   |   |   |   |   |   |   |    |    |
# | 2018-03           | 0.56 |    |    |   |   |   |   |   |   |   |    |    |
# | 2018-04           | 0.48 |    |    |   |   |   |   |   |   |   |    |    |
# | 2018-05           | 0.63 |    |    |   |   |   |   |   |   |   |    |    |
# ```
# 
#     
# ![image.png](attachment:image.png)
# </s>
# </div>

# --- 
# 
# # Conclusão e Recomendações de Investimento em Marketing

# ### Investir nos canais com melhor relação Custo x Retorno
# 
# - Observamos que a maior parcela de gastos está concentrada no source_id=3, seguida por source_id=4 e source_id=5. Esses canais representam a maior parte do custo, é imprescindível verificar se a receita (ou LTV dos usuários provenientes desses canais) justifica o investimento.
# 
# - Canais com custo menor, como source_id=9 e source_id=10, podem ser boas apostas se (e somente se) gerarem um volume razoável de conversões ou um LTV satisfatório. Um custo baixo, aliado a um volume de compras moderado, pode resultar em ROI positivo.

# ### Potencializar estratégias de Retenção
# 
# - O LTV médio (7) é relativamente baixo em relação ao custo total investido. Isso sugere que muitas aquisições não estão se pagando ao longo do tempo.
# 
# - Como muitas compras ocorrem no “0d”, é interessante reforçar ações de remarketing para tentar aumentar o número de compras subsequentes (aumentando o LTV). Quanto maior o LTV, maior a chance de compensar o custo de aquisição ao longo do ciclo de vida do cliente.

# ### Segmentar Campanhas por Perfil de Usuário
# 
# - Há usuários que retornam depois de meses para comprar novamente, e outros que fazem compras imediatas. Ajustar a comunicação conforme a janela de conversão típica desses segmentos pode melhorar a eficácia e o timing das campanhas.

# ### Recomendação Final
# 
# - Redirecionar orçamento para os canais ou plataformas que apresentem (ou possam apresentar) maior LTV e conversões rápidas, sustentadas por dados reais de receita por canal.
# 
# - Manter um acompanhamento constante de ROI por canal, fazendo testes e ajustes periódicos (testar novos canais de baixo custo, renegociar valores nos canais atuais de alto custo etc.).
# 
# - Investir em retenção (programas de fidelidade, notificações segmentadas, remarketing) para elevar o LTV dos clientes que já foram adquiridos, reduzindo a dependência de grandes gastos em aquisição.

# # Conlusão, foque nos canais que mostrem indícios de melhor equilíbrio entre custo e conversão e implemente estratégias de engajamento de longo prazo para aumentar o LTV. Assim, será possível reverter gradualmente o ROI negativo e tornar os investimentos em marketing mais sustentáveis.
