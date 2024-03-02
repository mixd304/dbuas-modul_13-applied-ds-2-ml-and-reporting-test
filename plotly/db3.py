from dash import Dash, html, dcc
from datetime import date
import plotly.express as px
 
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation", text_auto=True)

app = Dash() 
app.layout = html.Div(
    children=[
        html.H1("Guten Morgen Berlin!"),
        html.H2("Es geht los!"),
        html.H3("H3"),
        html.P("Link zur Google Startseite:"),
        html.A("Google", href="https://google.com", target="_blank"),
        dcc.Checklist(["Linde", "Akazie", "Apfelbaum"], inline=True),
        dcc.DatePickerRange(start_date=date(year=2024, month=2, day=29)),
        dcc.RadioItems(options=["Alle Bäume", "Häufige Bäume", "Seltene Bäume"], value="Häufige Bäume"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)