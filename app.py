from flask import Flask, render_template
import random
import platform

app = Flask(__name__)

# list of cat images
images = [
    "http://i.giphy.com/Nm8ZPAGOwZUQM.gif",
    "https://i.giphy.com/JIX9t2j0ZTN9S.gif",
    "https://i.giphy.com/8u9PS5l5znIbe.gif",
    "https://i.giphy.com/82CItLnbSh8hzsXK3H.gif",
    "https://i.giphy.com/jFxlUfJkHdz7W.gif",
    "https://i.giphy.com/IUjNSNM9VEUH6.gif",
    "https://i.giphy.com/O5pd2oPjjcGFW.gif",
    "https://i.giphy.com/l0IydrYaxclPhGG76.gif",
    "https://i.giphy.com/WQ9ghbypX4mly.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    hostname = platform.node()
    return render_template('index.html', url=url, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
