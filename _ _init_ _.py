from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'afa9bec304152f1e369aa69c2199e3b9949e8fe9578f2183'

    # Import Blueprints
    from .routes import main_bp
    
    # Register Blueprints
    app.register_blueprint(main_bp)

    return app