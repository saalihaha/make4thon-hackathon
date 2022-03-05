from distutils.log import debug
from flask import Flask , request,render_template,flash,redirect
from main import run_classifier
import os
import random
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(),"images")
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER




@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        print("hello")
        files = request.files
        image = files.get('file')
        
        if image.filename == '':
            flash("no image selected")
            return redirect(request.url)
        else:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(UPLOAD_FOLDER,filename)
            print(run_classifier(image_path))

    return render_template('index.html')


@app.route('/music',methods=["GET","POST"])
def music():
    pagetitle = "Music"
    return render_template('musicplayer.html')


if __name__=='__main__':
    app.run(debug=True)

'''
if __name__=='__main__':
    app.run('0.0.0.0',debug=True,ssl_context="adhoc")
'''

