from flask import Flask,render_template,request,send_from_directory
import os
from rembg import remove


app = Flask(__name__)


ALLOWED_EXTENSIONS = {"png","jpeg"}

app.config["UPLOAD_FOLDER"] = "media"


def remove_background(img_path, output_path):
    with open(img_path, "rb") as img:
        with open(output_path, "wb") as output:
            file = img.read()
            output.write(remove(file))


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)
