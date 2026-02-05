# .\venv\Scripts\Activate
from gtts import gTTS
import os
import io
import re

audio_folder = "audio"

def preprocess_text(text):
    # Pasar todo a una sola línea
    text = text.replace("\n", " ")

    # Eliminar espacios múltiples
    text = re.sub(r"\s+", " ", text)

    # Normalizar guiones largos
    text = text.replace("—", "-")

    # Eliminar caracteres no deseados
    text = re.sub(r"[^\w\sáéíóúÁÉÍÓÚñÑ.,;:¡!¿?\-]", "", text)

    return text.strip()

def split_text(text: str, max_chars: int = 900) -> list[str]:
    # Dividir el texto en frases
    phrases = re.split(r'(?<=[.!?])\s+', text)

    fragments = []
    current_fragment = ""

    for phrase in phrases:

        # Si añadir la frase supera el límite, cerramos fragmento
        if len(current_fragment) + len(phrase) > max_chars:
            fragments.append(current_fragment.strip())
            current_fragment = phrase
        else:
            current_fragment += " " + phrase

    # Añadir el último fragmento
    if current_fragment.strip():
        fragments.append(current_fragment.strip())

    return fragments

with open("book/elquijotedeavellaneda.txt", "rt" , encoding="utf-8") as f:
    book = f.read()

cleaned_book = preprocess_text(book)

separated_book = split_text(cleaned_book)

fragmentos = separated_book  # tu lista de fragmentos

mp3_final = io.BytesIO()

for fragment in fragmentos:
    tts = gTTS(text=fragment, lang="es", slow=False)
    memoria = io.BytesIO()
    tts.write_to_fp(memoria)
    memoria.seek(0)

    # Concatenar los bytes directamente
    mp3_final.write(memoria.read())

# Guardar el MP3 final
with open("ElQuijotePrimerCapitulo.mp3", "wb") as f:
    f.write(mp3_final.getvalue())

print("¡MP3 generado con éxito!")