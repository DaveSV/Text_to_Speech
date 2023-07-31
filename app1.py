from gtts import gTTS

def text_to_audio(text, output_file, language='es', tld='es'):
    # Crear el objeto gTTS con la configuración del acento deseado
    tts = gTTS(text=text, lang=language, tld=tld)

    # Guardar el archivo de audio
    tts.save(output_file)

if __name__ == "__main__":
    input_text_file = '¿Por qué aprender desarrollo y programación web? Aprender desarrollo y programación web puede ser una inversión valiosa para cualquier persona interesada en una carrera en tecnología o en cualquier persona que busque una forma de trabajar de manera más independiente y creativa. Además, el campo está en constante evolución, lo que significa que siempre hay oportunidades para aprender y mejorar tus habilidades.'
    output_audio_file = "audio.mp3"  # Reemplaza con la ruta donde quieras guardar el archivo de audio

    text_to_audio(input_text_file, output_audio_file)
