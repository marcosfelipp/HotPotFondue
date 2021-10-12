from hotpot.models import Order, Item, Flavor
from hotpot.ext.database import db


def init_app(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        flavor1 = Flavor(name='chocolate')
        flavor2 = Flavor(name='carne')
        flavor3 = Flavor(name='queijo')

        db.session.add_all([flavor1, flavor2, flavor3])
        db.session.commit()

        item1 = Item(name='Brocolis', type='', price=0, amount=10)
        item1.flavor_id = Flavor.query.filter_by(name='queijo').first().id

        item2 = Item(name='Marshmellow', type='', price=0, amount=10)
        item2.flavor_id = Flavor.query.filter_by(name='chocolate').first().id

        db.session.add_all([item1, item2])
        db.session.commit()
