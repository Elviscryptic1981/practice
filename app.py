from flask import Flask
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recap.db"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/users')
def users():
    users = User.query.all()
    print(users)
    return 'users'
    

@app.route('/')
def hello_world():
    return 'Welcome to flask'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
