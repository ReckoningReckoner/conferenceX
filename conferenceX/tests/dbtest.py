# This module updates the database tables, and adds test values to it


from conferenceX.flask_app import db
from conferenceX.models import HTML, Person, Question, Price, User
from conferenceX.models import DATABASE_DICT
import conferenceX.tests.testdata as testdata
from secrets import HASHED_PW
import bcrypt


def insert_test_data():
    """ Inserts a bunch of test data into the databse """

    db.create_all()
    html = testdata.test_html()
    if not HTML.query.limit(1).all():
        print("html not empty, adding test data:", html)
        db.session.add(html)

    for persons in testdata.test_persons():
        if not Person.query.get(persons.id):
            print("adding", persons)
            db.session.add(persons)

    for question in testdata.test_questions():
        if not Question.query.get(question.id):
            print("adding", question)
            db.session.add(question)

    for question in testdata.test_questions():
        if not Question.query.get(question.id):
            print("adding", question)
            db.session.add(question)

    for price in testdata.test_prices():
        if not Price.query.get(price.id):
            print("adding", price)
            db.session.add(price)

    db.session.commit()
    print("committed to database")

# Inserts the root into the database


def insert_root():
    """ Inserts the root user into the db """
    root = User.query.get("root")
    if not User.query.get("root"):
        print("adding root")
        user = User(username="root", hashed=HASHED_PW)
        db.session.add(user)
        db.session.commit()
    else:
        print("Root already exists, updating")
        root.hashed = HASHED_PW
        db.session.commit()


def print_row(row):
    def align(x, y):
        a, b = len(x), len(y)
        end = (b-a)*" "
        print(" " + x + end, end="|")

    for col in row:
        align(str(col["column"]), str(col["value"]))
    print("")

    for col in row:
        align(str(col["value"]), str(col["column"]))
    print("")


def test_blank_data():
    """ Inserts a bunch of blank data into the db, them removes them """

    for name, table in DATABASE_DICT.items():
        row = table()

        print("TABLE IS", name)
        print("row is currently: id=", row.id)
        print_row(row.edit_view())

        db.session.add(row)
        db.session.commit()
        print("added blank :", name)

        print("row is currently: id=", row.id)
        print_row(row.edit_view())

        db.session.delete(row)
        db.session.commit()
        print("deleted blank")
        print("------------------")


def test_fake_login():
    print("trying a test login")
    h = bcrypt.hashpw(b"walla", bcrypt.gensalt())
    user = User(username="u", hashed=h)
    assert user.verify("walla"), "FAILURE with correct pass"
    assert not user.verify("balla"), "FAILURE with incorrect pass"
    print("PASSED user login")
