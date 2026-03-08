from services.speech_to_text.stt import speech_to_text
from services.language_detection.detect import detect_language
from services.agent.agent import detect_intent
from services.scheduler.appointment_engine import book_appointment, cancel_appointment, check_availability

if __name__ == "__main__":
    # audio file
    audio_file = "services/speech_to_text/sample.m4a"

    # Step 1: Speech to text
    text = speech_to_text(audio_file)
    print("Recognized text:", text)

    # Step 2: Detect language
    language = detect_language(text)
    print("Language:", language)

    # Step 3: Detect intent
    intent = detect_intent(text)
    print("Intent:", intent)

    # Step 4: Perform action
    if intent == "book_appointment":
        result = book_appointment("Akash", "Cardiologist", "10 AM")

    elif intent == "cancel_appointment":
        result = cancel_appointment("Akash")

    elif intent == "check_availability":
        result = check_availability()

    else:
        result = "Sorry, I could not understand."

    print("AI Response:", result)