from flask import Flask
from flask_migrate import Migrate
from server.models import db, Customer, Item, Review


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Review Lab</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)