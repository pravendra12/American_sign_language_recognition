from flask import Flask, render_template, Response
import cv2
from keras.models import load_model
import mediapipe as mp

import numpy as np

app=Flask(__name__)

global model 
model = load_model("model1.h5", compile=False)

global predicted_character
predicted_character = ''

global output
output = []

labels_dict = {}
for i in range(37):
    if(i<10):
        labels_dict[i] = str(i)
    elif(i == 36):
        labels_dict[i] = " "
    else:
        labels_dict[i] = str(chr(55+i))

def capture_by_frames(): 
    global camera
    camera = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    
    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = camera.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10
            
            data_aux = np.asarray(data_aux)

            try:
                pred = model.predict([data_aux.reshape(1,-1)])
            except:
                pass

            prediction = np.argmax(pred)
            predicted_character = labels_dict[prediction]
        
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
            
                    
            ret,buffer=  cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            

            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
def save_character():
    output.append(predicted_character)

    
            
    

        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start',methods=['POST'])
def start():
    return render_template('index.html')

@app.route('/stop',methods=['POST'])
def stop():
    if camera.isOpened():
        camera.release()
    return render_template('stop.html')

@app.route('/video_capture')
def video_capture():
    return Response(capture_by_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True,use_reloader=False, port=8000)

    
