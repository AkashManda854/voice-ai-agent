from fastapi import FastAPI
import time

from services.speech_to_text.stt import speech_to_text
from services.language_detection.detect import detect_language
from services.agent.agent import detect_intent
from services.scheduler.appointment_engine import (
    book_appointment,
    cancel_appointment,
    check_availability
)
from services.tts import speak
app=FastAPI()


@app.get("/")
def health():
    return {"status": "Voice AI Agent Running"}


@app.get("/run-agent")
def run_agent():

    start = time.time()

    audio_file = "services/speech_to_text/sample.m4a"

    # Speech to Text
    text = speech_to_text(audio_file)

    # Language detection
    language = detect_language(text)

    # Intent detection
    intent = detect_intent(text)

    # Scheduler
    if intent == "book_appointment":
        result = book_appointment("Akash", "Cardiologist", "10 AM")

    elif intent == "cancel_appointment":
        result = cancel_appointment("Akash")

    elif intent == "check_availability":
        result = check_availability()

    else:
        result = "Sorry, I could not understand."

    # Text to speech
    speak(str(result))

    end = time.time()
    latency = (end - start) * 1000

    return {
        "recognized_text": text,
        "language": language,
        "intent": intent,
        "response": result,
        "latency_ms": latency
    }