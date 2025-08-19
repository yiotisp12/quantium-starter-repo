import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

# path to csv file
DATA_PATH = "./formatted_data.csv"
Colors = {
    "primary": "#0F2C67", # BMW San Marino Blue background color
    "secondary": "#1E88E5", # BMW Voodoo Blue accent color
    "font": "F8F9F9" # Audi Ibis White text color
}

# load data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash app
dash_app = Dash(__name__)


# create line plot visual
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout()
    plot_bgcolor = Colors["primary"],
    plot_bgcolor = Colors["secondary"],
    font_color = Colors["font"]
    )
    return line_chart


visualization = dcc.Graph(
    id = "visualization",
    figure = generate_figure(data)
)

# create header
header = html.H1(
    "Pink Morsel Visual",
    id = "header",
    style = {
        "background-color": COLORS["primary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# region selector
region_selector = dcc.RadioItems(
    ["north", "south", "east", "west", "all"],
    "north",
    id = "region-selector",
    inline = True
)
region_selector_wrapper = html.Div(
    [
        region_selector
    ],
    style = {
        "font-size": "150%"
    }
)


#define region selector callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_selector, "value")
)
def update_graph(region):
    # filtered data
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == region]

        # generate a new chart with filtered data
        figure = generate_figure(filtered_data)
        return figure


# app layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_selector_wrapper
    ],
    style = {
        "text-align": "center",
        "background-color": Colors["primary"],
        "border-radius": "20px"
    }
)

# true only if a script is run as a program entry point
if __name__ == '__main__':
    dash_app.run_server()