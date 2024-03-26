from flask import Flask, request, jsonify, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from google.cloud import speech_v1p1beta1 as speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
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


def summarize_transcript(transcript):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=transcript.encode('utf-8'))
    config = speech.RecognitionConfig(language_code="en-US")

    response = client.recognize(config=config, audio=audio)

    summarized_text = ''
    for result in response.results:
        summarized_text += result.alternatives[0].transcript + ' '

    return transcript.strip() 

if __name__ == '__main__':
    app.run(debug=True)
