# from distutils.log import debug
from flask import Flask
from pages import pages
from .common import db


app = Flask(__name__)
app.register_blueprint(pages, url_prefix="/")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yoocjyzfjjaglx:38b9c0b18c45d7ab122afdf172c23bfb5fdba6e0da908be0fb889d36eb001230@ec2-3-216-113-109.compute-1.amazonaws.com:5432/ddgva3hrk30lqp'

db.init_app(app)
# db = SQLAlchemy(app)

class SchoolData(db.Model):
    __tablename__='schoolData'
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(100))
    first = db.Column(db.String(100))
    last = db.Column(db.String(100))
    
    def __init__(self, school, first, last):
        self.school = school
        self.first = first
        self.last = last

if __name__ == "__main__":
    app.run(debug=True, port=8000)