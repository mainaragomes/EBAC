
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê os dados do arquivo CSV para um DataFrame
df = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha com Seaborn
sns.lineplot(x='dia', y='venda', data=df)

# Salva o gráfico como uma imagem PNG
plt.savefig('gasolina.png')
