from flask import Blueprint
from flask_assets import Bundle, Environment
from .views import index

js = Bundle('materialize.js', output='gen/main.js')
css = Bundle('materialize.css', 'index.css', output='gen/main.css')

bp = Blueprint("webui", __name__, template_folder="templates", static_folder='static')
bp.add_url_rule("/", view_func=index)


def init_app(app):
    assets = Environment(app)
    assets.register('main_js', js)
    assets.register('main_css', css)
    app.register_blueprint(bp)
