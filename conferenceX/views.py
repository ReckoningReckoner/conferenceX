from conferenceX import app
from conferenceX.models import HTML, Person, Question, Price, User
from flask import render_template, session, redirect, url_for, request
from flask import flash
from secrets import SECRET_KEY

app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('admin'):
        return redirect(url_for("login"))
    else:
        return render_template("admin.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if not session.get('admin'):  # not logged in
        if request.method == "POST":
            user = User.query.get(request.form['username'])

            # User is validated
            if user is not None and user.verify(request.form['password']):
                session['admin'] = True
                return redirect(url_for('admin'))  # log in
            else:
                flash("incorrect username or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("index"))


@app.route("/")
def index():
    html = HTML.query.limit(1).all()[0]
    prices = Price.query.all()
    persons = Person.query.all()
    questions = Question.query.all()

    return render_template("index.html", html=html,
                           prices=prices, persons=persons,
                           questions=questions)
