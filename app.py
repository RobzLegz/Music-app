from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "s#?/12sd3ēadģč»«4’54~sFg23ašļģ('/sm$»«4fGF=!')"


def register_blueprints(app):
    from components.account.views import account

    app.register_blueprint(account)