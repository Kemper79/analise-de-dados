import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conexao = sqlite3.connect('dados_vrndas.db')
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas1(
    id_vendas INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

cursor.execute("""
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda)VALUES
    ('2023-01-01', 'Produto A', 'Eletronicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletronicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletronicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletronicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletronicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletronicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
""")
conexao.commit()

df_vendas = pd.read_sql_query('SELECT * FROM vendas1', conexao)
print(df_vendas)

print('\n============== ANALISANDO OS DADOS ==============')

total_vendas = df_vendas['valor_venda'].sum()
print(f'Total de vendas: R$ {total_vendas:.2f}')

media_vendas = df_vendas['valor_venda'].mean()
print(f'Media das vendas: R$ {media_vendas:.2f}')

vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum()
print('\nVenda por categoria')
print(vendas_categoria)

maior_venda = df_vendas.loc[df_vendas['valor_venda'].idxmax()]
print('\nProduto com maior venda')
print(maior_venda)

quantidade_categoria = df_vendas['categoria'].value_counts()
print('\nQuantidade de vendas por categoria')
print(quantidade_categoria)

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes'] = df_vendas['data_venda'].dt.month
vendas_mes = df_vendas.groupby('mes')['valor_venda'].sum()
print('\nVendas por mes')
print(vendas_mes)

# GRAFICO DE VENDAS POR CATEGORIA

plt.figure(figsize=(8, 5))

sns.barplot(
    x = vendas_categoria.index,
    y = vendas_categoria.values
)

plt.title('Vendas por categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor das vendas')

plt.show()

# GRAFICO DE VENDAS POR MES

plt.figure(figsize=(10, 5))

sns.barplot(
    x = vendas_mes.index,
    y = vendas_mes.values
)

plt.title('Vendas por mes')
plt.xlabel('Mes')
plt.ylabel('Valor das vendas')

plt.show()





