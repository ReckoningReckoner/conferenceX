from conferenceX.flask_app import app, db
from conferenceX.models import HTML, Person, Question, Price, User
from conferenceX.models import DATABASE_DICT
from flask import render_template, session, redirect, url_for, request
from flask import flash, abort
import json


def get_table_from_str(table):
    """ Given a string table, return the corresponsind Table object """
    new_table = DATABASE_DICT.get(table)
    if new_table is None:
        raise AttributeError("Invalid table name")

    return new_table


def get_row_from_dict(row_edit):
    """ Given a dict with "table" and "id" keys,
    return the corresponing row object
    """

    table = get_table_from_str(row_edit["table"])
    if table is None:
        raise AttributeError("Invalid table name")

    row = table.query.get(row_edit["id"])
    if row is None:
        raise AttributeError("Invalid id. Maybe wrong type?")

    return row


def update_row(row_dict, row=None):
    """
    Updates a row from the database given a dictionary. A dictionary is given
    with a 'column' to determine the column to change, and a 'value' to
    determine what to change the current column's value to.

    If the row param is left as 'None', the program will try to look for a
    corresponding row object using the row_dicts 'table' and 'id' value.
    """

    try:
        if row is None:
            row = get_row_from_dict(row_dict)

        getattr(row, row_dict["column"])
        setattr(row, row_dict["column"], row_dict["value"])
    except AttributeError as e:
        raise e


def delete_row(row):
    """ Deletes a row from the datbase, given the row is a dictionary with keys
    containing the 'table' and 'id' from the database
    """

    try:
        row = get_row_from_dict(row)
        db.session.delete(row)
    except AttributeError as e:
        raise e


@app.route("/admin", methods=["GET", "POST"])
def admin():
    """ The admin page for various things, such as editing the db.
    If a user is NOT logged in, it should redict to the login page.
    """

    if not session.get('admin'):
        return redirect(url_for("login"))

    if request.method == "POST" and request.json:
        try:
            row_edit = request.json
            if row_edit.get("delete"):
                print("delete", row_edit)
                delete_row(row_edit)
            else:
                print("update", row_edit)
                update_row(row_edit)

            db.session.commit()

            return json.dumps({'status': 'OK'}), 200
        except AttributeError as e:
            return json.dumps({'error': str(e)}), 200

    html = HTML.query.limit(1).all()
    prices = Price.query.all()
    persons = Person.query.all()
    questions = Question.query.all()
    return render_template("admin.html",
                           html=html,
                           prices=prices,
                           persons=persons,
                           questions=questions)


@app.route("/admin/add/<table>", methods=["GET", "POST"])
def add(table):
    """ Adds a table to the database based on the URL. Throws an AttributeError
    if the table cannot be found, or a 403 error if the user looks for an
    invalid table type """

    if not session.get('admin'):
        return abort(403)

    try:
        if table == "HTML":
            raise AttributeError("Cannot edit HTML table")

        new_table = get_table_from_str(table)
    except AttributeError:
        return table + " is not a valid table", 403

    row = new_table()

    if request.method == "GET":
        return render_template("add.html", row=row)

        for form in request.form:
            row_dict = {}
            row_dict['table'], row_dict['id'], row_dict['column'] = \
                form.split("-")
            row_dict['value'] = request.form[form]
            update_row(row_dict, row)

        db.session.add(row)
    db.session.commit()

    return redirect(url_for('admin'))


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log in the admin for admintools """
    if not session.get('admin'):  # not logged in
        if request.method == "POST":
            user = User.query.get(request.form['username'])

            # User is validated
            if user is not None and user.verify(request.form['password']):
                session['admin'] = True
                return redirect(url_for('admin'))  # log in

            flash("incorrect username or password")
            return render_template('login.html'), 401

    return render_template("login.html")


@app.route("/logout")
def logout():
    """ Log out the admin """
    session.pop("admin", None)
    return redirect(url_for("index"))


@app.route("/")
def index():
    """ The main page with the majority of content """
    html = HTML.query.limit(1).all()[0]
    prices = Price.query.all()
    persons = Person.query.all()
    questions = Question.query.all()

    return render_template("index.html", html=html,
                           prices=prices, persons=persons,
                           questions=questions)
