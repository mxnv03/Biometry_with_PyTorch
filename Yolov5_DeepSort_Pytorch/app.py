import os, shutil
import time

from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import config
from Yolov5_DeepSort_Pytorch import RunTrack
import threading
from werkzeug.utils import secure_filename
import glob

app = Flask(__name__)


def gen_frames():  # generate frame by frame from camera
    while True:
        path = os.path.join('Photos', str(config.num) + '.jpg')
        img = cv2.imread(path, cv2.IMREAD_COLOR) if os.path.exists(path) else None

        if img is not None:
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            # print(type(frame))
            time.sleep(0.04)
            os.remove(os.path.join('Photos', str(config.num) + '.jpg'))
            config.num += 1
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        else:
            time.sleep(0.04)


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/watch')
def watch():
    if config.AI == False:
        config.AI = True
        print('Start of detection')
        source = request.args.get('video').replace("{'", "").replace("'}", "")
        url = request.args.get('url').replace("{'", "").replace("'}", "")
        x = threading.Thread(target=RunTrack.run, args=(source, url, os.getcwd(),), daemon=True)
        x.start()
    else:
        print('End of detection')
        config.num = 0
    return render_template('watch.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form.get("YoutubeGet"):
            youtube = request.form.get("youtube")
            return redirect(url_for(f'watch', video={youtube}, url=True), 301)
        elif request.form.get("FileGet"):
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for(f'watch', video={filename}, url=False), 301)
    return render_template('index.html')


def clearFolder():
    folder = os.getcwd() + '/Photos'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == '__main__':
    UPLOAD_FOLDER = os.getcwd() + '/Videos'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    clearFolder()

    app.run(debug=True, port=8000)
