import pandas as pd
import dash
from dash import html as html
from dash import dcc as dcc
from dash.dependencies import Input, Output
import plotly.express as px


life_expec = pd.read_csv("life_expectancy.csv")


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Life Expectancy'),
    dcc.Dropdown(id='country-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in life_expec['Country'].unique()],
                 value='Afghanistan'),
    dcc.Graph(id='life-graph')
])

@app.callback(
    Output(component_id='life-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value')
)

def update_graph(selected_country):
    filtered_life_expec = life_expec[life_expec['Country'] == selected_country]
    line_fig = px.line(filtered_life_expec,
                       x='Year', y='Life expectancy ',
                       color='Country',
                       title=f'Life Expectancy in {selected_country}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)