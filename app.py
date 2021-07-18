from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
import fastbook
from fastbook import *
from fastai.vision import *
import os
from werkzeug.utils import secure_filename
import imghdr

fastbook.setup_book()


# Se importa nuestro modelo preentrenado /export.pkl)

path=Path()
path.ls(file_exts='.pkl')
learn_inf=load_learner(path/'export.pkl')


# valores para uso de Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static'


# función que valida la extensión del archivo
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

# función que valida el tamaño del archivo
@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


# función  de genera la página pricipal
@app.route('/')
def index():
    for f in os.listdir(app.config['UPLOAD_PATH']):
    	os.remove(os.path.join(app.config['UPLOAD_PATH'], f))
    return render_template('inicio.html')

# función  generada tras pulsar boton de Clasificación
@app.route('/', methods=['POST'])
def upload_files():
    files = os.listdir(app.config['UPLOAD_PATH'])
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
            
        filenamefull =os.path.join(app.config['UPLOAD_PATH'], filename)  
        uploaded_file.save(filenamefull)  #guardar la imagen, se mostrará en el resultado
       
        img = PILImage.create(os.path.join(filenamefull))
        pred,pred_inx,prob=learn_inf.predict(img)   # uso del modelo para hacer la predicción
        prediccion=f'Prediccion: {pred}; probabilidad: {prob[pred_inx]:.04f}'
                
    return render_template('resultado.html',prediccion=prediccion, files=files,imagen=filenamefull)                

