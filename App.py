from flask import Flask
from config import Config
from models.user import db
from routes.users import user_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
