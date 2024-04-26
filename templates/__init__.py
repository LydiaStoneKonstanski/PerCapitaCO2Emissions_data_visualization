import os.path

from flask import Flask
#TODO imports from other files like auth, comments, posts, etc.

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
#TODO register all the blueprints from the other files.
    app.register_blueprint()

    # from co2.models import db
    # db.init_app(app)

#     with app.app_context():
#         #add some routes
# # #TODO add pathname
# #         if not os.path.exists('')
# #             # db.create_all()
# #         return app