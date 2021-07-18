# clasificador_lunares
<h1>Clasificador de lunares </h1>
<h2>Creación de una aplicación web que use un modelo entrenado con Deep Learning a partir del curso de Fastai<h2>
Practical Deep Learning for Coders  https://course.fast.ai/
<h3>Datos usados:</h3>
Kaggle Dataset: Skin Cancer: Malignant vs. Benign
Processed Skin Cancer pictures of the ISIC Archive
This dataset contains a balanced dataset of images of benign skin moles and malignant skin moles
https://www.kaggle.com/fanconic/skin-cancer-malignant-vs-benign


<h3>Motivación</h3>
En la lección 2 se ofrecen diferentes opciones para poder usar el modelo entrenando en el curso a través de la web.  Recomiendan hacerlo a través de Voila y Binder por ser una forma sencilla de publicar Jupyter notebooks.

Yo, en cambio, he querido ir más allá y crear una aplicación web en la cual se realice la predicción del modelo entrenado en el lado del servidor. Esta aproximación tiene la ventaja de poder implementarse de forma fácil también en apps de dispositivos móviles.

De esta forma, se podrá subir la imagen desde la web al servidor, devolviendo el resultado obtenido.


