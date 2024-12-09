from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/baixar')
def baixar_video():
    url = request.args.get('url')
    if not url:
        return jsonify({'success': False, 'message': 'URL inválido'}), 400

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.join(os.getcwd(), 'downloads')
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        
        stream.download(download_path)
        return jsonify({'success': True, 'message': 'Vídeo baixado com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
