from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFax!"
    
    # register blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    #register fax bp
    from . import fax
    app.register_blueprint(fax.bp)

    return app
