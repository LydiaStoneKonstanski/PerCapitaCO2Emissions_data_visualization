from os import path
from flask import Flask

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    #TODO this is where the db gets called
    #from flask_co2.models import db
    #db.init_app(app)

    with app.app_context():
        #TODO what goes here? It's not the 'forum/circus'
        #if not os.path.exists('forum/circus'):
            #db.create_all()
        #return app

