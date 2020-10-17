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
            [sg.Button('Incluir',key='incluir'),sg.Button('Excluir',key='excluir'),sg.Button('Exibir Lista',key='exibir'),sg.Button('Limpar Tela',key='limpar')],
            [sg.Output(size=(60,10))]            
        ]
        #janela
        self.janela = sg.Window('Dados Morador').layout(layout)
        
    def iniciar(self):
        while True:
            #extração
            self.Button, self.values = self.janela.Read()
      
            if self.Button == 'incluir':
                n = self.values['linha1']
                a = self.values['linha2']
                q = self.values['linha3']
                vs = self.values['sim']
                vn = self.values['nao']
                
                cursor = conexao.cursor()
                incluir = 'INSERT INTO morador(nome, apt, qnt, vsim,vnao)VALUES(%s, %s, %s, %s, %s)'
                valor =(str(n),str(a),str(q),bool(vs),bool(vn))

                cursor.execute(incluir,valor)
                conexao.commit()
                print('CARREGAMENTO CONCLUÍDO')
                print(f'nome: {n}')
                print(f'apt: {a}')
                print(f'qnt: {q}')
                print(f'veiculo sim: {vs}')
                print(f'veiculo nao: {vn}')
            
            elif self.Button == 'limpar':
                self.result = 0
                self.values['linha1'].update(value=self.result)
                self.values['linha2'].update(value=self.result)
                self.values['linha3'].update(value=self.result)
                self.values['sim'].update(value=self.result)
                self.values['nao'].update(value=self.result)

                 
                

               

              
                
                

            

    





