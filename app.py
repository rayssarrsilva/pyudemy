from flask import Flask, render_template, request
from mat2 import processar_matriz
from matriz import matriz_user


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        n = int(request.form["n"])
        # depois de receber n, renderiza a página com os campos da matriz
        return render_template("matriz.html", n=n)
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n = int(request.form["n"])
    valores = [float(x) for x in request.form.getlist("valores")]
    diagonal, negativos = processar_matriz(n, valores)
    return render_template("resultado.html", diagonal=diagonal, negativos=negativos, n=n)

@app.route("/matriz", methods=["POST"])
def matriz_route():
    linhas = int(request.form["linhas"])
    colunas = int(request.form["colunas"])

    matriz = matriz_user(linhas, colunas, request.form)
    return render_template("mostrar_matriz.html", matriz=matriz, linhas=linhas, colunas=colunas)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

