import json
import re

import os
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types
from fastapi import FastAPI

app = FastAPI()
# Function to fetch transcript
def get_youtube_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = ""
    for entry in transcript:
        full_text += f"{entry['start']:.2f}s: {entry['text']}\n"
    return full_text


# Function to generate JSON summary using Gemini
def summarize_transcript_with_gemini(transcript_text):
    client = genai.Client(api_key="AIzaSyB5ydv-_eICfMUrQKmacj1hbF3ziXZszzU")

    model = "gemini-2.0-flash"

    prompt = f"""
Based on the following YouTube transcript, return a brief summary of the topic below in JSON format only:

Transcript:
{transcript_text}

Format:
{{
    "topic_name": "name of topic",
    "topic_summary": "summary of topic"
}}
"""

    response = client.models.generate_content(
        model=model,
        contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
        config=types.GenerateContentConfig(response_mime_type="text/plain")
    )

    # Gemini returns a single content object (not stream)
    return response.text

def get_video_id_from_url(url):
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[-1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL format.")


def clean_and_parse_gemini_json(response_text):
    # Remove triple backticks and language identifier if present
    cleaned = re.sub(r"```json|```", "", response_text).strip()

    # Unescape newlines and other escaped characters
    cleaned = cleaned.encode().decode('unicode_escape')

    # Convert string to Python dict
    try:
        parsed_json = json.loads(cleaned)
        return parsed_json
    except json.JSONDecodeError as e:
        print("[ERROR] Failed to parse JSON:", e)
        return None


# Main function
def main():
    # Example video ID — replace with actual one
    video_id = get_video_id_from_url(url="https://www.youtube.com/watch?v=f5-xJfVZE4c")

    print("[INFO] Fetching YouTube transcript...")
    transcript = get_youtube_transcript(video_id)

    print("[INFO] Sending transcript to Gemini for summarization...")
    summary = summarize_transcript_with_gemini(transcript)

    print("\n=== Summary Output ===")
    print(summary)

@app.get("/summarize")

def summarize_youtube_video(url: str):
    """
    Endpoint to summarize a YouTube video given its URL.
    Example URL: http://localhost:8000/summarize?url=https://www.youtube.com/watch?v=f5-xJfVZE4c
    """
    video_id = get_video_id_from_url(url)
    transcript = get_youtube_transcript(video_id)
    if not transcript:
        return {"error": "Transcript not available for this video."}
    summary = summarize_transcript_with_gemini(transcript)
    return clean_and_parse_gemini_json(summary)

