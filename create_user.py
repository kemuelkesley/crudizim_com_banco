from connected_database import conexao
from datetime import date
from datetime import time
from datetime import datetime


def criar_usuario_senha():
    cursor = conexao.cursor()
    
    nome = str(input('Criar Usuario: ')).replace(" ", "")    
    
    while True:
        senha = str(input("Digite sua senha : "))
        if senha.islower():
            print("A senha deve ter pelo menos um caractere MAIUSCULO: ")
        elif len(senha) < 6 :
            print("A senha deve ter pelo menos 8 caracteres: ")
        elif senha.isalpha() :
            print("Necessita de um numero: ")
        elif senha.isalnum() :
            print("Necessita de um Caractere especial: ")
        else:
            break



    if len(nome) >= 6:
            
        data_criacao = datetime.now()
        sql = f'INSERT INTO usuarios (nome, senha, datacriacao) VALUES ("{nome}", "{senha}", "{data_criacao}")'
        cursor.execute(sql)
        conexao.commit()


        print(f'\x1b[6;30;42m' + 'Usuario: ' + nome + ' Criado com Sucesso.' + '\x1b[0m')
        print(f'Data da Criação do Usuario: {data_criacao}')
        # print(f'Usuario: {nome} Criado com Sucesso.')
        ver_usuario_criado = int(input('Deseja vê o o nome do seu usuario? 1 - Sim  2 - Não:'))
        
        if ver_usuario_criado == 1:
            print(f'Nome do seu usuario: {nome}: {data_criacao}')
        elif ver_usuario_criado == 2:
            # print(f'Sistema Finalizado.')
            print(f'\x1b[6;30;42m' + 'Sistema Finalizado.' + '\x1b[0m')
            
            
    else:
        if len(nome) < 6:
            print(f'Quantidade de Caractere insuficiente. Precisa ter pelo menos 6 caracteres.')
       
    cursor.close()



criar_usuario_senha()