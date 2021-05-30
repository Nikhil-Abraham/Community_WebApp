from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

USER_LIST = set()


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///community.db")


@app.route("/")
def index():
  if not session.get("user_id"):
    return redirect("/intro")
    
  else:
    return render_template("index.html")

@app.route("/intro", methods=["GET","POST"])
def intro():
  print("Entered def Intro() block")
  session.clear()
  if request.method == "POST":
    print("Entered Post Block")
    if request.form['submit_button']=="Register":
      username = request.form.get("username")
      password = request.form.get("password")
      hash = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8
        )
      rows = db.execute("SELECT * FROM users WHERE email=?",username)
      if len(rows)==1:
        return render_template("error.html",message="User Already Registered!",Code=403)
      
      return_id = db.execute("INSERT INTO users(email,hash) VALUES(?,?)",username,hash)
      
      session["user_id"] = return_id
      
      return redirect("/")
      
    print("Just Outside Login Block")
    
    
    if request.form['submit_button'] == "Login":
      print("Entered Login Block")
      
      username = request.form.get("username")
      password = request.form.get("password")
      
      rows = db.execute("SELECT * FROM users WHERE email = ?",username)
      
      if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        return render_template("error.html",message="Incorect Password !",Code=403)
      else:
        session["user_id"] = rows[0]["uid"]
        return redirect("/")
      
  else:
    return render_template("intro.html")
    


@app.route("/logout")
def logout():
  session.clear()
  USER_LIST.clear()
  return redirect("/intro")

@app.route("/explore", methods=["GET","POST"])
def explore():
  if not session.get("user_id"):
    return redirect("/intro")
  if request.method == "POST":
    rows = request.form.getlist("list")
    for row in rows:
      USER_LIST.add(row)
    print(USER_LIST)
    
    for tid in USER_LIST:
      print(session['user_id'],tid)
      
      db.execute("INSERT INTO user_topic(uid,tid) VALUES(?,?)",session["user_id"],tid)
    
    return redirect("/result")
  else:
    rows = db.execute("SELECT * FROM topics")
    return render_template("explore.html",rows=rows)
  
@app.route("/result")
def result():
  
  results = {}
  if not session.get("user_id"):
    return redirect("/intro")
  print("entered result block")
  emails = set()
  topics = []
  for tid in USER_LIST:
    names = db.execute("SELECT name FROM topics WHERE tid=?",tid)
    for name in names:
      topics.append(name["name"])
      rows = db.execute("SELECT email FROM users WHERE uid in (SELECT uid FROM user_topic WHERE tid=?)",tid)
      for row in rows:
        emails.add(row["email"])        
      results[name["name"]] =  emails
      
      print(result)
    
    
    
  return render_template("result.html", results = results)