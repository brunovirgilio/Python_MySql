import pymysql
import PySimpleGUI as sg
from database import *


layout = [
    [sg.Text('Nome Completo', size=(16,0)),sg.Input(key='linha1')],
    [sg.Text('Apartamento', size=(16,0)),sg.Input(key='linha2')],
    [sg.Text('Qnt de moradores', size=(16,0)),sg.Input(key='linha3')],
    [sg.Text('Possui veículo?', size=(16,0))],
    [sg.Checkbox('Sim',key='sim'),sg.Checkbox('Não',key='nao')],
    [sg.Button('Incluir',key='incluir'), sg.Button('Deletar',key='deletar'), sg.Button('Atualizar',key='alterar'),sg.Button('Exibir Lista',key='exibir'),sg.Button('Limpar Tela',key='limpar'), ],
    [sg.Output(size=(60,10), key ='_output_')]
    ]
#janela
janela = sg.Window('Lista de Moradores').layout(layout)
        
while True:      
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        break
    
    #try:   
    if event == 'incluir':
        n = values['linha1']
        a = values['linha2']
        q = values['linha3']
        vs = values['sim']
        vn = values['nao']
                
        cursor = conexao.cursor()
        incluir = 'INSERT INTO morador(nome, apt, qnt, vsim,vnao)VALUES(%s, %s, %s, %s, %s)'
        valor =(int(n),str(a),str(q),bool(vs),bool(vn))
        
        cursor.execute(incluir,valor)
        conexao.commit()
        print('CARREGAMENTO CONCLUÍDO')
        print(f'nome: {n}')
        print(f'apt: {a}')
        print(f'qnt: {q}')
        print(f'veiculo sim: {vs}')
        print(f'veiculo nao: {vn}')
    
    #except (ValueError):
        #print('FALHA: Verifique se o tipo da variável esta correto')
    
    #except (NameError):
        #print('FALHA: Verifique se a variável usada esta correspondente a declarada')
    
    #except Exception as erro:
        #print('FALHA: Foi encontrada a classe de erro abaixo:')
        #print(erro.__class__)

    if event == 'deletar':
        n = values['linha1']
        
        cursor = conexao.cursor()
        delete = f'DELETE FROM morador WHERE nome = "{n}"'
        
        cursor.execute(delete)
        conexao.commit()
        print('Dado excluido')

    if event == 'exibir':
        n = values['linha1']
        
        cursor = conexao.cursor()
        exibe = ' SELECT nome,apt,qnt,vsim from morador'
        
        cursor.execute(exibe)
        resultado = cursor.fetchall()
        
        print('Lista de Moradores(Nome/Apt/Qnt/carro):')
        for c in resultado :
            print(c)
    
    if event == 'limpar':
        janela.FindElement('_output_').Update(' ')

    if event == 'alterar':
        n = values['linha1']
        a = values['linha2']
        
        cursor = conexao.cursor()
        altere = f'UPDATE morador SET nome ="{n}" WHERE apt ="{a}"'
        
        cursor.execute(altere)
        conexao.commit()
        print('Dado atualizado')
        
      


            
            

                 
                

               

              
                
                

            

    





