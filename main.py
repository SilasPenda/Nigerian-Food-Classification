import streamlit as st
from PIL import Image
from keras_preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model

model = load_model('NF.h5')
labels = {0: 'yam', 1: 'Akara', 2: 'Bread', 3: 'Moi Moi', 4: 'Egusi', 5: 'Oha Soup', 6: 'Afang Soup', 7: 'Rice and stew'}

def fetch_recipes(prediction):
    if prediction == 'yam':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=yam)")
    elif prediction == 'Akara':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=akara)")
    elif prediction == 'Bread':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=bread)")
    elif prediction == 'Moi Moi':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=moi%20moi)")
    elif prediction == 'Egusi':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=egusi)")
    elif prediction == 'Oha Soup':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=oha%20soup)")
    elif prediction == 'Afang Soup':
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=afang%20soup)")
    else:
        recipe = st.write(
            "View Recipe! [link](https://www.allnigerianrecipes.com/searchresults/?q=rice%20and%20stew)")
    return recipe


def processed_img(imagepath):
    img = load_img(imagepath, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img/255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():
    img_file = st.file_uploader('Choose an Image', type=['jpg', 'png'])
    if img_file is not None:
        img = Image.open(img_file).resize((250,250))
        st.image(img, use_column_width=False)
        save_image_path = '.upload_images/'+img_file.name
        with open(save_image_path, 'wb') as f:
            f.write(img_file.getbuffer())

        if img_file is not None:
            result = processed_img(save_image_path)
            print(result)
            st.success('Predicted: '+result)
            rec = fetch_recipes(result)
            st.warning(rec)

run()