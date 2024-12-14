import speech_recognition as sr
from elevenlabs import generate, play
import sounddevice as sd
import soundfile as sf
import numpy as np
from typing import Optional

class VoiceProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def listen_to_therapist(self) -> Optional[str]:
        """Record and transcribe therapist's speech"""
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=10)
                print("Processing speech...")
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

    def speak_response(self, text: str, voice_id: str = "default"):
        """Generate and play AI response using ElevenLabs"""
        try:
            audio = generate(
                text=text,
                voice=voice_id,
                model="eleven_monolingual_v1"
            )
            play(audio)
        except Exception as e:
            print(f"Error generating speech: {e}")
            # Fallback to basic TTS if ElevenLabs fails
            self._fallback_tts(text)
