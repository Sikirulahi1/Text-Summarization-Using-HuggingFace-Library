from summarizer import app
from flask import render_template, redirect, url_for, request
from summarizer.forms import SummarizeText
from summarizer.models import UserModel
from components.summarizer import Summarizer

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/summarizer', methods=['GET', 'POST'])
def summarizer_page():
    form = SummarizeText()
    summary = None
    if form.validate_on_submit():
        text = form.text.data
        summarizer = Summarizer(text)
        summary = summarizer.summarize()
    return render_template('summarizer.html', form=form, summary=summary)