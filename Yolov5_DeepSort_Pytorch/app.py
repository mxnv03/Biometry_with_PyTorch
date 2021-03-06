import os
import shutil
import threading
import time
from bd_connection import connection_check
from video_title import get_yt_video_title, get_video_title
import cv2
from flask import Flask, render_template, Response, request, redirect, url_for
from werkzeug.utils import secure_filename
import config
from Yolov5_DeepSort_Pytorch import RunTrack
from track import create_new_table
from Yolov5_DeepSort_Pytorch.check_bd_title_free import is_title_free

app = Flask(__name__)


def gen_frames():  # generate frame by frame from camera
    while True:
        path = os.path.join('Photos', str(config.num) + '.jpg')
        img = cv2.imread(path, cv2.IMREAD_COLOR) if os.path.exists(path) else None

        if img is not None:
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
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
    if not config.AI:
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
    file_title = open('title.txt', 'w')
    if request.method == 'POST':
        if request.form.get("YoutubeGet"):
            youtube = request.form.get("youtube")
            title = get_yt_video_title(youtube)
            file_title.write(title)
            if connection_check():
                if is_title_free(title):
                    create_new_table(title)
            return redirect(url_for(f'watch', video={youtube}, url=True), 301)
        elif request.form.get("FileGet"):
            file = request.files['file']
            filename_for_bd = get_video_title(file.filename)
            if connection_check():
                if is_title_free(filename_for_bd):
                    create_new_table(filename_for_bd)
            filename = secure_filename(file.filename)
            file_title.write(filename_for_bd)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for(f'watch', video={filename}, url=False), 301)
    return render_template('index.html')


def clear_folder():
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
    clear_folder()
    app.run(debug=True, port=8000)
