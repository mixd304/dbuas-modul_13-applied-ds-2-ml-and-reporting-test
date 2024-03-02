from dash import Dash, html
 
app = Dash()
 
app.layout = html.Div(
    children=[
        html.H1("Guten Morgen Berlin!"),
        html.H2("Es geht los!"),
        html.H3("H3"),
        html.P("Link zur Google Startseite:"),
        html.A("Google", href="https://google.com", target="_blank")
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)