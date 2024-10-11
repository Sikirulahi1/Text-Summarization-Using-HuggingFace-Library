from transformers import pipeline, AutoTokenizer, AutoModelWithLMHead

class Summarizer:
    def __init__(self, text):
        self.text = text
    def summarize(self):
        summarizer = pipeline("summarization", model="Falconsai/text_summarization")

        summary = summarizer(self.text, max_length=425, min_length=30, do_sample=False)
        summary_text = summary[0]['summary_text']
        return summary_text