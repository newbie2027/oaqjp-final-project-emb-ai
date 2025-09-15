"""This script processes emotion analysis results and prints formatted output."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('emotion detector')

@app.route('/emotionDetector')

def sent_analyzer():
    """Run emotion detection."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_label = list(response.keys())[0]
    anger_score = response['anger']
    disgust_label = list(response.keys())[1]
    disgust_score = response['disgust']
    fear_label = list(response.keys())[2]
    fear_score = response['fear']
    joy_label = list(response.keys())[3]
    joy_score = response['joy']
    sadness_label = list(response.keys())[4]
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    return (
            f"For the given statement, the system response is '{anger_label}': {anger_score},"
            f"'{disgust_label}': {disgust_score},"
            f"'{fear_label}': {fear_score},"
            f"'{joy_label}': {joy_score},"
            f"'{sadness_label}': {sadness_score}. "
            f"The dominant emontion is {dominant_emotion}."
        )

@app.route("/")
def render_index_page():
    """redirect to default index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    