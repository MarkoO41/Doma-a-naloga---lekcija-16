from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/omeni")
def omeni():
    return render_template("omeni.html")

@app.route("/slike")
def slike():
    return render_template("slike.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run()