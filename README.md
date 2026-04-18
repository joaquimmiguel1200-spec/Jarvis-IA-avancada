# JARVIS Virtual Assistant (Python 3.12+)

Este é um assistente virtual modular inspirado no JARVIS, utilizando tecnologias modernas de Python.

## Funcionalidades
- **Reconhecimento de Voz**: Escuta contínua via `SpeechRecognition`.
- **Síntese de Voz**: Feedback por voz masculina via `pyttsx3`.
- **Modos de Operação**:
  - `Modo Trabalho`: Abre GitHub, StackOverflow e VS Code.
  - `Modo Lazer`: Abre Spotify e YouTube.
  - `Status do Sistema`: Relata CPU e bateria via `psutil`.
- **Hardware Trigger**: Detector de palmas via `PyAudio` e `NumPy` para ativar/desativar o estado de escuta.
- **Estrutura**: Totalmente tipado (type hints) e modularizado.

## Requisitos de Sistema
- Python 3.12 ou superior.
- PortAudio (necessário para o `pyaudio`).
  - *Linux*: `sudo apt install portaudio19-dev`
  - *macOS*: `brew install portaudio`

## Como Usar
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure o arquivo `.env` se desejar usar APIs externas.
3. Execute o sistema: `python main.py`
4. Diga "Jarvis" seguido de um comando, ou bata uma palma para alternar o modo de espera.

## Arquitetura
- `main.py`: Ponto de entrada e orquestração.
- `voice_engine.py`: Encapsulamento de Text-to-Speech.
- `sensors.py`: Processamento de sinal de áudio em tempo real.
- `actions.py`: Automação de SO e comandos.
- `config.py`: Gestão de variáveis de ambiente com Pydantic V2.