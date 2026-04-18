# Python 3.12+
import speech_recognition as sr
import threading
import logging
import sys
from voice_engine import VoiceEngine
from sensors import SoundSensor
from actions import JarvisActions
from config import settings

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class Jarvis:
    def __init__(self) -> None:
        self.voice = VoiceEngine()
        self.recognizer = sr.Recognizer()
        self.actions = JarvisActions()
        self.is_active = True
        self.wake_word = settings.JARVIS_NAME.lower()

    def toggle_state(self) -> None:
        """Alterna o estado de escuta via palma."""
        self.is_active = not self.is_active
        status = "ativo" if self.is_active else "em espera"
        self.voice.speak(f"Sistema {status}, senhor.")

    def process_command(self, text: str) -> None:
        text = text.lower()
        
        match text:
            case t if "trabalho" in t:
                response = self.actions.open_work_mode()
            case t if "lazer" in t:
                response = self.actions.open_leisure_mode()
            case t if "status" in t:
                response = self.actions.get_system_status()
            case t if "descansar" in t:
                response = self.actions.stop_all()
                self.is_active = False
            case t if "encerrar sistema" in t:
                self.voice.speak("Desconectando. Até logo, senhor.")
                sys.exit()
            case _:
                response = "Comando não reconhecido pela minha base de dados."

        self.voice.speak(response)

    def listen_loop(self) -> None:
        """Loop principal de reconhecimento de voz."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.voice.speak("Sistemas online. Estou ouvindo.")

            while True:
                if not self.is_active:
                    continue

                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = self.recognizer.recognize_google(audio, language="pt-BR")
                    
                    if self.wake_word in command.lower():
                        # Remove a palavra de ativação para processar o comando puro
                        pure_command = command.lower().replace(self.wake_word, "").strip()
                        if pure_command:
                            self.process_command(pure_command)
                        else:
                            self.voice.speak("Sim, senhor?")

                except (sr.WaitTimeoutError, sr.UnknownValueError):
                    continue
                except Exception as e:
                    logging.error(f"Erro na escuta: {e}")

    def run(self) -> None:
        # Inicia sensor de palmas em uma thread separada
        sensor = SoundSensor(threshold=settings.CLAP_THRESHOLD)
        clap_thread = threading.Thread(
            target=sensor.listen_for_clap, 
            args=(self.toggle_state,), 
            daemon=True
        )
        clap_thread.start()

        # Inicia loop de voz principal
        try:
            self.listen_loop()
        except KeyboardInterrupt:
            logging.info("Encerrando JARVIS via teclado.")

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()