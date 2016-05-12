# Contains db tables for frontend. If this module is called, the database
# tables are updated


from flask_sqlalchemy import SQLAlchemy
from conferenceX import app
import bcrypt
try:
    from secrets import DATABASE_URI
except ImportError:
    import sys
    print("no secrets.py file created, please do that")
    sys.exit(-1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)


class HTML(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    show_location = db.Column(db.Boolean)
    show_program = db.Column(db.Boolean)
    show_ticket_button = db.Column(db.Boolean)
    show_speaker_button = db.Column(db.Boolean)

    subtitle = db.Column(db.Text)
    table = db.Column(db.Text)
    location = db.Column(db.Text)
    google_maps = db.Column(db.Text)
    about = db.Column(db.Text)
    apply_text = db.Column(db.Text)

    def __repr__(self):
        return "<HTML Table " + str(self.id) + ">"


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(140))
    school = db.Column(db.Text)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<Persons " + str(self.id) + " " + self.name + ">"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __repr__(self):
        return "<Question " + str("self.id") + " " + self.question + ">"


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.String(10))
    description = db.Column(db.Text)

    def __repr__(self):
        return "<Question " + str("self.id") + " " + self.name + ">"


class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    hashed = db.Column(db.String(80))

    def verify(self, attempt):
        attempt = bytes(attempt, 'utf-8')
        hashed = bytes(self.hashed, 'utf-8')
        return hashed == bcrypt.hashpw(attempt, hashed)

    def __repr__(self):
        return "<User " + self.username + ">"

if __name__ == "__main__":
    db.create_all()
