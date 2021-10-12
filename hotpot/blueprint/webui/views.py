from flask import abort, render_template


def index():
    return render_template("index.html")


def order_page():
    return render_template("order.html")
