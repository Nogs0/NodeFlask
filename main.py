from flask import Flask, request, jsonify
from textblob import TextBlob
from yt import *


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    url = data.get('url', '')

    if not url:
        return jsonify({"error": "Parâmetro 'url' é necessário!"}), 400

    video_id = url.split("v=")[-1]
    comentarios = Get_Comments(video_id=video_id)

    results = []
    for i, comentario in  enumerate(comentarios):
        analysis = TextBlob(comentario)
        result = {
            "index": i,
            "text": comentario,
            "polarity": analysis.sentiment.polarity,  
            "subjectivity": analysis.sentiment.subjectivity,  
        }
        results.append(result)

    return jsonify(results)

@app.route('/analyze', methods=['GET'])
def dica():
    return "<p>O link do video precisa ser enviado no corpo da requisição usando o parâmetro \'url\'. </p>"
if __name__ == '__main__':
    app.run(port=5000)
