from distutils.log import debug
from flask import Flask , request,render_template,flash,redirect, url_for
from main import run_classifier
import os
import random
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(),"images")
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
#token = ""

songs = {

    'Disgust':"7zpZFvJpcZC2uYgdSZNfuA",
    'Fear':"405PXg1fJunIlSo75L78Kb",
    'Happy':"4PY9rbCQSo2JvGdgREogIe",
    'Neutral':"3C7FXzgUwDq7hY68lW5B2d", 
    'Sad':"4YOfhHpjPB0tq29NPpDY3F", 
    'Surprise':"7vatYrf39uVaZ8G2cVtEik"
}

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
       
        files = request.files
        image = files.get('file')
        
        if image.filename == '':
            flash("no image selected")
            return redirect(request.url)
        else:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(UPLOAD_FOLDER,filename)
            mood = run_classifier(image_path)
            print(mood)
            # the first argument in url_for takes the function name, NOT the actual endpoint
            return redirect(url_for("music", mood=songs[mood]))

    return render_template('index.html')


@app.route('/music/<mood>',methods=["GET","POST"])
def music(mood):
    
    context = {
        "mood":mood
    }
    return render_template('musicplayer.html',context=context)


if __name__=='__main__':
    app.run(debug=True)
