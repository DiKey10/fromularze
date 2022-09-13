from flask import Flask, render_template, request
import requests


app = Flask(__name__)

user = {"username": "jamesbond", "password": "superpass123"}


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get("password")

        if username == user['username'] and password == user["password"]:
            return "Jesteś w sytemie. Wiadomość ulegnie samozniszczeniu... "

    return render_template("login_form_post.html")


@app.route("/wybor", methods=["GET", "POST"])
def wybory():
    if request.method == "POST":
        data = request.form
        licz = int(data.get('licz'))
        valut= data.get('walut')
        if valut == "dolar amerykański":
            return str(licz * 4.5998)
        if valut == "dolar australijski":
            return str(licz * 3.168)
        if valut == "dolar kanadyjski":
            return str(licz * 3.548)
        if valut == "funt szterling":
            return str(licz * 5.3763)

    return render_template("wybory.html")


if __name__ == "__main__":
    app.run(debug=True)