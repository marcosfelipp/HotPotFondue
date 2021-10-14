from flask import abort, render_template
from hotpot.models import Flavor


def index():
    return render_template("index.html")


def order_page():
    flavors = Flavor.query
    flavors_count = flavors.count()
    return render_template("order.html", flavors=flavors, flavors_count=flavors_count)
