import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

# Create the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id="graph",
        figure={
            "data": [
                {
                    "x": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico"],
                    "y": [1, 1.3, 0.3, 0.27, 0.21, 206, 208, 164, 146, 128],
                    "type": "bar"
                }
            ],
            "layout": {
                "title": "Population of the 10 Most Populous Countries in the World"
            }
        }
    ),
    dcc.Dropdown(
        id="graph-type",
        options=[
            {
                "label": "Bar chart",
                "value": "bar"
            },
            {
                "label": "Line chart",
                "value": "line"
            },
            {
                "label": "Pie chart",
                "value": "pie"
            }
        ],
        value="bar",
        style={"width": "50%"}  # Customize the width here, e.g., "50%" for half of the screen width
    )
])

# Update the figure property of the Graph component
@app.callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="graph-type", component_property="value")
)
def update_graph(graph_type):
    if graph_type == "pie":
        proportions = [pop / sum([1, 1.3, 0.3, 0.27, 0.21, 206, 208, 164, 146, 128]) for pop in [1, 1.3, 0.3, 0.27, 0.21, 206, 208, 164, 146, 128]]
        figure = {
            "data": [
                {
                    "labels": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico"],
                    "values": proportions,
                    "type": "pie"
                }
            ],
            "layout": {
                "title": "Population of the 10 Most Populous Countries in the World"
            }
        }
    else:
        figure = {
            "data": [
                {
                    "x": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico"],
                    "y": [1, 1.3, 0.3, 0.27, 0.21, 206, 208, 164, 146, 128],
                    "type": graph_type
                }
            ],
            "layout": {
                "title": "Population of the 10 Most Populous Countries in the World"
            }
        }
    return figure

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
