# Python 3.12+
import pyttsx3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceEngine:
    """Gerencia a síntese de voz (TTS) do JARVIS."""
    
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self._configure_voice()

    def _configure_voice(self) -> None:
        voices = self.engine.getProperty('voices')
        # Tenta encontrar uma voz masculina e calma
        # No Windows, geralmente o índice 0 ou vozes com 'Ricardo' ou 'Daniel'
        self.engine.setProperty('rate', 175)  # Velocidade controlada
        self.engine.setProperty('volume', 0.9)
        
        for voice in voices:
            if "portuguese" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text: str) -> None:
        logger.info(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()