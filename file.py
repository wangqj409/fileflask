from flask import Flask,request
from pathlib import Path
import uuid
from datetime import datetime

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 200 * 1000 * 1000

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowedfile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def genewname():
    return datetime.now().strftime("%Y/%m/%d/") + str(uuid.uuid4()).replace('-', '')


@app.route("/upload", methods=["POST"])
def upload():
    file1 = request.files['file']
    if not allowedfile(file1.filename):
        return {'path':'', 'error':'not allowed file'}

    dst = "static/" + genewname()
    dp = Path(dst)
    if not dp.parent.exists():
        dp.parent.mkdir(parents=True)
        
    file1.save(dst)

    return {'path':dst, 'error':''}
