import flask
from asgiref.wsgi import WsgiToAsgi

app = flask.Flask(__name__)
asgi_app = WsgiToAsgi(app)

# Rota para a página inicial
@app.route("/")
def home():
    return flask.render_template("index.html", active_page="inicio")

# Página dedicada aos serviços
@app.route("/servicos")
def services():
    return flask.render_template("services.html", active_page="servicos")

# Rota para a página "Sobre Nós"
@app.route("/sobre-nos")
def about():
    return flask.render_template("about.html", active_page="sobre")

# Rota para a página "Contato"
@app.route("/contato")
def contact():
    return flask.render_template("contact.html", active_page="contato")


if __name__ == "__main__":
    app.run(debug=True)
