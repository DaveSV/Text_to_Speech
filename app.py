from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

def text_to_audio(text, output_file, language='es-us'):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        archivo_audio = "static/audio.mp3"  # Ruta donde se guardará el archivo de audio
        text_to_audio(texto, archivo_audio)
        return render_template('index.html', audio_file=archivo_audio)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
