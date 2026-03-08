def detect_intent(text):

    text = text.lower()

    if "book" in text:
        return "book_appointment"

    elif "cancel" in text:
        return "cancel_appointment"

    elif "reschedule" in text or "move" in text:
        return "reschedule_appointment"

    elif "availability" in text or "available" in text:
        return "check_availability"

    else:
        return "unknown_intent"