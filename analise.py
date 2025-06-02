import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Configurações de estilo
sns.set(style="whitegrid")

# Carregar o arquivo Excel
file_path = 'analise.xlsx'  # Coloque o caminho correto se estiver em outra pasta
df = pd.read_excel(file_path, sheet_name='Plan1')

# Visualizar as primeiras linhas (opcional)
print(df.head())

# -------------------------------
# 1. Distribuição de casos por bairro
plt.figure(figsize=(10, 6))
bairro_counts = df['Bairro'].value_counts()
sns.barplot(x=bairro_counts.values, y=bairro_counts.index, palette='viridis')
plt.title('Distribuição de Casos de Dengue por Bairro')
plt.xlabel('Número de Casos')
plt.ylabel('Bairro')
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Distribuição por faixa etária e gênero
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Idade', hue='Gênero', multiple='stack', bins=10, palette='Set2')
plt.title('Distribuição de Casos por Faixa Etária e Gênero')
plt.xlabel('Idade')
plt.ylabel('Número de Casos')
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Localização geográfica dos focos (por bairro)

# Como não temos coordenadas geográficas, vamos simular usando bairros
plt.figure(figsize=(10, 6))
bairro_counts = df['Bairro'].value_counts()
sns.barplot(x=bairro_counts.index, y=bairro_counts.values, palette='coolwarm')
plt.xticks(rotation=45)
plt.title('Focos de Dengue por Bairro (Simulação Geográfica)')
plt.xlabel('Bairro')
plt.ylabel('Número de Casos')
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Análise por datas de notificação
df['Data da Notificação'] = pd.to_datetime(df['Data da Notificação'])

plt.figure(figsize=(10, 6))
data_counts = df['Data da Notificação'].value_counts().sort_index()
sns.lineplot(x=data_counts.index, y=data_counts.values, marker='o')
plt.title('Casos de Dengue por Data de Notificação')
plt.xlabel('Data')
plt.ylabel('Número de Casos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Identificação de áreas críticas

# Considerando como áreas críticas os bairros com mais casos
top_bairros = bairro_counts.head(5)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_bairros.values, y=top_bairros.index, palette='Reds_r')
plt.title('Top 5 Áreas Críticas - Dengue')
plt.xlabel('Número de Casos')
plt.ylabel('Bairro')
plt.tight_layout()
plt.show()