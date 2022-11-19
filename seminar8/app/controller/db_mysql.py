import mysql.connector
from app.model import tel

cnx = None

def get_data(str_pattern):
    cur = cnx.cursor()
    cur.execute(tel.select_tel_query(str_pattern))
    print(cur)
    return [tuple(elem) for elem in cur]

# def push_data(lst_in):
#     conn.executemany(tel.get_add_tel_query(),lst_in)
#     conn.commit()

def create_table():
    global cnx
    cnx.cursor().execute(tel.get_create_table_query().replace('AUTOINCREMENT','AUTO_INCREMENT'))


# def remove_data(data):
#     conn.execute(tel.get_remove_query(data))
#     conn.commit()

def init():
    global cnx    

    try:
        cnx = mysql.connector.connect(user='python', db='python',passwd='Python3', host='localhost')     

    except:
        print('Error connecting to MySQL database')
    
    create_table()