""" Contains db tables for frontend. """

import bcrypt
from conferenceX.flask_app import db


class HTML(db.Model):
    """ The text content for the index page """
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
    payment_msg = db.Column(db.Text)
    sponsor_text = db.Column(db.Text)
    sponsor_url = db.Column(db.Text)

    def __repr__(self):
        return "<HTML Table " + str(self.id) + ">"

    def edit_view(self):
        edit = []
        edit.append({"column": "title", "label": "Title",
                     "value": self.title})
        edit.append({"column": "subtitle", "label": "Subtitle",
                     "value": self.subtitle})
        edit.append({"column": "about", "label": "About Text",
                     "value": self.about})
        edit.append({"column": "table", "label": "Schedule HTML",
                     "value": self.table})
        edit.append({"column": "location", "label": "Location Text",
                     "value": self.location})
        edit.append({"column": "google_maps", "label": "Embedded Map HTML",
                     "value": self.google_maps})
        edit.append({"column": "payment_msg", "label": "Payment Explanation",
                     "value": self.payment_msg})

        edit.append({"column": "apply_text", "label": "Apply Text",
                     "value": self.apply_text})

        edit.append({"column": "sponsor_text", "label": "Sponsor Text",
                     "value": self.sponsor_text})
        edit.append({"column": "sponsor_url",
                     "label": "Sponsor Presentation URL",
                     "value": self.sponsor_url})

        edit.append({"column": "show_location",
                     "label": "Enable users to see location?",
                     "value": self.show_location})
        edit.append({"column": "show_program",
                     "label": "Enable users to see program?",
                     "value": self.show_program})
        edit.append({"column": "show_ticket_button",
                     "label": "Enable users to buy tickets?",
                     "value": self.show_ticket_button})
        edit.append({"column": "show_speaker_button",
                     "label": "Enable users to apply as speaker?",
                     "value": self.show_speaker_button})
        return edit


class Person(db.Model):
    """ A 'featured person' """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(140))
    school = db.Column(db.Text)
    description = db.Column(db.Text)

    def __init__(self, id=None, name="", url="", school="", description=""):
        self.id = id
        self.name = name
        self.url = url
        self.school = school
        self.description = description

    def __repr__(self):
        return "<Persons " + str(self.id) + " " + self.name + ">"

    def edit_view(self):
        edit = []
        edit.append({"column": "name", "label": "Name",
                     "value": self.name})
        edit.append({"column": "url", "label": "Picture URL",
                     "value": self.url})
        edit.append({"column": "school", "label": "Occupation or school",
                     "value": self.school})
        edit.append({"column": "description", "label": "Short Description",
                     "value": self.description})
        return edit


class Question(db.Model):
    """ A question for the FAQ """
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __init__(self, id=None, question="", answer=""):
        self.id = id
        self.question = question
        self.answer = answer

    def __repr__(self):
        return "<Question " + str("self.id") + " " + self.question + ">"

    def edit_view(self):
        edit = []
        edit.append({"column": "question", "label": "Question",
                     "value": self.question})
        edit.append({"column": "answer", "label": "Answer",
                     "value": self.answer})

        return edit


class Price(db.Model):
    """ A price for a ticket """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.String(10))
    description = db.Column(db.Text)
    url = db.Column(db.Text)

    def __init__(self, id=None, name="", price="", description="", url=""):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.url = url

    def __repr__(self):
        return "<Question " + str("self.id") + " " + self.name + ">"

    def edit_view(self):
        edit = []
        edit.append({"column": "name", "label": "Heading", "value": self.name})
        edit.append({"column": "price", "label": "Price", "value": self.price})
        edit.append({"column": "description", "label": "Subheading",
                     "value": self.description})
        edit.append({"column": "url", "label": "Tilt URL",
                     "value": self.url})
        return edit


class User(db.Model):
    """ Root user """
    username = db.Column(db.String(80), primary_key=True)
    hashed = db.Column(db.Text)

    def verify(self, attempt):
        if type(self.hashed) is str:
            hashed = self.hashed
        else:
            hashed = self.hashed.decode("utf-8")

        return hashed == bcrypt.hashpw(attempt, self.hashed)

    def __repr__(self):
        return "<User " + self.username + ">"


class Sponsor(db.Model):
    """ Sponsors """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.Text)
    website = db.Column(db.Text)

    def __init__(self, id=None, name="", url="", website="#void"):
        self.id = id
        self.name = name
        self.url = url
        self.website = website

    def __repr__(self):
        return "<Sponsor" + str("self.id") + " " + self.name + ">"

    def edit_view(self):
        edit = []
        edit.append({"column": "name", "label": "Sponsor Name",
                     "value": self.name})
        edit.append({"column": "url", "label": "Logo URL",
                     "value": self.url})
        edit.append({"column": "website", "label": "Sponsor Website " +
                     "(keep as #void if they don't provide a link)",
                     "value": self.website})
        return edit


DATABASE_DICT = {"html": HTML, "person": Person,
                 "question": Question, "sponsor": Sponsor}
