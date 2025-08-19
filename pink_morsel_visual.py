import pandas
from dash import Dash, html, dcc

from plotly.express import line

# path to csv file
DATA_PATH = "./formatted_data.csv"

# load data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash app
dash_app = Dash(__name__)

# create line plot visual
line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id = "visualization",
    figure = line_chart
)

# create header
header = html.H1(
    "Pink Morsel Visual",
    id = "header"
)

# app layout
dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)

# true only if a script is run as a program entry point
if __name__ == '__main__':
    dash_app.run_server()