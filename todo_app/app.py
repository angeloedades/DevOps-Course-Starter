from flask import Flask, render_template
import todo_app.data.session_items as session
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    items = session.get_items()
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run()
