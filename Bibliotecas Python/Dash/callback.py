from dash import Dash, html, dcc, Input, Output
from plotly.express import line
from pandas import DataFrame
from numpy import arange


#------------------------------------------------------------------------
# Dados Iniciais
x = arange(0.0, 2.0, 0.01)
y1 = x**2 - 0.5
y2 = 2*x - 1

dicionario = {'Valores de x': x, 'Y_1': y1, 'Y_2': y2}

df = DataFrame(dicionario)

#-------------------------------------------------------------------------
# Estrutura do painel

app = Dash(__name__)

app.layout = html.Div(children = [
                html.H1('Callback Básica'),

                html.Div('Selecione a função'),

                html.Br(),

                dcc.Dropdown(id = 'botao',
                             options = ['f(x) = x² - 0.5', 'f(x) = 2x -1'],
                             value = 'f(x) = x² - 0.5'),

                dcc.Graph(id = 'grafico',
                          figure = {})

])

@app.callback(
    Output(component_id = 'grafico', component_property = 'figure'),
    Input(component_id = 'botao', component_property = 'value')
)
def FuncaoAtualizadora(nome):

    if nome == 'f(x) = x² - 0.5':
        eixoY = 'Y_1'
    else:
        eixoY = 'Y_2'

    figura = line(data_frame = df,
                  x = 'Valores de x',
                  y = eixoY)

    return figura


if __name__ == '__main__':
    app.run_server(debug = True)
