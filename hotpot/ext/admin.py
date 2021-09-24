from flask_admin import Admin

admin = Admin()

def init_app(app):
    admin.init_app(app)