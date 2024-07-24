
import pandas as pd
import seaborn as sns

# Lê os dados do arquivo CSV para um DataFrame
conteudo = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha com Seaborn
with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=conteudo, x='dia', y='venda', palette='dark')
    grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel='Preço')
    grafico.figure.savefig('gasolina.png')
