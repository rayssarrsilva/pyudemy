from flask import Flask, render_template, request
from mat2 import processar_matriz


app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "POST":
        n = int(request.form["n"])
        valores = [float(x) for x in request.form.getlist("valores")]
        diagonal, negativos = processar_matriz(n, valores)
        return render_template("resultado.html", diagonal=diagonal, negativos=negativos, n=n)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

