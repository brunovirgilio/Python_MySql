import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db1'
)

cursor = conexao.cursor()
cursor.execute('SHOW TABLES')

for x in cursor:
    print(x)