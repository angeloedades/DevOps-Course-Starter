import os
from flask import Flask, render_template
from todo_app.flask_config import Config
from todo_app.trello import trello_handler

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def app_index():
    list_of_cards = trello_handler.get_board_cards(os.getenv("TRELLO_BASE_BOARD"))
    return render_template("index.html", list_of_cards=list_of_cards)


@app.route("/configuration")
def app_configuration():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
