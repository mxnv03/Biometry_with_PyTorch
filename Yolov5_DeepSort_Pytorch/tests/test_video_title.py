from Yolov5_DeepSort_Pytorch.video_title import get_yt_video_title, get_video_title


def test_yt_get_video_title():
    assert get_yt_video_title(url='https://www.youtube.com/watch?v=KdZ4HF1SrFs') == 'Алгоритмы_на_Python_3_Лекция_№1'


def test_get_video_title():
    assert get_video_title('Мальбэк — Равнодушие ft. Сюзанна.mp4') == 'Мальбэк_Равнодушие_ft_Сюзанна'
