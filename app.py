
from flask import Flask, request, jsonify, send_file
import yt_dlp
from io import BytesIO

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data['videoUrl']
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        url = info['formats'][0]['url']
        filename = info['title'] + '.' + info['formats'][0]['ext']
        response = send_file(
            BytesIO(),
            as_attachment=True,
            attachment_filename=filename,
            mimetype='video/' + info['formats'][0]['ext']
        )
        return response

if __name__ == '__main__':
    app.run(debug=True)
