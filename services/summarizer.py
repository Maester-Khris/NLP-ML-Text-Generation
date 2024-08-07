from summarizer import Summarizer,TransformerSummarizer

bert_model = Summarizer()

def summarize(text_to_summarize):
    bert_summary = ''.join(bert_model(text_to_summarize, min_length=30))
    return bert_summary