import pymysql
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Button('Enviar')]            
        ]
        #janela
        janela = sg.Window('Dados Morador').layout(layout)
        #extração
        self.Button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)
    

'''
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
'''



