# Importa el objeto de tu aplicación desde tu archivo principal
# Importa la biblioteca pytest
import pytest
# Importa el objeto de tu aplicación desde tu archivo principal
from ..app import app

# ...

def test_index_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    # Ajusta la aserción para que coincida con el nuevo contenido HTML
    assert b'Text to Speech' in response.data

def test_audio_generation():
    client = app.test_client()
    response = client.post('/', data={'texto': 'Hola, esto es una prueba'})
    assert response.status_code == 200
    # Ajusta la aserción para que coincida con el nuevo contenido HTML
    assert b'<audio controls>' in response.data
    assert b'static/audio.mp3' in response.data