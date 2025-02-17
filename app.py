from flask import Flask, render_template, request, jsonify
from transformers import pipeline

summarizer = pipeline("summarization")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    note = request.json['note']
    # Calculate appropriate max_length based on input length
    input_length = len(note.split())
    max_len = min(50, max(25, int(input_length * 0.75)))  # Use 75% of input length
    min_len = max(10, int(max_len * 0.5))  # Use 50% of max length
    summary = summarizer(note, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
