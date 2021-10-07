from hotpot.ext.database import db


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    type = db.Column(db.String(), nullable=False)
    amount = db.Column(db.Integer())


class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    observation = db.Column(db.String())
    items = db.relationship('Item')
