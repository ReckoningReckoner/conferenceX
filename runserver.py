from conferenceX.flask_app import app
import conferenceX.views

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
