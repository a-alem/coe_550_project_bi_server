from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api

server = Flask(__name__)
app = Dash(server=server)
api = Api(server)

df_data = {
    "Topic": ["livingroomlight", "livingroomtv", "livingroomheater", "bedroomtempsensor", "kitchencofee", "garagedoor"],
    "Events": [0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(df_data)

class AppendData(Resource):
    def get(self, data):
        counter = 0
        for topic in df_data["Topic"]:
            if topic == data:
                df["Events"][counter] += 1
                break
            else:
                counter += 1
        
        # Redraw App layout
        app.layout = html.Div(children=[
            'Number of total events graph',
            dash_table.DataTable(data=df.to_dict('records'), page_size=10),
            dcc.Graph(figure=px.histogram(df, x='Topic', y='Events'))
        ])
        return {'Message': "success"}

api.add_resource(AppendData, '/append/<data>')

# Incorporate data
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')



# App layout
app.layout = html.Div(children=[
    'Number of total events graph',
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='Topic', y='Events'))
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
