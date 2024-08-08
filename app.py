import os
from flask import Flask
from flasgger import Swagger
from controllers.api import WelcomeLetsgo
from controllers.mlapi import Summarizer, Augmenter
from flask_restful import Api, Resource

def create_app():
    app = Flask(__name__)
    # ===== configuring rest api
    api = Api(app)
    # ===== configuring swagger
    app.config['SWAGGER'] = {
        'title': 'Let\'s GO ML API',
        'uiversion': 3,
        'template': './resources/flasgger/swagger_ui.html'
    }
    template = {
        "swagger": "2.0",
        "info": {
            "title": 'Let\'s GO ML API',
            "description": "This API was developed using Python Flask and Transformer ML models to resolve some NLP problems related to the text generation problematic",
            "version": "1.0"
        }
    }
    swagger = Swagger(app, template=template)

    api.add_resource(WelcomeLetsgo, '/')
    api.add_resource(Summarizer, '/summarize')
    api.add_resource(Augmenter, '/augment')
    
    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

    