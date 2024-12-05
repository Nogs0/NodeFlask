from flask import Flask, request, jsonify
from textblob import TextBlob
from yt import *

app = Flask(__name__)

LINK_VALIDO = "https://www.youtube.com/watch?"

@app.route('/analyze', methods=['GET'])
def analyze_text():
    url = request.args.get('url')  

    if not url:
        return jsonify({"error": "Parâmetro 'url' é necessário!"}), 400

    url_split = url.split("v=")
    url_youtube = url_split[0]
    if url_youtube != LINK_VALIDO:
        return {
            "text": "Insira um link válido."
        }
    video_id = url_split[-1]
    comentarios = Get_Comments(video_id=video_id)  

    results = []
    for i, comentario in enumerate(comentarios):
        analysis = TextBlob(comentario)
        result = {
            "index": i,
            "text": comentario,
            "polarity": analysis.sentiment.polarity,  
            "subjectivity": analysis.sentiment.subjectivity,  
        }
        results.append(result)

    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000)
