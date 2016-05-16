# This module updates the database tables, and adds test values to it


from conferenceX.models import db, HTML, Person, Question, Price, User
from conferenceX.models import DATABASE_DICT
from secrets import HASHED_PW


def add_table():
    return """
            <tbody>
                <thead>
                <tr>
                    <th data-field="id">Time</th>
                    <th data-field="name">Speaker</th>
                    <th data-field="price">Title</th>
                </tr>
                </thead>
                <tr>
                    <td>3:00</td>
                    <td>Eclair</td>
                    <td>Eclair</td>
                </tr>
                <tr>
                    <td>3:30</td>
                    <td>Eclair</td>
                    <td>Jellybean</td>
                </tr>
                <tr>
                    <td>4:00</td>
                    <td>Eclair</td>
                    <td>Lollipop</td>
                </tr>
                <tr>
                    <td>4:00</td>
                    <td>Eclair</td>
                    <td>Lollipop</td>
                </tr>
                <tr>
                    <td>4:00</td>
                    <td>Eclair</td>
                    <td>Lollipop</td>
                </tr>
            </tbody>
            """


def add_location():
    return """
           <h5 class="grey-text"> Address </h5>
           <hr>
           <p class="flow-text">
               2265 Erin Centre Blvd, Mississauga ON
           </p>

           <h5 class="grey-text"> Date and time</h5>
           <hr>
           <p class="flow-text">June 1 2016 from 3 pm to 7 pm</p>
           """


def add_about():
    return """
            Praesent commodo risus velit, sit amet tincidunt risus
            pharetra et. Pellentesque in elit magna. Nam scelerisque
            sem quis orci blandit aliquam. Curabitur et metus tortor.
            Integer eu eros nisi. Nunc sodales tortor sed
            justo sollicitudin
            ullamcorper. Quisque interdum ligula eget elit aliquam,
            sit amet
            ultrices mi ultrices. Maecenas ultrices odio lorem, id
            imperdiet
            enim vestibulum at."""


def google_maps():
    return """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2891.2543947112094!2d-79.71834638499719!3d43.559581966498236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882b418b3d8ade65%3A0xba2d4d9099046a2!2sJohn+Fraser+Secondary+School!5e0!3m2!1sen!2sca!4v1462459740942" width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>"""


def add_apply_text():
    return """
           Duo commune imperdiet te, ea omittam euripidis suscipiantur nec. N
           e lucilius perfecto similique cum, eros molestiae maiestatis ei qu
           o. An etiam melius instructior vel, in vix soleat lobortis gloriat
           ur. Has option accommodare et, eum an rebum equidem consequat.<br>
           """


def test_html():
    return HTML(title="Phase Shift",
                subtitle="June 1 2016 @ Living Arts Centre",
                show_program=True,
                show_location=True,
                show_ticket_button=True,
                show_speaker_button=False,
                table=add_table(),
                location=add_location(),
                google_maps=google_maps(),
                about=add_about(),
                apply_text=add_apply_text())


def test_persons():
    desc = """
           Id sonet soluta virtute ius, vim atqui graecis ullamcorper ut,
           cum in nibh novum. Ipsum sanctus has eu.
           In sumo discere pri, quo te vivendum voluptatum.
           """

    persons = []
    persons.append(
            Person(url="https://s3.amazonaws.com/" +
                   "uifaces/faces/twitter/brynn/128.jpg",
                   id=1,
                   name="Ya Bish",
                   school="Mom Fraser SS",
                   description=desc))

    persons.append(
            Person(url="https://s3.amazonaws.com/" +
                   "uifaces/faces/twitter/dustin/128.jpg",
                   id=2,
                   name="Rel Y. High",
                   school="Butt University",
                   description=desc))

    persons.append(
            Person(url="https://s3.amazonaws.com/" +
                   "uifaces/faces/twitter/connor_gaunt/128.jpg",
                   id=3,
                   name="N. Olips",
                   school="U of C",
                   description=desc))

    persons.append(
            Person(url="http://cdn2.blog-media.zillowstatic.com/8/" +
                   "Chris-Morrison-Facebook-c7ea82-300x300.jpg",
                   id=4,
                   name="No Treal",
                   school="Unemployed",
                   description=desc))

    return persons


def test_questions():
    questions = []

    answer = """
            Nominati intellegam eu sit. Nam sapientem deterruisset in, id vel
            deserunt explicari. Ius viris utinam ex, fabulas scribentur pri c
            u. Partem putant ne quo, ut vis sumo nemore. Ei agam labitur mole
            stie vim.
            """

    for i in range(8):
        questions.append(Question(id=i+1,
                         question="Lorem ipsum",
                         answer=answer))

    return questions


def test_prices():
    prices = []

    prices.append(Price(name="Youth",
                  price="$12",
                  id=1,
                  description="for one youth"))

    prices.append(Price(name="General (18+)",
                  price="$15",
                  id=2,
                  description="for one adult"))

    prices.append(Price(name="Group",
                  price="$45",
                  id=3,
                  description="for five adults"))

    return prices


def insert_test_data():
    db.create_all()
    html = test_html()
    if not HTML.query.limit(1).all():
        print("html not empty, adding test data:", html)
        db.session.add(html)

    for persons in test_persons():
        if not Person.query.get(persons.id):
            print("adding", persons)
            db.session.add(persons)

    for question in test_questions():
        if not Question.query.get(question.id):
            print("adding", question)
            db.session.add(question)

    for question in test_questions():
        if not Question.query.get(question.id):
            print("adding", question)
            db.session.add(question)

    for price in test_prices():
        if not Price.query.get(price.id):
            print("adding", price)
            db.session.add(price)

    if not User.query.get("root"):
        print("adding root")
        user = User(username="root", hashed=HASHED_PW)
        db.session.add(user)

    db.session.commit()
    print("committed to database")



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

if __name__ == "__main__":
    insert_test_data()
