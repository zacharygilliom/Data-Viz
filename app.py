import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np


def add_columns(df, column_name_1, column_name_2,decider_column):
	df[column_name_1] = np.where(df[decider_column] == 'E-Commerce', 1, 0)
	df[column_name_2] = np.where(df[decider_column] == 'Retail', 1, 0)
	return df


df = pd.read_csv('SalesPortalOrderLog.csv')

df = add_columns(df,'Total E-Commerce', 'Total Retail', 'Brand')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Customer Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Each Customer', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
    	id='Orders bar graph'
    ),

    dcc.Slider(
        id = 'year-slider',
        min = df['Month'].min(),
        max = df['Month'].max(),
        value = df['Month'].min(),
        marks = {str(Date): str(Date) for Date in df['Month'].unique()},
        step = None
    ),
    dcc.Graph(
        id='Estimates bar graph'
    ),

    dcc.Slider(
        id = 'year-slider2',
        min = df['Month'].min(),
        max = df['Month'].max(),
        value = df['Month'].min(),
        marks = {str(Date): str(Date) for Date in df['Month'].unique()},
        step = None

    ),

])


@app.callback(
    Output('Orders bar graph', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['Month'] == selected_year]
    traces = []
    for i in filtered_df['B2B/C2C'].unique():
        traces.append(dict(
            x = df[df['B2B/C2C']==i]['Name'],
            # x = df_by_name['Name'],
            y = df[df['B2B/C2C'] ==i]['Total E-Commerce'],
            # y = df_by_name['Total Orders'],
            type = 'bar',
            width = .25,
            name = i)
        
        )
    return {
        'data': traces,
        'layout': 
                {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': {
                'color': colors['text'],
            },
            'title': 'B2B/C2C Orders by Customer',
            'xaxis' : {'tickangle':25},
            'yaxis' : {'title': 'Number of E-Commerce'},
            
                
        }

}

@app.callback(
    Output('Estimates bar graph', 'figure'),
    [Input('year-slider2', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['Month'] == selected_year]
    traces = []
    for i in filtered_df['B2B/C2C'].unique():
        traces.append(dict(
            x = df[df['B2B/C2C']==i]['Name'],
            # x = df_by_name['Name'],
            y = df[df['B2B/C2C'] ==i]['Total Retail'],
            # y = df_by_name['Total Orders'],
            type = 'bar',
            width = .25,
            name = i)
        
        )
    return {
        'data': traces,
        'layout': 
                {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': {
                'color': colors['text'],
            },
            'title': 'B2B/C2C Orders by Customer',
            'xaxis' : {'tickangle':25},
            'yaxis' : {'title': 'Number of Retail'},
            
                
        }

}


if __name__ == '__main__':
    app.run_server(debug=True)
  


