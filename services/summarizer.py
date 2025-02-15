#from summarizer import Summarizer,TransformerSummarizer
#bert_model = Summarizer()

import os
from pathlib import Path
from joblib import load

# base_dir = Path(__file__).resolve().parent.parent
# file_path = os.path.join(base_dir,'trainer', 'models', 'bert_summarizer.joblib')
# bert_model = load(file_path)

def summarize(text_to_summarize):
    #bert_summary = ''.join(bert_model(text_to_summarize, min_length=30))
    bert_summary = ""
    return bert_summary