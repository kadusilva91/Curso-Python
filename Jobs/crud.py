# dashboard

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('Vendas.xlsx')

# criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o Faturamento de Todas as Lojas'),
    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
