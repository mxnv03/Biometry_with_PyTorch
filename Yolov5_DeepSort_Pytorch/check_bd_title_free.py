from Yolov5_DeepSort_Pytorch.bd_connection import connection_check, connection, cursor


def is_title_free(title):
    if connection_check():
        cursor.execute("""SELECT relname FROM pg_class WHERE relkind='r'
                          AND relname !~ '^(pg_|sql_)';""")  # "rel" is short for relation.

        tables = [i[0] for i in cursor.fetchall()]  # A list() of tables.
        if title not in tables:
            return True
        else:
            return False