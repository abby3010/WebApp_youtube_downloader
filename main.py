import pytube
from pytube import YouTube
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    url = request.form.get("url")
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        return render_template("index.html", eval=0)
    except Exception as e:
        print(e)    
        return render_template("index.html", eval=1)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)