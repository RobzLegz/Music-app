from flask import Flask


app = Flask(__name__)
from components.account.views import account

app.register_blueprint(account)

# def register_blueprints(app):
#     from components.account.views import account

#     app.register_blueprint(account)