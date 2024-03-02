from dash import Dash, html
 
app = Dash()
 
app.layout = html.H1("Guten Morgen Berlin")
 
print("guten morgen")
if __name__ == "__main__":
    app.run_server(debug=True)