import pymysql
import PySimpleGUI as sg
from database import *



class Tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome Completo', size=(16,0)),sg.Input(key='nome')],
            [sg.Text('Apartamento', size=(16,0)),sg.Input(key='apt')],
            [sg.Text('Qnt de moradores', size=(16,0)),sg.Input(key='qnt')],
            [sg.Text('Possui veículo?', size=(16,0))],
            [sg.Checkbox('Sim',key='sim'),sg.Checkbox('Não',key='nao')],
            [sg.Button('Enviar')]            
        ]
        #janela
        janela = sg.Window('Dados Morador').layout(layout)
        #extração
        self.Button, self.values = janela.Read()

    def iniciar(self):
        nome =self.values['nome']
        apt = self.values['apt']
        qnt = self.values['qnt']
        vsim = self.values['sim']
        vnao = self.values['nao']
        print(f'nome: {nome}')
        print(f'apt: {apt}')
        print(f'qnt: {qnt}')
        print(f'veiculo sim: {vsim}')
        print(f'veiculo nao: {vnao}')

    





