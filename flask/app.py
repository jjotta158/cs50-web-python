import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    my_birthday = now.month == 1 and now.day == 29
    names = ['jairo', 'pedro', 'junior']
    return render_template("index.html", my_birthday=my_birthday, names=names)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/hello", methods=["POST"])
def hello():
    # pega o valor enviado através de um formulário
    name = request.form.get("name")
    return render_template("more.html", name=name)
