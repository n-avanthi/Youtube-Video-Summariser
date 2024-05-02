from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Import CORS module
app = Flask(__name__)
CORS(app)

# Configure the API key for Generative AI
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Function to generate content using GenerativeModel
def generate_content(prompt, video_summary):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + " " + video_summary)
    return response.text

@app.route('/qa')
def qa_api():
    url = request.args.get('url', '')
    question = request.args.get('question', '')
    video_id = url.split('=')[1]
    transcript = get_transcript(video_id)
    summary = get_summary(transcript)
    response = generate_content(question, summary)
    return response, 200

@app.route('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    transcript = get_transcript(video_id)
    summary = get_summary(transcript)
    return summary, 200

@app.route('/conversation')
def conversation_api():
    url = request.args.get('url', '')
    prompt = request.args.get('prompt', '')
    video_id = url.split('=')[1]
    transcript = get_transcript(video_id)
    summary = get_summary(transcript)
    response = generate_content(prompt, summary)
    return response, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    summary = ''
    max_length = 512  # Maximum sequence length supported by the model
    for i in range(0, len(transcript), max_length):
        segment = transcript[i:i+max_length]
        summary += segment + ' '
    return summary

if __name__ == '__main__':
    app.run()
