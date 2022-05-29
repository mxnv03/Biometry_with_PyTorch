from Yolov5_DeepSort_Pytorch.bd_connection import connection_check


def test_connection_ok():
    assert connection_check() == True