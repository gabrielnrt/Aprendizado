from dash import html, dcc, Dash


app = Dash(__name__)

app.layout = html.Div(children = [

    html.H1(children = 'Códigos de aeroportos'),

    dcc.Dropdown(options = ['GRU', 'YYZ', 'ATL'], value = 'GRU')

])

if __name__ == '__main__':
    app.run_server(debug = True)
