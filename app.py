import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd

'''

I am makinga web dashboard in Dash. My dashboard is about anlayzing poverty dynamics using indian census datavisualization. I have the required data set and this is the format of it (datasets/final_dataset.csv):
State,District,Area (sq km),Households,Total Population,Total Males,Total Females,Literate Population,Literate Males,Illiterate Population,Males Illiterates,Female Illiterates,Total Working Population,Total Working Males,Total Working Females,Unemployed Population,Unemployed Males,Unemployed Females,ST,SC,Hindus,Muslims,Sikhs,Buddhists,Jains,Others_Religions,Religion_Not_Stated,Households,Rural_Households,Urban_Households,Households_with_Internet,MPI HCR

Write me a basic dashboard using this data set containing data for around 640 districts according to the 2011 census. MPI HCR is the multidimensional poverty indicator head count ratio.
'''
# Create a simple line chart
df = pd.read_csv('datasets/final_dataset.csv')

df['MPI HCR'] = df['MPI HCR'].str.replace('%','').astype('float')

print(df[df['MPI HCR'] > 70])

fig = go.Figure(data=go.Scatter(x=df['District'], y=df[df['MPI HCR'] > 70]['MPI HCR']))

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)