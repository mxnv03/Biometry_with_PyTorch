import psycopg2

connection = psycopg2.connect(user="postgres", password="123456789",
                                  host="127.0.0.1", port="5432", database="biometry_output")
cursor = connection.cursor()


def connection_check():
    if connection:
        return True
    else:
        return False



