from flask import Flask,render_template,request,send_from_directory
from remove_background import remove_background
import os

app = Flask(__name__)


ALLOWED_EXTENSIONS = {"png","jpeg"}

app.config["UPLOAD_FOLDER"] = "media"


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/upload")
def handle_image():

    image = request.files["image"]

    path = os.path.join(app.config["UPLOAD_FOLDER"],image.filename )
    output = os.path.join(app.config["UPLOAD_FOLDER"], "output.png")
    print(path)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    image.save(path)
    remove_background(path,output )
    os.remove(path)
    return send_from_directory(app.config["UPLOAD_FOLDER"],path="output.png")

app.run(debug=True)
