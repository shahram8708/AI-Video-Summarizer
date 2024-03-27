import tempfile
from flask import Flask, request, jsonify, render_template, send_file
from youtube_transcript_api import YouTubeTranscriptApi
from google.cloud import speech_v1p1beta1 as speech
from fpdf import FPDF
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    video_id = data['videoId']
    try:
        transcript = get_transcript(video_id)
        return jsonify({'summary': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([t['text'] for t in transcript])
        return text.strip()  
    except Exception as e:
        raise Exception('Failed to fetch transcript: ' + str(e))

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    data = request.json
    text = data['text']
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        filename = tmpfile.name
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(filename)

    response = send_file(filename, as_attachment=True, download_name="transcript.pdf")
    
    try:
        time.sleep(1)  
        os.remove(filename) 
    except Exception as e:
        print(f"Error deleting the file: {e}")
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
