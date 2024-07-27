from flask import Flask, render_template, request, jsonify, send_file
import requests
import tempfile
import logging
import time
import os
from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
import markdown2

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

logging.basicConfig(level=logging.DEBUG)

API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBc9a2I57vkHjVYhJ42QkzMxZvwq0BY44k"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    video_id = data['videoId']
    prompt_text = data['promptText']
    try:
        transcript = get_transcript(video_id)
        gemini_response = generate_story(prompt_text + transcript)
        logging.debug(f"API response: {gemini_response}")
        if gemini_response and 'candidates' in gemini_response:
            story_content = extract_story_content(gemini_response)
            if story_content:
                markdown_content = markdown2.markdown(story_content)
                return jsonify({'summary': markdown_content})
        return jsonify({'error': 'Failed to generate story content. Please try again.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([t['text'] for t in transcript])
        return text.strip()
    except Exception as e:
        raise Exception('Failed to fetch transcript: ' + str(e))

def generate_story(prompt):
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(API_ENDPOINT, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_story_content(response):
    candidates = response['candidates']
    if candidates:
        content = candidates[0]['content']
        if content:
            parts = content['parts']
            if parts:
                return parts[0].get('text', '')
    return None

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
