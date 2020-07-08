import pytube
from pytube import YouTube
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        url = request.form["url"]
        try:
            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            return render_template("index.html", eval=0)
        except Exception as e:
            return render_template("index.html", error_msg=e , eval=1)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)