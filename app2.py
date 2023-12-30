from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import time

app = Flask(__name__, static_url_path='/static')

model = load_model('model.h5')  # Change the filename based on your saved model

def process_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalization
    return img_array

def process_result(result):
    class_labels = ['paper', 'rock', 'scissors']
    predicted_class = class_labels[np.argmax(result)]
    confidence = max(result[0])
    return predicted_class, confidence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Simpan file dengan nama yang tetap
        filename = os.path.join('static', 'uploads', 'uploaded_image.png')
        file.save(filename)

        start_time = time.time()

        # Lakukan prediksi dengan model
        img_array = process_image(filename)
        result = model.predict(img_array)
        prediction, confidence = process_result(result)

        end_time = time.time()
        processing_time = f'{end_time - start_time:.2f} seconds'

        # Definisikan path gambar secara eksplisit
        image_path = os.path.join('uploads', 'uploaded_image.png')

        return render_template('result1.html', image_path=image_path, prediction=prediction, confidence=confidence, processing_time=processing_time)

if __name__ == '__main__':
    app.run(debug=True)
