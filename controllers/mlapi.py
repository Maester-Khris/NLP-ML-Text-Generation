from flask import Blueprint, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flasgger import swag_from
from services.summarizer import summarize
from services.augmenter import insert_context_keywords


class Summarizer(Resource):
    @swag_from({
        'tags': ['BERT Summarizer'],
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


class Augmenter(Resource):
    @swag_from({
        'tags': ['BERT Augmenter with Next entity prediction and Spacy'],
        "parameters":[
            {
                "name": "user_data",
                "in": "body",
                "type": "string",
                "example":{
                    "input_text":"Un nuage de fumée juste après l’explosion, le 1er juin 2019. Une déflagration dans une importante usine d’explosifs du centre de la Russie a fait au moins 79 blessés samedi 1er juin... ",
                    "keywords":["Tech", "Machine learning", "Projet"]
                },
                "required": "true",
                "description": ""
            },
        ],
        "responses":{
            200:{
                'description': "Return a text with augmented data that represent context keyword, in a way that the new sentence has a consistent meaning.",
                'content':{
                    'application/json':{
                        "data": {
                            "augmented_text": "Un nuage de fumée juste après l’explosion, le 1er juin 2019 au cameroun",
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
        This endpoint is used to perform data augmentation on a text or sentence content. The user will need to provide a text and a list for keyword considered a context data to add.
        """
        userinput = request.get_json()
        text_sentences= userinput['input_text'].split(".")
        augmented_sentences = []
        # apply augmentation
        for sentence in text_sentences:
            new_s, keys =insert_context_keywords(sentence.strip(), userinput['keywords'])
            augmented_sentences.append(new_s)

        # rejoin augmented sentencse
        new_text = ". ".join(augmented_sentences)
        return {"task result":{
            "augmented_text": new_text,
        }}
        
        # used as placeholder
        # return {
        #     "task result":{
        #         "augmented_text":"That's it"
        #     }
        # }