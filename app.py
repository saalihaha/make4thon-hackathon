from flask import Flask , request,render_template
from main import run_classifier
import os
import random
app = Flask(__name__)


def specific_string(length):  
    sample_string = 'pqrstuvasdasdaswxy' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        files = request.files
        image = files.get('file')
        imagePath = os.path.abspath(f'images/{image}')
        with open(imagePath, 'wb') as f:
            f.write(image.content)
        print(run_classifier(imagePath))

    return render_template('index.html')


@app.route('/music',methods=["GET","POST"])
def music():
    pagetitle = "Music"
    return render_template('musicplayer.html')


if __name__=='__main__':
    app.run()

'''
if __name__=='__main__':
    app.run('0.0.0.0',debug=True,ssl_context="adhoc")
'''

