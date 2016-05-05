from conferenceX import app
from flask import render_template


def add_people(data):
    desc = """
           Id sonet soluta virtute ius, vim atqui graecis ullamcorper ut,
           cum in nibh novum. Ipsum sanctus has eu.
           In sumo discere pri, quo te vivendum voluptatum.
           """

    data["persons"] = []
    data["persons"].append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/brynn/128.jpg",
           "id": "person1",
           "name": "Ya Bish",
           "description": desc}
          )

    data["persons"].append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/dustin/128.jpg",
           "id": "person2",
           "name": "Rel Y. High",
           "description": desc}
          )

    data["persons"].append(
          {"url":
           "https://s3.amazonaws.com/uifaces/faces/twitter/connor_gaunt/" +
           "128.jpg",
           "id": "person3",
           "name": "N. Olips",
           "description": desc}
          )

    data["persons"].append(
          {"url":
           "http://cdn2.blog-media.zillowstatic.com/8/Chris-Morrison-Facebook-c7ea82-300x300.jpg",
           "id": "person4",
           "name": "No Treal",
           "description": desc}
          )


def add_table(data):
    data["table"] = """
                    <tbody>
                        <tr>
                            <td>3:00</td>
                            <td>Eclair</td>
                        </tr>
                        <tr>
                            <td>3:30</td>
                            <td>Jellybean</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                        <tr>
                            <td>4:00</td>
                            <td>Lollipop</td>
                        </tr>
                    </tbody>
                    """


def add_location(data):
    data["location"] = """
                       <h5> Address </h5>
                       <hr>
                       <p class="flow-text">
                           2265 Erin Centre Blvd, Mississauga ON
                       </p>

                       <h5> Date and time</h5>
                       <hr>
                       <p class="flow-text">June 1 2016 from 3 pm to 7 pm</p>
                       """


def google_maps(data):
    data["google_maps"] = """ <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2891.2543947112094!2d-79.71834638499719!3d43.559581966498236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882b418b3d8ade65%3A0xba2d4d9099046a2!2sJohn+Fraser+Secondary+School!5e0!3m2!1sen!2sca!4v1462459740942" width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>"""


@app.route("/")
def index():
    data = {}
    add_people(data)
    add_table(data)
    add_location(data)
    google_maps(data)

    return render_template("index.html", data=data)
