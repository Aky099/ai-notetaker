import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def transcribe_audio(audio_bytes: bytes, filename: str) -> str:
    """Transcribe an audio file with Groq's Whisper model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")

    client = Groq(api_key=api_key)
    transcription = client.audio.transcriptions.create(
        file=(filename, audio_bytes),
        model="whisper-large-v3-turbo",
    )
    return transcription.text