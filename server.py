from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    print('button clicked')
    text = request.args.get("textToAnalyze")
    print(text)
    json_rep = emotion_detector(text)
    print(json_rep)

    # if not text or json_rep.get('dominant_emotion') is None:
    #     return "Invalid text! Please try again!"

    # output = f"For the given statement, the system response is 'anger': {str(json_rep['anger'])},"
    # output += f" 'disgust': {str(json_rep['disgust'])}, 'fear': {str(json_rep['fear'])}, "
    # output += f"'joy': {str(json_rep['joy'])} and 'sadness': {str(json_rep['sadness'])}. The dominant emotion is {str(json_rep['dominant_emotion'])}."

    # print(output)

    return json_rep
    
     
       