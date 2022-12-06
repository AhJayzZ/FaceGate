from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.44.135:3306/openapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'person'
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(80), nullable=False)
    state    = db.Column(db.String(80), nullable=False)
    in_time  = db.Column(db.String(80), nullable=False)
    out_time = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Shipment %r>' % self.item
    
    def __init__(self, name, state, in_time, out_time):
        
        self.name = name
        self.state = state
        self.in_time = in_time
        self.out_time = out_time

db.create_all()
db.session.commit()
