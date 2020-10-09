import pymysql
import PySimpleGUI as sg
from database import *


class Tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome Completo', size=(16,0)),sg.Input(key='linha1')],
            [sg.Text('Apartamento', size=(16,0)),sg.Input(key='linha2')],
            [sg.Text('Qnt de moradores', size=(16,0)),sg.Input(key='linha3')],
            [sg.Text('Possui veículo?', size=(16,0))],
            [sg.Checkbox('Sim',key='sim'),sg.Checkbox('Não',key='nao')],
            [sg.Button('Enviar')]            
        ]
        #janela
        janela = sg.Window('Dados Morador').layout(layout)
        #extração
        self.Button, self.values = janela.Read()

    def iniciar(self):
        n = self.values['linha1']
        a = self.values['linha2']
        q = self.values['linha3']
        vs = self.values['sim']
        vn = self.values['nao']
        print(f'nome: {n}')
        print(f'apt: {a}')
        print(f'qnt: {q}')
        print(f'veiculo sim: {vs}')
        print(f'veiculo nao: {vn}')
        cursor = conexao.cursor()
        incluir = 'INSERT TO morador(nome, apt, qnt, vsim,vnao)VALUES(%s, %s, %s, %s, %s)'
        valor = [
            (str(n),str(a),str(q),str(vs),str(vn))
        ]
        cursor.execute(incluir,valor)
        
        conexao.commit()
        print(cursor.rowcount,'Inserido com Sucesso')

    





