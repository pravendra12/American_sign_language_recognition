# American Sign Language Recognition
<p align="center">
    <img width="600" src="https://github.com/pravendra12/American_sign_language_recognition/assets/105543056/738f3f2d-020e-40f1-bffb-ff7d7a836dbb" alt="ASL">
</p>
<br>
To learn more about American Sign Language - https://en.wikipedia.org/wiki/American_Sign_Language
<br>
<br>
The process followed during the building of the recognition system can be summarized as follows:

## Data collection. 
The images were captured with the help of a mobile camera for various signs.
    
## Data importing and preprocessing. 
The images were imported and then using Google's Mediapipe Framework, the hand landmarks were extracted and stored into a pickle file along with the labels.
<br>
<p align="center">
    <img width="600" src="https://github.com/pravendra12/American_sign_language_recognition/assets/105543056/48fadd66-7b29-4ad6-a35d-2202eddd979b" alt="Handlandmarks">
</p>

## Model building and training. 
An artificial neural network was used for the classification of various signs. Hyperparameter tuning was done in order to get the optimized number of units per layer for maximum accuracy. Based on the results of hyperparameter tuning, a neural network with an input layer containing 384 units, a hidden layer containing 320 units, and an output layer containing 37 units was chosen. The model was then trained for 40 epochs.

<p align="center">
    <img width="600" src="https://github.com/pravendra12/American_sign_language_recognition/assets/105543056/1ec4d5e0-a749-4ce1-8671-77a2fc54a467" alt="Neural Network schematic">
</p>


## Real-time application. 
The model was deployed to the web using Flask for real-time application. Below is the snapshot of the webpage

<p align="center">
    <img width="600" src="https://github.com/pravendra12/American_sign_language_recognition/assets/105543056/75e02f89-f7e9-45ac-ba9a-f840367392ef" alt="real time detection">
</p>
<br>
To use the webpage, download webapp folder and run the app.py file.
