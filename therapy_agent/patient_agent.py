from openai import OpenAI
from typing import Dict, List
import json
from .config import DEFAULT_PATIENT_PROFILE, RESPONSE_TEMPERATURE

class PatientAgent:
    def __init__(self, api_key: str, profile: Dict = None):
        self.client = OpenAI(api_key=api_key)
        self.profile = profile or DEFAULT_PATIENT_PROFILE
        self.conversation_history = []
        
    def _create_system_prompt(self) -> str:
        """Create the system prompt based on patient profile"""
        return f"""You are a therapy patient named {self.profile['name']}, age {self.profile['age']}.
Background: {self.profile['background']}
Personality: {self.profile['personality']}
Speech Style: {self.profile['speech_style']}

Respond naturally as this patient would in a therapy session. Show appropriate emotional responses 
and psychological patterns. Maintain consistency with previous responses and your background story.
"""

    def process_therapist_input(self, therapist_input: str) -> str:
        """Process therapist's input and generate patient's response"""
        # Add therapist's input to conversation history
        self.conversation_history.append({"role": "user", "content": therapist_input})
        
        # Prepare messages for the API
        messages = [
            {"role": "system", "content": self._create_system_prompt()},
            *self.conversation_history
        ]
        
        try:
            # Generate response using OpenAI
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=RESPONSE_TEMPERATURE,
                max_tokens=150
            )
            
            patient_response = response.choices[0].message.content
            
            # Add response to conversation history
            self.conversation_history.append({"role": "assistant", "content": patient_response})
            
            return patient_response
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I'm not feeling well right now. Can we take a moment?"
            
    def get_conversation_history(self) -> List[Dict]:
        """Return the conversation history"""
        return self.conversation_history
