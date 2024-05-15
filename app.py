import streamlit as st
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
from utils import predict_label
from PIL import Image, ImageOps
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('best_model.h5')
    return model

def import_and_predict(image_data, model):
    size = (150,150)  
    image = ImageOps.fit(image_data, size)
    image = np.asarray(image, dtype='float32')
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
    img = img / 255
    prediction = model.predict(img)
    return prediction

st.write("Emerging Technologies 2 by Pagatpat, Paul Gabriel and Dalangan, Katherine May")
st.write("""
         # Intel Image Classification
         \nA demonstration on a Predictive Convolutional Neural Network with a 66% accuracy that uses
         images of natural scenes from a Datahack challenge by Intel.
         """
         )

file = st.file_uploader("Upload images that either classify as an image of a mountain, street, glacier, building, sea, or a forest (PNG or JPG only)", type=["jpg", "png"])
st.set_option('deprecation.showfileUploaderEncoding', False)
if file is None:
    st.text("Please upload an image file")
else:
    size = (150,150)  
    image = Image.open(file)
    image = ImageOps.fit(image, size)
    st.image(image, width=image.size[0]*2)
    model = load_model()
    prediction = import_and_predict(image, model)
