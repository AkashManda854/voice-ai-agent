from faster_whisper import WhisperModel

# load model once
model = WhisperModel("base", compute_type="int8")

def speech_to_text(audio_file):

    segments, info = model.transcribe(audio_file)

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()