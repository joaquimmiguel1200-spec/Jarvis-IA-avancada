# Python 3.12+
import numpy as np
import pyaudio
import logging
from collections.abc import Callable

logger = logging.getLogger(__name__)

class SoundSensor:
    """Monitora o ambiente para eventos sonoros como palmas."""
    
    def __init__(self, threshold: float = 0.2) -> None:
        self.threshold = threshold
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()

    def listen_for_clap(self, callback: Callable[[], None]) -> None:
        """Loop bloqueante simples para detectar picos de volume (palmas)."""
        stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        
        try:
            while True:
                data = np.frombuffer(stream.read(self.chunk, exception_on_overflow=False), dtype=np.int16)
                peak = np.average(np.abs(data)) / 32768
                if peak > self.threshold:
                    logger.info("Palma detectada!")
                    callback()
        except Exception as e:
            logger.error(f"Erro no sensor de som: {e}")
        finally:
            stream.stop_stream()
            stream.close()