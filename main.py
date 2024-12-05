from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "Parâmetro 'text' é necessário!"}), 400

    lines = text.splitlines()

    results = []

    for i, text in  enumerate(lines):
        analysis = TextBlob(text)
        result = {
            "index": i,
            "text": text,
            "polarity": analysis.sentiment.polarity,  
            "subjectivity": analysis.sentiment.subjectivity,  
        }
        results.append(result)

    return jsonify(results)

@app.route('/analyze', methods=['GET'])
def dica():
    return "<p>O texto precisa ser enviado no corpo da requisição usando o parâmetro \'text\'. </p>"
if __name__ == '__main__':
    app.run(port=5000)
