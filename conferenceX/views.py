from conferenceX import app
from conferenceX.models import HTML, Person, Question, Price, User, db
from conferenceX.models import DATABASE_DICT
from flask import render_template, session, redirect, url_for, request
from flask import flash
from secrets import SECRET_KEY
import json

app.config["SECRET_KEY"] = SECRET_KEY
db.create_all()


def get_row_from_dict(row_edit):
    table = DATABASE_DICT.get(row_edit["table"])
    if table is None:
        raise AttributeError("Invalid table name")

    row = table.query.get(row_edit["id"])
    if row is None:
        raise AttributeError("Invalid id. Maybe wrong type?")

    return row


def update_row(row_edit):
    try:
        row = get_row_from_dict(row_edit)
        getattr(row, row_edit["column"])
        setattr(row, row_edit["column"], row_edit["value"])
    except AttributeError as e:
        raise e


def delete_row(row):
    try:
        row = get_row_from_dict(row)
        db.session.delete(row)
    except AttributeError as e:
        raise e


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('admin'):
        return redirect(url_for("login"))

    if request.method == "POST":
        if request.json:

            try:
                row_edit = request.json
                if row_edit.get("delete"):
                    print("delete", row_edit)
                    delete_row(row_edit)
                else:
                    print("update", row_edit)
                    update_row(row_edit)

                db.session.commit()
                print("committed")
            except AttributeError as e:
                return json.dumps({'error': str(e)}), 200

            return json.dumps({'status': 'OK'}), 200
    else:
        html = HTML.query.limit(1).all()
        prices = Price.query.all()
        persons = Person.query.all()
        questions = Question.query.all()

    return render_template("admin.html",
                           html=html,
                           prices=prices,
                           persons=persons,
                           questions=questions)


@app.route("/login", methods=["GET", "POST"])
def login():
    if not session.get('admin'):  # not logged in
        if request.method == "POST":
            user = User.query.get(request.form['username'])

            try:
                # User is validated
                if user is not None and user.verify(request.form['password']):
                    session['admin'] = True
                    return redirect(url_for('admin'))  # log in

                flash("incorrect username or password")
            except Exception as e:
                flash(e)
                return render_template('login.html')

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
