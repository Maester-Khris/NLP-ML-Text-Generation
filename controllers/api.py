from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flasgger import swag_from

# INmemory DB
data = [{'id': 1, 'name': 'Ashley'}, {'id': 2, 'name': 'Kate'}, {'id': 3, 'name': 'Joe'}]
summarizer = Blueprint('Summarizer', __name__)


class WelcomeLetsgo(Resource):
    @swag_from({
        'tags': ['Home directory'],
        'responses':{
            200:{
                'description': "The text was successful parsed.",
                'content':{
                    'application/json':{}
                }
            }
        }
    })
    def get(self):
        """
        This is an example endpoint which returns a simple message.
        """
        return {'message':"Welcome to Lets go ML API!"}


class Items(Resource):
    @swag_from({
        'tags': ['Transformer BERT summarizer'],
        'responses':{
            200:{
                'description': "A status code 200 means successful and returns a list of items.",
                'content':{
                    'application/json':{
                        "data": data
                    }
                }
            }
        }
    })
    def get(self):
        """
        This endpoint returns a list of items.
        """
        return {'items': data}

    @swag_from({
        'tags': ['Transformer BERT summarizer'],
        "parameters":[
            {
                "name": "data",
                "in": "body",
                "type": "string",
                "example":{
                    "name":"Boutlefika",
                    "power":30
                },
                "required": "true",
                "description": "input text and sum power to summarize"
            },
        ],
        "responses":{
            200:{
                'description': "Display the updated list of items.",
                'content':{
                    'application/json':{
                        "data": data
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
        This endpoint is used to add another element to the list of existings items.
        """
        userdata = request.get_json()
        print(f"the user sent name {userdata['name']}")
        newin = len(data)+1
        data.append({'id':newin, 'name':userdata['name']})
        return {"new items":data}
