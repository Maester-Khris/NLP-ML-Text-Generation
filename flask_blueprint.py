from flask import Blueprint, render_template

# Create Blueprints
index_bp = Blueprint('index', __name__)
summarizer_bp = Blueprint('summarizer', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')

@summarizer_bp.route('/summarizer')
def test_summarizer():
    return render_template('summarizer.html')