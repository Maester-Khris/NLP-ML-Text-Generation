from flask import Flask, render_template
from flask_blueprint import index_bp, summarizer_bp
from flask_restful import Api, Resource
from flasgger import Swagger
from controllers.api import WelcomeLetsgo
from controllers.mlapi import Summarizer, Augmenter




def create_app():
    app = Flask(__name__)

    # ===== configuring rest api
    api = Api(app)

    # ===== configuring swagger
    app.config['SWAGGER'] = {
        'title': 'Text Ninja NLP and ML API',
        'uiversion': 3,
        'template': './resources/flasgger/swagger_ui.html'
    }
    template = {
        "swagger": "2.0",
        "info": {
            "title": 'Text Ninja NLP and ML API',
            "description": """This API was developed using Python Flask and Transformer ML models to resolve some NLP problems related to the text generation problematic.  Important Notes: 
            our api is actually non functioanl due to the limitation of our hosting provider that doesn't allow us to make live inference in the production environment. We are currently working on this. Thank you 🙏""",
            "version": "1.0"
        }
    }
    swagger = Swagger(app, template=template)
    api.add_resource(WelcomeLetsgo, '/api/')
    api.add_resource(Summarizer, '/api/summarize')
    api.add_resource(Augmenter, '/api/augment')

    # ===== configuring templates blueprint
    app.register_blueprint(index_bp)
    app.register_blueprint(summarizer_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=3000, debug=True, use_reloader=True)

    