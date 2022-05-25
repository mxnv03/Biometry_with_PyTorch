import subprocess
import os

videos = ['0',
          'https://www.youtube.com/watch?v=cJdjX9sksaI&ab_channel=panov90210',
          'https://www.youtube.com/watch?v=SsvM80bIA1k&ab_channel=MORGENSHTERN',
          'https://www.youtube.com/watch?v=wDsU4H2w48k&ab_channel=MORGENSHTERN',
          '1.jpg',
          '/Photos',
          'videoplayback.mp4'
          ]


def run(source=None, youtube=True, path=os.getcwd()):
    #print(source, youtube, path)
    # path = 'bestv2.pt'
    path1 = 'yolov5/weights/crowdhuman_yolov5m.pt'
    # path = 'C:/Users/CL/PycharmProjects/Biometry/yolov5/runs/train/exp/weights/best1.pt'
    source = videos[6] if source is None else source
    if youtube == 'False' or youtube == False:
        source = path + '/Videos/' + source
    print(source)
    subprocess.run(f'python track.py --yolo_model {path1} --img 416 --source {source} --classes 1 --show-vid --save-txt', shell=True)


if __name__ == '__main__':
    run(youtube=False)
