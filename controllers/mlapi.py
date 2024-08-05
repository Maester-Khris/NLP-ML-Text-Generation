from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flasgger import swag_from
from services.summarizer import summarize


Class Summarizer(Resource):
     @swag_from({
        'tags': ['Transformer BERT summarizer'],
        "parameters":[
            {
                "name": "text",
                "in": "body",
                "type": "string",
                "example":{
                    "text":"Un nuage de fumée juste après l’explosion, le 1er juin 2019. Une déflagration dans une importante usine d’explosifs du centre de la Russie a fait au moins 79 blessés samedi 1er juin... ",
                },
                "required": "true",
                "description": "Provide a text as input to summarize"
            },
        ],
        "responses":{
            200:{
                'description': "Display the number of word of the input text, same for summarized text and then provide the full content of the summarized text",
                'content':{
                    'application/json':{
                        "data": {
                            "input_text_word_count": 12,
                            "summarized_text_word_count": 12,
                            "summarized_text": "Un nuage de fumée juste après l’explosion, le 1er juin 2019..."
                        }
                    }
                }
            },
            500:{
                'description': "Something went wrong during the process.",
                'content':{
                    'application/json':{
                        "message": "check the format of your input data"
                    }
                }
            }
        }
    })
    def post(self):
        """
        This endpoint is used to perform text summarization on a text content passed as parameter in request body.
        """
        userinput = request.get_json()
        summarized_text = summarize(userinput['text'])
        return {"task result":{
            "input_text_word_count": len(userinput['text'].split()),
            "summarized_text_word_count": len(summarized_text.split()),
            "summarized_text": summarized_text
        }}