from hotpot.ext.database import db


class Flavor(db.Model):
    __tablename__ = 'flavors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    items = db.relationship('Item', backref='owned_flavor', lazy=True)
    order_id = db.Column(db.Integer(), db.ForeignKey('orders.id'))


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    type = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float())
    amount = db.Column(db.Integer())
    flavor_id = db.Column(db.Integer(), db.ForeignKey('flavors.id'))


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    observation = db.Column(db.String())
    delivery_price = db.Column(db.Float(), nullable=False)
    final_price = db.Column(db.Float(), nullable=False)
    flavors = db.relationship('Flavor', backref='orders')
