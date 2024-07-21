from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os
from Functions import process_resume, create_visualizations, upload_file, show_details

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def route_process_resume():
    if request.method == 'POST':
        # Verifica si el post request tiene el archivo parte
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # Si el usuario no selecciona un archivo, el navegador
        # submit un archivo vacio sin un nombre de archivo.
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            process_resume(file_path)  # Ahora pasas la ruta del archivo a process_resume
            return redirect('/results')
    return render_template('home.html')