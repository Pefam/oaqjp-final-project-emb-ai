"""
Flask web application for emotion detection
This module defines a Flask app that analyzes emotions in text input.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    Analyze emotion in provided text
    Returns formatted analysis results or error message
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "<strong>Invalid text! Please try again!</strong>"
    # Format all emotions including fear with 4 decimal places
    message = (
        "For the given statement, the system response is 'anger': "
        f"{result['anger']:.4f}, 'disgust': {result['disgust']:.4f}, "
        f"'fear': {result['fear']:.4f}, 'joy': {result['joy']:.4f} "
        f"and 'sadness': {result['sadness']:.4f}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    )
    return message

@app.route("/")
def index():
    """Render the main index page with the input form"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
