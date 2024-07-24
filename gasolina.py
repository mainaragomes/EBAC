
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')

# Definir o estilo e tamanho do gráfico
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plotar o gráfico de linha
sns.lineplot(data=df, x='dia', y='venda', marker='o', color='b', linewidth=2.5)

# Adicionar título e rótulos dos eixos
plt.title('Preço da Gasolina ao Longo dos Dias', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço (R$)', fontsize=14)

# Adicionar legenda
plt.legend(['Preço da Gasolina'], loc='best')

# Salvar o gráfico como arquivo PNG
plt.savefig('gasolina.png')

# Mostrar o gráfico
plt.show()
    