from conferenceX.flask_app import app
from conferenceX.models import HTML, Person, Question, Price, User, db
from conferenceX.models import get_row_from_dict, get_table_from_str
from flask import render_template, session, redirect, url_for, request
from flask import flash, abort
from secrets import SECRET_KEY
import json

app.config["SECRET_KEY"] = SECRET_KEY
db.create_all()


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
        elif request.form:
            print("form")

            return json.dumps({'status': 'OK'}), 200

    html = HTML.query.limit(1).all()
    prices = Price.query.all()
    persons = Person.query.all()
    questions = Question.query.all()
    return render_template("admin.html",
                           html=html,
                           prices=prices,
                           persons=persons,
                           questions=questions)


@app.route("/admin/add/<table>")
def add(table):
    try:
        if table == "HTML":
            raise AttributeError

        new_table = get_table_from_str(table)
        row = new_table()
        print(row.edit_view())
        return render_template("add.html", row=row)

    except AttributeError:
        abort(403)


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
