from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
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