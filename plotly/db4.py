import os
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table

FILEPATH = os.path.join("data", "baumkataster_frankfurt_2021.parquet")
data = pd.read_parquet(FILEPATH)

dfg = data.groupby("GATTUNG").agg(
    {
        "PFLANZJAHR": "mean",
        "BAUMHOEHE": "mean",
        "BAUMNUMMER": "count",
        "ST_DURCHM": "mean"
    }
)
dfg = dfg.reset_index()
dfg = dfg.rename(columns={"BAUMNUMMER": "COUNT"})

fig = px.scatter(dfg, x="PFLANZJAHR", y="BAUMHOEHE", size="COUNT", color="ST_DURCHM", hover_name="GATTUNG")

app = Dash() 
app.layout = html.Div(
    children=[
        dcc.Tabs(
            [
                dcc.Tab(label="Main Dashboard", children=(
                    [
                        dcc.Graph(figure=fig)
                    ]
                )),
                dcc.Tab(label="Table", children=(
                    [
                        dash_table.DataTable(data=data[:100].to_dict("records"))
                    ]
                )),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)