# Library:
- flask
- Flask-RESTful
- flasgger (swagger ui v3)
- bert-extractive-summarizer
- dataset and models to download locally, avoid load from internet:
    * bert-large-uncased, we first supposte that pip install bert-extractive-summarizer will also install transform, and the model is available inside
    * add command in docker file to donwload spacy language model: python -m spacy download en_core_web_sm 

