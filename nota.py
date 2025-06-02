import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do Excel
file_path = "nota.xlsx"
df_alunos = pd.read_excel(file_path, sheet_name="base_alunos")
df_desempenho = pd.read_excel(file_path, sheet_name="desempenho_academico")
df_participacao = pd.read_excel(file_path, sheet_name="participacao")
df_risco = pd.read_excel(file_path, sheet_name="risco_final")

# ======= Desempenho Acadêmico por Curso =======
desempenho_curso = pd.merge(df_desempenho, df_alunos[['ID_Aluno', 'Curso']], on='ID_Aluno')
media_por_curso = desempenho_curso.groupby('Curso')['Média'].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=media_por_curso.values, y=media_por_curso.index, palette='Blues_r')
plt.title('Média de Desempenho Acadêmico por Curso')
plt.xlabel('Média Geral')
plt.ylabel('Curso')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ======= Participação em Atividades por Curso =======
df_participacao["Total Participações"] = (
    df_participacao["Participações em Fórum"]
    + df_participacao["Entregas no Prazo"]
    + df_participacao["Projetos em Grupo"]
    + df_participacao["Apresentações"].map({"Sim": 1, "Não": 0})
)

participacao_curso = pd.merge(df_participacao, df_alunos[['ID_Aluno', 'Curso']], on='ID_Aluno')
media_participacao = participacao_curso.groupby('Curso')["Total Participações"].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=media_participacao.values, y=media_participacao.index, palette='Greens')
plt.title('Média de Participação em Atividades por Curso')
plt.xlabel('Total Médio de Participações')
plt.ylabel('Curso')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ======= Faltas por Curso =======
faltas_curso = desempenho_curso.groupby('Curso')["Faltas (%)"].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=faltas_curso.values, y=faltas_curso.index, palette='Reds')
plt.title('Média de Faltas (%) por Curso')
plt.xlabel('Faltas (%)')
plt.ylabel('Curso')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ======= Risco Acadêmico por Curso =======
risco_merged = pd.merge(df_risco, df_alunos[['ID_Aluno', 'Curso']], on='ID_Aluno')
risco_por_curso = risco_merged.groupby(['Curso', 'Risco Acadêmico']).size().unstack(fill_value=0)

risco_por_curso.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='coolwarm')
plt.title('Distribuição de Risco Acadêmico por Curso')
plt.xlabel('Curso')
plt.ylabel('Número de Alunos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
