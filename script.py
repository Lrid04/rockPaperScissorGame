from flask import Flask, render_template, request, flash, redirect, url_for, session

from BackEnd import BackEnd

app = Flask(__name__)
app.secret_key = "shh"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=['POST'])
def game():
    my_game = BackEnd

    return render_template("game.html")

@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)