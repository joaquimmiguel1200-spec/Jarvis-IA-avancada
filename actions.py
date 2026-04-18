# Python 3.12+
import webbrowser
import subprocess
import psutil
import pyautogui
import logging
from config import settings

logger = logging.getLogger(__name__)

class JarvisActions:
    """Define as automações de sistema que o JARVIS pode executar."""

    @staticmethod
    def open_work_mode() -> str:
        webbrowser.open("https://github.com")
        webbrowser.open("https://stackoverflow.com")
        subprocess.Popen([settings.VS_CODE_PATH], shell=True)
        return "Modo de trabalho ativado. VS Code e navegadores prontos, senhor."

    @staticmethod
    def open_leisure_mode() -> str:
        webbrowser.open("https://www.youtube.com")
        webbrowser.open("https://open.spotify.com")
        return "Modo de lazer iniciado. Relaxe e aproveite."

    @staticmethod
    def get_system_status() -> str:
        cpu = psutil.cpu_percent()
        battery = psutil.sensors_battery()
        percent = battery.percent if battery else "N/A"
        return f"O uso da CPU está em {cpu} porcento. A bateria está em {percent} porcento."

    @staticmethod
    def stop_all() -> str:
        pyautogui.hotkey('win', 'd')
        return "Minimizando tudo e aguardando novos comandos."