import os
from dotenv import load_dotenv
from .voice_processor import VoiceProcessor
from .patient_agent import PatientAgent
from .config import OPENAI_API_KEY

class TherapySession:
    def __init__(self):
        self.voice_processor = VoiceProcessor()
        self.patient_agent = PatientAgent(api_key=OPENAI_API_KEY)
        
    def start_session(self):
        """Start an interactive therapy session"""
        print("Starting therapy session...")
        print("Patient Profile:", self.patient_agent.profile)
        print("\nYou can start speaking with your patient now.")
        
        while True:
            # Listen to therapist's input
            therapist_input = self.voice_processor.listen_to_therapist()
            
            if not therapist_input:
                continue
                
            if "end session" in therapist_input.lower():
                print("Ending session...")
                break
                
            # Process input and generate patient response
            patient_response = self.patient_agent.process_therapist_input(therapist_input)
            
            # Speak the response
            self.voice_processor.speak_response(patient_response)
            
    def save_session(self, filename: str):
        """Save the session history to a file"""
        history = self.patient_agent.get_conversation_history()
        with open(filename, 'w') as f:
            for entry in history:
                role = "Therapist" if entry["role"] == "user" else "Patient"
                f.write(f"{role}: {entry['content']}\n")

def main():
    load_dotenv()
    session = TherapySession()
    session.start_session()
    
if __name__ == "__main__":
    main()
