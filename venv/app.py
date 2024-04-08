# app.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    # Aquí puedes configurar tu aplicación, registrar blueprints, etc.
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
