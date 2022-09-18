from pandas import DataFrame
from plotly.express import bar
from dash import Dash, html, dcc

dicionario = {"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
              "Amount": [4, 1, 2, 2, 4, 5],
              "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]}

df = DataFrame(dicionario) 


figura = bar(df, x = 'Fruit', y = 'Amount', color="City", barmode="group")


app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='Dash: A web application framework for your data.'),

    dcc.Graph(figure=figura)
])

if __name__ == '__main__':
    app.run_server(debug=True)