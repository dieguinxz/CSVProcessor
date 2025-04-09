import os  
import pandas as pd  


# Listar os arquivos na pasta
lista_arquivos = os.listdir(r"d:\vscode\pYTHON\Projeto de vendas\Vendas")
print(lista_arquivos)

# Criar um DataFrame vazio
tabela_total = pd.DataFrame()

# Importar bases de dados de vendas
for arquivo in lista_arquivos:   
    caminho_arquivo = f"d:/vscode/pYTHON/Projeto de vendas/Vendas/{ arquivo}"
    print(caminho_arquivo)
    
    # Importa o arquivo
    tabela = pd.read_csv(caminho_arquivo)

    # Adiciona os dados ao DataFrame total
    tabela_total = pd.concat([tabela_total, tabela])

print(tabela_total)


#calcular o produto mais vendido
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Preco Unitario", "Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

#.sort_values(serve para ordenar os valores, e dentro do () vc diz pra ele duas informacao que o By= e o nome da coluna)
#groupby, ela e para agrupar uma coluna que vc escolhe, dps vc diz para ele o que ele deve fazer, que e Sum(serve para somar todos os produtos da tabela que vc escolher)

# Criar a coluna de faturamento antes de agrupar
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

# Agrupar por Produto e somar os valores relevantes
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)


# Exibir a tabela
print(tabela_faturamento)
  

#Calcular a loja/ cidade que mais vendeu (em faturamento) - criar um grafico/dashboard

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)
 