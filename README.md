# 🎥 YouTube Transcript Summarizer using Gemini Flash

A lightweight API that fetches transcripts from any YouTube video and generates a JSON summary using **Gemini 1.5 Flash (Gemini 2.0 Flash)** via the Google Generative AI SDK.

---

## 🚀 Project Overview

This is my second project as a **Generative AI Developer Intern at [AIWallah](https://www.linkedin.com/company/aiwallah/)**. It demonstrates how to extract insights from long-form video content using GenAI models.

**Given a YouTube video ID**, this tool:

1. Extracts the transcript using [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
2. Summarizes the transcript into a clean JSON response via Gemini Flash (Gemini 1.5)
3. Returns structured output with `topic_name` and `topic_summary`

---

## 🧠 Tech Stack

* Python 3.10+
* Google Generative AI SDK (`google-genai`)
* Gemini 1.5 Flash model
* youtube-transcript-api
* Postman (for testing endpoints)

---

## 💠 Setup Instructions

### 🔐 1. Get Your Gemini API Key

* Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
* Copy your API key

### 🧪 2. Install Dependencies

```bash
pip install google-genai youtube-transcript-api
```

### 📁 3. Set Environment Variable

```bash
export GEMINI_API_KEY=your_api_key_here
```

On Windows (CMD):

```cmd
set GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### In Python script (`main.py`)

```python
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types

# Use get_youtube_transcript(video_id)
# Then pass transcript to summarize_transcript_with_gemini(transcript_text)
```

### Or test with Postman

1. Run the script as an API or wrap with Flask/FastAPI.
2. Use Postman to send a video ID.
3. Get back a JSON response with summary.

---

## ✅ Sample Output

```json
{
  "topic_name": "Suspension of the Shimla Agreement",
  "topic_summary": "Following a terror attack in India, Pakistan has suspended the 1972 Shimla Agreement, a peace treaty signed after the 1971 Indo-Pakistani war which led to the creation of Bangladesh. The treaty established principles for future interactions, including converting the 1971 ceasefire line into the line of control, and settling differences through bilateral negotiations. Pakistan's suspension of the agreement has wide ranging implications, and means the line of control no longer exists."
}
```

---

## 📌 Limitations

* Only works if the video has captions (manual or auto-generated)
* Gemini Flash has context length limitations (\~8k tokens)
* Long transcripts are processed in one go; chunking not yet implemented

---

## 📂 Folder Structure

```bash
youtube-transcript-summarizer/
│
├── main.py              # Main script to extract + summarize
├── README.md            # You're here!
├── requirements.txt     # (Optional) Dependencies list
```

---

## 🙌 Acknowledgments

* Thanks to the team at **AIWallah** for this amazing learning opportunity
* Inspired by real-world use cases of news summarization and lecture insights

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/your-profile) or raise issues if you have suggestions or bugs.

---

## ⭐️ Give it a Star!

If you find this project helpful, consider starring ⭐ the repository!

---

## 🧠 Future Improvements

* Add chunking for longer transcripts
* Wrap in Flask API for easy deployment
* Support batch video summarization

---

\#AIWallah #GenAI #GeminiFlash #YouTubeSummarizer #TranscriptAI #PostmanDemo #PythonAI #InternshipProject #GoogleGemini #GenerativeAI
