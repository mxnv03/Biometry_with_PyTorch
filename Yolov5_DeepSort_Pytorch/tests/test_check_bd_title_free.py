from Yolov5_DeepSort_Pytorch.check_bd_title_free import is_title_free
from Yolov5_DeepSort_Pytorch.bd_connection import connection, cursor


def test_is_title_free():
    cursor.execute(f'CREATE TABLE tables.test_table (time REAL,'
                   f' frame INTEGER,'
                   f' face_id INTEGER,'
                   f' box_x INTEGER,'
                   f' box_y INTEGER,'
                   f' box_width INTEGER,'
                   f' box_height INTEGER);')
    connection.commit()
    assert not is_title_free(title='test_table')


cursor.execute('DROP TABLE tables.test_table;')
