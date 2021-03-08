import pymysql
import PySimpleGUI as sg
from database import *



layout = [
    [sg.Text('Nome Completo', size=(16,0)),sg.Input(key='linha1')],
    [sg.Text('Apartamento', size=(16,0)),sg.Input(key='linha2')],
    [sg.Text('Qnt de moradores', size=(16,0)),sg.Input(key='linha3')],
    [sg.Text('Possui veículo?', size=(16,0))],
    [sg.Checkbox('Sim',key='sim'),sg.Checkbox('Não',key='nao')],
    [sg.Button('Incluir',key='incluir')],
    [sg.Output(size=(60,10))]
    ]
#janela
janela = sg.Window('Dados Morador').layout(layout)
        
while True:      
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        break
        
    if event == 'incluir':
        n = values['linha1']
        a = values['linha2']
        q = values['linha3']
        vs = values['sim']
        vn = values['nao']
        
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

            
            

                 
                

               

              
                
                

            

    





