from gtts import gTTS
import io

def text_to_speech(list_of_texts, language="es", slow=False):

    mp3 = io.BytesIO()

    for fragment in list_of_texts:
        tts = gTTS(text=fragment, lang=language, slow=slow)
        memoria = io.BytesIO()
        tts.write_to_fp(memoria)
        memoria.seek(0)

        # Concatenar los bytes directamente
        mp3.write(memoria.read())

    return mp3