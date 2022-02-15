# Flask_App

Set-ExecutionPolicy -Scope Process -ExecutionPolicy  ByPass

cd venv-flask
.\Scripts\activate

$env:FLASK_ENV="development"

$env:FLASK_APP="app"   

pip packages:

Flask==2.0.2
gunicorn==20.1.0
psycopg2==2.9.3
psycopg2-binary==2.9.3
Flask-SQLAlchemy==2.5.1
SQLAlchemy==1.4.31
