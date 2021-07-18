from app.app import app, register_blueprints, register_db_models

if __name__ == "__main__":
    register_blueprints(app)
    register_db_models()

    app.run(host="localhost", port=8080, debug=True)