from conferenceX import app
from flask import render_template


def add_people():
    desc = """
           Id sonet soluta virtute ius, vim atqui graecis ullamcorper ut,
           cum in nibh novum. Ipsum sanctus has eu.
           In sumo discere pri, quo te vivendum voluptatum.
           """

    persons = []
    persons.append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/brynn/128.jpg",
           "id": "person1",
           "name": "Ya Bish",
           "school": "Mom Fraser SS",
           "description": desc}
          )

    persons.append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/dustin/128.jpg",
           "id": "person2",
           "name": "Rel Y. High",
           "school": "Butt University",
           "description": desc}
          )

    persons.append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/connor_gaunt/" +
           "128.jpg",
           "id": "person3",
           "name": "N. Olips",
           "school": "U of C",
           "description": desc}
          )

    persons.append(
          {"url":
           "http://cdn2.blog-media.zillowstatic.com/8/" +
           "Chris-Morrison-Facebook-c7ea82-300x300.jpg",
           "id": "person4",
           "name": "No Treal",
           "school": "Unemployed",
           "description": desc}
          )

    return persons


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
    return """ <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2891.2543947112094!2d-79.71834638499719!3d43.559581966498236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882b418b3d8ade65%3A0xba2d4d9099046a2!2sJohn+Fraser+Secondary+School!5e0!3m2!1sen!2sca!4v1462459740942" width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>"""


def add_prices():
    prices = []

    prices.append(
            {"name": "Youth",
             "price": "$12",
             "description": "for one youth"}
            )

    prices.append(
            {"name": "General (18+)",
             "price": "$15",
             "description": "for one adult"}
            )

    prices.append(
            {"name": "Group",
             "price": "$45",
             "description": "for five adults"}
            )

    return prices


def add_faq():
    questions = []

    answer = """
            Nominati intellegam eu sit. Nam sapientem deterruisset in, id vel
            deserunt explicari. Ius viris utinam ex, fabulas scribentur pri c
            u. Partem putant ne quo, ut vis sumo nemore. Ei agam labitur mole
            stie vim.
            """

    q = {"question": "Lorem impsum", "answer": answer}

    for i in range(8):
        questions.append(q)
    return questions


def add_apply_text():
    return """
           Duo commune imperdiet te, ea omittam euripidis suscipiantur nec. N
           e lucilius perfecto similique cum, eros molestiae maiestatis ei qu
           o. An etiam melius instructior vel, in vix soleat lobortis gloriat
           ur. Has option accommodare et, eum an rebum equidem consequat.<br>
           """


@app.route("/")
def index():
    data = {}
    data["title"] = "Conference<sup>x</sup>"
    data["subtitle"] = "June 1 2016 @ Living Arts Centre"
    data["persons"] = add_people()
    data["table"] = add_table()
    data["location"] = add_location()
    data["google_maps"] = google_maps()
    data["about"] = add_about()
    data["prices"] = add_prices()
    data["faq"] = add_faq()
    data["apply_text"] = add_apply_text()

    data["show_location"] = True
    data["show_program"] = True
    data["show_ticket_button"] = True
    data["show_speaker_button"] = True

    return render_template("index.html", data=data)
