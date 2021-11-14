import dash
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

#Eksplorasi data dengan python
#________________________________________________

df = pd.read_csv("vgsales.csv")

#print(df[:5])
#print (df.iloc[:5, [2,3,5,10]])
print(df.Genre.nunique())
print(df.Genre.unique())
print(sorted(df.Year.unique()))

#Visualisasi data dengan plotly
#________________________________________________

#fig_pie = px.pie(df, names="Genre", values = 'Japan Sales')
#fig_pie = px.pie(df, names="Genre", values = 'North American Sales')

#fig_pie.show()

#fig_bar = px.bar(df, x='Genre', y='North American Sales')
#fig_bar.show()

#fig_hist = px.histogram(df, x='Year', y='North American Sales', labels = "Genre")
#fig_hist.show()

#Dashboard INteraktif dengan Dash Python

app = dash.Dash(__name__)

#layout/isi tampilan yang akan muncul di dashboard
app.layout=html.Div([
    html.H1("Analisis Grafik dengan Data yang Menarik"),
    dcc.Dropdown(id='genre-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.Genre.unique())],  #<==== dialkukan perulangan untuk mengambil setiap genre di df.Genre
                 value="Sports"
                 ),
    dcc.Graph(id='my-graph',figure={}  #akan terhubung dengan fungsi def dibawah, jadi tidak perlu lagi plotting
              )



])

#  Dasar Syntax untuk callback
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphing(value_genre):
    print(value_genre)
    dff = df[df.Genre==value_genre]
    fig = px.histogram(df, x='Year', y='North American Sales', labels = "Genre")
    return fig    #akan terhubung dan memasukkannya ke 'dropdown'


#untuk menjalankan app nya
if __name__=='__main__':
    app.run_server()