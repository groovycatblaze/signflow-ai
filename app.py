
from flask import Flask, render_template, request
from utils.predict import predict_from_video
import pyttsx3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output_text = ""
    if request.method == "POST":
        video = request.files.get("video")
        if video:
            video_path = "static/input_video.mp4"
            video.save(video_path)
            output_text = predict_from_video(video_path)

            engine = pyttsx3.init()
            engine.say(output_text)
            engine.runAndWait()

    return render_template("index.html", prediction=output_text)

if __name__ == "__main__":
    app.run(debug=True)
