# from flask import Blueprint
from email import message
from flask import Blueprint, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from app import SchoolData
from .common import db
pages = Blueprint(__name__, "pages")



@pages.route("/")
def home():
    # return "<p>lettsss goooooo</p>"
    return render_template("index.html")

@pages.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        school = request.form['school']
        first = request.form['first']
        last = request.form['last']
        if school == '' or first == '' or last == '':
            return render_template('index.html', message="Must fill out all fields")
        if db.session.query(SchoolData).filter(SchoolData.school == school).count() == 0:
            data = SchoolData(school, first, last)
            db.session.add(data)
            db.session.commit()
            return render_template("formSubmit.html")
