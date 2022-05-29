from Yolov5_DeepSort_Pytorch.video_title import get_video_title

def test_get_video_title():
    assert get_video_title(url='https://www.youtube.com/watch?v=KdZ4HF1SrFs') == 'Алгоритмы'
