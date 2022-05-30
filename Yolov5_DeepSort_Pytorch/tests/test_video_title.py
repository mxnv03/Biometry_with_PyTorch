from Yolov5_DeepSort_Pytorch.video_title import get_yt_video_title, get_video_title


def test_yt_get_video_title():
    assert get_yt_video_title(url='https://www.youtube.com/watch?v=KdZ4HF1SrFs') \
           == 'Алгоритмы_на_Python_3_Лекция_1'  # Алгоритмы на Python 3. Лекция №1
    assert get_yt_video_title(url='https://www.youtube.com/watch?v=x_-L7MM8rV8') \
           == 'ТЕСТИРУЕМ_WEBCLIENT_С_ПОМОЩЬЮ_PYTEST_И_RESPONSES'  # ТЕСТИРУЕМ WEB-CLIENT С ПОМОЩЬЮ PYTEST И RESPONSES
    assert get_yt_video_title(url='https://www.youtube.com/watch?v=BoazgBZ4D7k') \
           == 'Собеседование_Python_Разбор_вопросов'  # Собеседование Python. Разбор вопросов


def test_get_video_title():
    assert get_video_title('Мальбэк — Равнодушие ft. Сюзанна.mp4') == 'Мальбэк_Равнодушие_ft_Сюзанна'
