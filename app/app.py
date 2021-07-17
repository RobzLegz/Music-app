from flask import Flask
from peewee import SqliteDatabase
import datetime


app = Flask(__name__)

app.config["SECRET_KEY"] = "s#?/12sd3ēadģč»«4’54~sFg23ašļģ('/sm$»«4fGF=!')"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

db = SqliteDatabase("database.db")

def register_blueprints(app):
    from components.account.views import account
    from components.home.views import home

    app.register_blueprint(account)
    app.register_blueprint(home)