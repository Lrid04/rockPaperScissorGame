from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "shh"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)