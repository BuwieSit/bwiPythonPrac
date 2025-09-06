from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    user = "buwie"
    return render_template('index.html', name=user)