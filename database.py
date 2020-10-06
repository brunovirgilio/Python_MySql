import pymysql


conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database ='db2'    
)
'''
cursor = conexao.cursor()
cursor.execute('CREATE TABLE morador(Id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), apt INT(3), qnt INT(2), vsim BOOLEAN, vnao BOOLEAN)')
'''
cursor = conexao.cursor()
cursor.execute('SHOW TABLES')

for x in cursor:
    print(x)