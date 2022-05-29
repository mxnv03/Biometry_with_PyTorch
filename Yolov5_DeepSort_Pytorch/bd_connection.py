import psycopg2


def connection_check():
    connection = psycopg2.connect(user="postgres", password="123456789",
                                  host="127.0.0.1", port="5432", database="biometry_output")
    if connection:
        return True
    else:
        return False



