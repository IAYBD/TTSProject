# .\venv\Scripts\Activate
from modules import preprocess_text, split_text, text_to_speech
import os

audio_folder = "results"

with open("book/elquijotedeavellaneda.txt", "rt" , encoding="utf-8") as f:
    book = f.read()

cleaned_book = preprocess_text(book)

separated_book = split_text(cleaned_book)

final_mp3 = text_to_speech(separated_book, language="es", slow=False)

if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Guardar el MP3 final
with open(os.path.join(audio_folder, "ElQuijotePrimerCapitulo.mp3"), "wb") as f:
    f.write(final_mp3.getvalue())

print("¡MP3 generado con éxito!")