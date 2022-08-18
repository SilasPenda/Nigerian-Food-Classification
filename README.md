# Nigerian-Foood-Classification
This is an image classification project to classify Nigerian food to be either 'Yam', 'Egusi', 'Oha Soup', 'Afang Soup', 'Bread', 'Rice and Stew', 'Moi Moi', or 'Akara'. I created a streamlit web app to test the model. After the prediction, there is a link to a webpage where you can see recipes to make the predicted food.

# Guide
* Import necessary libraries
* Read image directory and save images path in a list
* Make a copy of the image paths list, shuffle and split into train, validation and test data 
* Generate new images using ImageDataGenerator
* Load pretrained model and freeze the layers
* Create layers
* Train model
* Test model and save as '.h5' model
* Create web app using streamlit and deploy
