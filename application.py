from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("/intro")

@app.route("/intro")
def intro():
  return render_template("intro.html")