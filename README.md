# 🏋️ GYM AI Coach

An AI-powered real-time gym coaching application that analyzes exercise form using computer vision and provides voice feedback.

## ✨ Features
- 📸 Real-time pose detection using MediaPipe
- 🤖 AI coaching feedback via Groq (Llama 3.3 70B)
- 🔊 Voice feedback using gTTS
- 📊 Workout metrics tracking
- 🏃 Supports: Squats, Push-ups, Bicep Curls, Shoulder Press, Lunges

## 🛠️ Tech Stack
- Python
- Streamlit + streamlit-webrtc
- MediaPipe (Pose Detection)
- Groq API (LLM)
- gTTS (Text to Speech)
- SQLite

## 🚀 Run Locally
1. Clone the repo
   git clone https://github.com/sitikanthaprusty2904/Gym_Coach_AI.git

2. Install dependencies
   pip install -r requirements.txt

3. Add your API key in .env
   GROQ_API_KEY=your_key_here

4. Run the app
   streamlit run main.py

## 🔐 Environment Variables
GROQ_API_KEY = your Groq API key