# American_sign_language_recognition
The process followed during the building of the recognition system can be summarized as follows:

## Data collection. 
The images were captured with the help of a mobile camera for various signs.
    
## Data importing and preprocessing. 
The images were imported and then using Google's Mediapipe Framework, the hand landmarks were extracted and stored into a pickle file along with the labels.

## Model building and training. 
An artificial neural network was used for the classification of various signs. Hyperparameter tuning was done in order to get the optimized number of units per layer for maximum accuracy. Based on the results of hyperparameter tuning, a neural network with an input layer containing 384 units, a hidden layer containing 320 units, and an output layer containing 37 units was chosen. The model was then trained for 40 epochs.

## Real-time application. 
The model was deployed to the web using Flask for real-time application.
