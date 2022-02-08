# from flask import Blueprint
from flask import Blueprint, render_template

pages = Blueprint(__name__, "pages")

@pages.route("/")
def home():
    # return "<p>lettsss goooooo</p>"
    return render_template("index.html")

