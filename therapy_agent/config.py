import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Agent Configuration
DEFAULT_PATIENT_PROFILE = {
    "name": "Alex",
    "age": 28,
    "background": "Experiencing mild anxiety and work-related stress",
    "personality": "Initially reserved but opens up gradually",
    "speech_style": "Speaks at a moderate pace, occasionally hesitant",
}

# Conversation Settings
MAX_CONVERSATION_TURNS = 20
RESPONSE_TEMPERATURE = 0.7

# Audio Settings
AUDIO_SAMPLE_RATE = 44100
CHUNK_SIZE = 1024
