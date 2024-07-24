Projeto de Gasolina, módulo 18 EBAC

## Introdução
Este projeto é destinado a demonstrar como formar um gráfico de linha a partir de um arquivo csv, considerando os custos da gasolina durante os 10 primeiros dias de julho de 2021.

## Passos:

1. Escrever o arquivo csv
2. Gerar o gráfico
3. Salvar o gráfico como imagem png

## Código
# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.lineplot(x='dia', y='venda', data=df)
plt.savefig('gasolina.png')

# Salva o código como um arquivo Python
with open('gasolina.py', 'w', encoding='utf-8') as f:
    f.write('''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê os dados do arquivo CSV para um DataFrame
df = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha com Seaborn
sns.lineplot(x='dia', y='venda', data=df)

# Salva o gráfico como uma imagem PNG
plt.savefig('gasolina.png')
''')
