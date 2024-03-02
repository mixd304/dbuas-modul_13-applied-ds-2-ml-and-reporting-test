import os
import pandas as pd
import plotly.express as px
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output

FILEPATH = os.path.join("data", "baumkataster_frankfurt_2022.parquet")
data = pd.read_parquet(FILEPATH)

tree_counts = data["GATTUNG"].value_counts()
rare_trees = tree_counts[tree_counts < 100].index.to_list()
common_trees = tree_counts[tree_counts > 2500].index.to_list()
print(tree_counts)

def _make_fig(df):
    dfg = df.groupby("GATTUNG").agg(
        {
            "PFLANZJAHR": "mean",
            "BAUMHOEHE": "mean",
            "BAUMNUMMER": "count",
            "ST_DURCHM": "mean",
        }
    )
    dfg = dfg.reset_index()
    dfg = dfg.rename(columns={"BAUMNUMMER": "COUNT"})
    fig = px.scatter(dfg, x="PFLANZJAHR", y="BAUMHOEHE", size="COUNT", color="ST_DURCHM", hover_name="GATTUNG")
    return fig

app = Dash()

@app.callback(Output("bubble-chart", "figure"), Input("radio-items", "value"))
def make_bubble_chart(value):
    if value == "Alle Bäume":
        return _make_fig(data)
    elif value == "Häufige Bäume":
        return _make_fig(data.query(f"GATTUNG == @common_trees"))
    elif value == "Seltene Bäume":
        return _make_fig(data.query(f"GATTUNG == @rare_trees"))
    
app.layout = html.Div(
    [
        html.H1("Intro Dashboard 5"),
        html.H2("Baumdaten 2022"),
        dcc.RadioItems(
            id="radio-items",
            options=[
                "Alle Bäume",
                "Häufige Bäume",
                "Seltene Bäume",
            ],
            value="Häufige Bäume",
        ),
        dcc.Graph(id="bubble-chart"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)