from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/lp02_team_7_mock_server_development'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

server = Manager(app)
server.add_command('db', MigrateCommand)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    tele = db.Column(db.String(128))
    age = db.Column(db.Integer)

if __name__ == '__main__':
    server.run()