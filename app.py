from flask import Flask, request, jsonify
import yt_dlp
from flask_cors import CORS

app = Flask(__name__)  # Fixed: _name_ to __name__
CORS(app)

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        if not data or 'videoUrl' not in data:
            return jsonify({'error': 'No video URL provided'}), 400
        video_url = data['videoUrl']
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({'message': 'Video downloaded successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':  # Fixed: _name_ to __name__ and _main_ to __main__
    app.run(debug=True, port=5000)  # Fixed formatting