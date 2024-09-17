from flask import Flask, render_template, request, flash, redirect, url_for, session

from BackEnd import BackEnd

app = Flask(__name__)
app.secret_key = "shh"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/result")
def result():
    ret_val = request.args.get('id')
    return render_template("result.html", ret_val=ret_val)


if __name__ == "__main__":
    app.run(debug=True)