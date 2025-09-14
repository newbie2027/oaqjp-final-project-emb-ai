from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('emotion detector')

@app.route('/emotionDetector')

def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    label = response[0]
    score = response[1]

    return f'For the given statement, the system response is {label}:{score}'
