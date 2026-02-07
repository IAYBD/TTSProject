import re

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