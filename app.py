import dash
from dash import dcc, html, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.config.suppress_callback_exceptions=True
df = pd.read_csv('datasets/final_dataset.csv')

def home_layout():
    return html.Div([
        html.H1("Indian Poverty Dynamics Dashboard", className='text-center pt-5 px-5 text-white'),
        html.Div(className='mx-4 row text-white', children=[html.Col(className='col-4'),
            html.P("""This dashboard provides an analysis of district-wise poverty data 
                  based on NFHS Survey data in the NITI Aayog Multi-dimensional Poverty Index report."""
                ,className='col-4 text-white', style={'justify':'center'})]),
            html.Hr(),
        dcc.Link("Go to Dashboard", href="/dashboard", className='btn btn-primary mt-3 px-5'),
        dcc.Link("Info", href="/info", className='btn btn-primary mt-3 px-5'),
    ], className='text-center vh-100 vw-100', style={'background-image': f'url("/assets/5.png")', 'background-size': 'contain'})


def info_layout():
    return html.Div([
        html.H1("About", className='text-center pt-5 px-5 text-white'),
        html.Hr(), html.Div(className='mx-4 row text-white', children=[html.Col(className='col-3'),
            html.P("""\n
            We consider various parameters from the 2011 census data that may be relevant to the estimation of poverty in a district.

At the time of the 2011 census, there were a recorded 640 districts. The HCR values will be considered for only these districts. There is no available data for a poverty indicator at the district level in the year 2011.

To estimate and mesaure poverty we use the multi-dimensional poverty index (MPI) based on the 2023 NITI Aayog report which has the headcount of persons under the MPI line for the years 2014 and 2019. We will be using the head-count of the 2014 MPI for each district. This data will be scraped out of the report PDF file (resources/NITI_2023.pdf), and be stored in resources/dataset.csv""", className='col-6 text-white', style={'justify':'center'})
                   ,
            html.P("""Modules used: Plotly, Plotly-Dash, Dash-Bootstrap-Components, Pandas, Flask, pdfplumber.. etc""", className='text-white pb-4', style={'justify':'center'}),

                 ]),
        dash_table.DataTable(
            columns=[
                {'name': col, 'id': col} for col in
                ['District', 'State', 'Area (sq km)', 'Total Population', 'Literate Population',
                 'Total Working Population', 'Urban_Households', 'Households_with_Internet', 'MPI HCR']
            ],
            data=df.to_dict('records'),
            style_table={'height': '440px', 'overflow': 'auto', 'padding-left': '30px', 'padding-right': '30px'},
            page_size=11,
            style_cell={'textAlign': 'center', 'padding': '7px'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
            style_data={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'},
            style_as_list_view=True,
            selected_rows=[],
            virtualization=False,

        ),
    ], className='text-center vh-100 vw-100',
        style={'background-image': f'url("/assets/5.png")', 'background-size': 'contain'})

# Define dashboard layout
def dashboard_layout():
    return html.Div(style={'background-image': f'url("/assets/5.png")', 'background-size': 'contain'}, children=[
        html.Div(children=[
            html.Div(children=[
                html.H1(id='state_name', className='card-title')
            ], className='card-body text-white bg-primary pb-4 pt-4 text-center'),
        ]),

        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id='state-dropdown',
                    options=[
                        {'label': state, 'value': state} for state in df['State'].unique()
                    ],
                    value='Andhra Pradesh',
                    placeholder="Select a State",
                    multi=False
                ),
                width={'size': 6, 'offset': 3, 'align': 'center'},
                className='justify-content-center pt-2'
            ), className='px-0 mx-0 pt-2'
        ),

        html.Hr(),

        dash_table.DataTable(
            id='table',
            columns=[
                {'name': col, 'id': col} for col in ['District', 'Area (sq km)', 'Total Population', 'Literate Population', 'Total Working Population', 'MPI HCR']
            ],
            style_table={'height': '440px', 'overflow': 'auto', 'padding-left': '15px', 'padding-right': '15px'},
            page_size=11,
            style_cell={'textAlign': 'center', 'padding': '7px'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
            style_data={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'},
            style_as_list_view=True,
            selected_rows=[],
            virtualization=False,

        ),

        html.Hr(),

        html.H1('Districts with the most poverty:', className='card-body fw-bold shadow-lg text-white bg-primary text-center py-4'),

        dcc.Graph(id='line-plot', className='pb-5 pt-3 px-3'),

        dbc.Row([
            dbc.Col([
                html.H1('Correlation b/w Literacy & Poverty', className='card-body fw-bold shadow-lg text-white bg-primary text-center pt-4 pb-3'),
                dcc.Graph(
                    id='scatter-plot',
                    figure={
                        'data': [],
                        'layout': dict(
                            xaxis={'type': 'log', 'title': 'Literate Population'},
                            yaxis={'title': 'MPI HCR'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            hovermode='closest',
                            plot_bgcolor='#333',  # Dark grey background
                            paper_bgcolor='#333',  # Dark grey background
                            font={'color': 'white'},  # White text
                        )
                    },
                    className='p-3 dark-bg'
                ),
            ], width=6, className='px-3 py-0'),

            dbc.Col([

                html.H1('Population groups in the state', className='card-body fw-bold shadow-lg text-white bg-primary text-center pt-4 pb-3'),
                dcc.Graph(
                    id='bar-chart',
                    figure={
                        'data': [],
                        'layout': dict(
                            barmode='group',
                            xaxis={'title': 'Categories'},
                            yaxis={'title': 'Population'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            hovermode='closest',
                            plot_bgcolor='#333',  # Dark grey background
                            paper_bgcolor='#333',  # Dark grey background
                            font={'color': 'white'},  # White text
                        )
                    },
                    className='p-3 dark-bg'
                ),
            ], width=6, className='px-3 py-0'),
        ]),

    ], className='px-3')


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback to switch between home and dashboard layouts
@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard_layout()
    if pathname == '/info':
        return info_layout()
    else:
        return home_layout()

# Callback to open the modal
@app.callback(
    dash.dependencies.Output("intro-modal", "is_open"),
    [dash.dependencies.Input("intro-modal-close", "n_clicks")],
    prevent_initial_call=False,
)
def open_intro_modal(n_clicks):
    return True

# Define callback to update scatter plot and bar chart based on selected state
@app.callback(
    [dash.dependencies.Output('scatter-plot', 'figure'),
     dash.dependencies.Output('bar-chart', 'figure'),
     dash.dependencies.Output('state_name', 'children'),
     dash.dependencies.Output('table', 'data'),
     dash.dependencies.Output('line-plot', 'figure')],
    [dash.dependencies.Input('state-dropdown', 'value')])
def update_plots(selected_state):
    if not selected_state:
        return {'data': [], 'layout': {}}, {'data': [], 'layout': {}}

    filtered_df = df[df['State'] == selected_state]
    display_table = filtered_df[['District', 'Area (sq km)', 'Total Population', 'Literate Population', 'Total Working Population', 'MPI HCR']]
    filtered_df['MPI HCR'] = filtered_df['MPI HCR'].str.replace('%', '').astype(float)

    scatter_plot_figure = {
        'data': [
            dict(
                x=filtered_df['Literate Population'],
                y=filtered_df['MPI HCR'],
                text=filtered_df['District'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 9,
                    'line': {'width': 1, 'color': 'black'}
                },
                name=selected_state
            )
        ],
        'layout': dict(
            xaxis={'type': 'log', 'title': 'Total Population'},
            yaxis={'title': 'MPI HCR'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest',
            plot_bgcolor='#111111',  # Dark grey background
            paper_bgcolor='#111111',  # Dark grey background
            font={'color': 'white'},  # White text
        )
    }

    bar_chart_figure = go.Figure()

    bar_chart_figure.add_trace(go.Bar(
        x=['Population', 'Literate Population', 'Working Population'],
        y=[filtered_df['Total Population'].sum(), filtered_df['Literate Population'].sum(),
           filtered_df['Total Working Population'].sum()],
        name='Total'
    ))

    bar_chart_figure.add_trace(go.Bar(
        x=['Population', 'Literate Population', 'Working Population'],
        y=[filtered_df['Total Males'].sum(), filtered_df['Literate Males'].sum(),
           filtered_df['Total Working Males'].sum()],
        name='Males'
    ))

    bar_chart_figure.add_trace(go.Bar(
        x=['Population', 'Literate Population', 'Working Population'],
        y=[filtered_df['Total Females'].sum(), filtered_df['Literate Females'].sum(),
           filtered_df['Total Working Females'].sum()],
        name='Females'
    ))

    bar_chart_figure.update_layout(
        barmode='group',
        xaxis={'title': 'Categories'},
        yaxis={'title': 'Population'},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        hovermode='closest',
        plot_bgcolor='#111111',  # Dark grey background
        paper_bgcolor='#111111',  # Dark grey background
        font={'color': 'white'},  # White text
    )

    sorted_df = filtered_df.sort_values(by='MPI HCR', ascending=False)

    fig = px.line(
        sorted_df,
        x='District',
        y='MPI HCR',
        text='MPI HCR',
        markers=True,
        line_shape='linear',
        labels={'MPI HCR': 'Highest MPI HCR'},
        title=f'Districts with Highest MPI HCR in {selected_state}',
        template='plotly_dark'
    ).update_layout(
        xaxis_title='District',
        yaxis_title='MPI HCR',
        showlegend=False
    )

    return scatter_plot_figure, bar_chart_figure, f'{selected_state} Analysis', display_table.to_dict('records'), fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
