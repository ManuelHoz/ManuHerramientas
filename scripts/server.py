from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# Carpeta que queremos compartir (la carpeta del script en este caso)
SHARED_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    files = os.listdir(SHARED_FOLDER)
    return render_template_string(
        '''
        <h1>Archivos disponibles:</h1>
        <ul>
        {% for file in files %}
            <li><a href="/files/{{ file }}">{{ file }}</a></li>
        {% endfor %}
        </ul>
        ''',
        files=files
    )

@app.route('/files/<path:path>')
def serve_file(path):
    return send_from_directory(SHARED_FOLDER, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
