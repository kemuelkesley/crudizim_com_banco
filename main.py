from connected_database import conexao
from input_numeros import leilaInt
import os
from colored import fg, bg, attr


def adicionar_professor():
    nome = str(input("Informe o Nome do Professor: "))
    disciplina = str(input("Informe a Disciplina do Professor: "))
    #Inserindo professores no banco.
    cursor = conexao.cursor()
    sql = f'INSERT INTO professores (nome, disciplina) VALUES ("{nome}", "{disciplina}")'
    cursor.execute(sql)
    conexao.commit()
    print(f"Professor:{nome} cadastrado com sucesso.")
    cursor.close()



def mostrar_professores():
    cursor = conexao.cursor()
    sql = f'SELECT * FROM professores'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    contador = 0
    for mostrar_professores in resultado:
        contador += 1
        print(f'{contador} - {mostrar_professores}')
    cursor.close()



def editar_professor():
    cursor = conexao.cursor()

    # chamei a função para deixar o campo só números.
    id_professor = leilaInt("Informe o ID do Professor:") 

    seleciona = f'SELECT * FROM professores WHERE idprofessores = {id_professor}'
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    print(resultado)
    
    # for i in resultado[0]:
    #     print(i)
    
    if (id_professor in resultado[0]):
        alterar_nome = str(input("Altere o nome do Professor: "))
        sql = f'UPDATE professores SET nome = "{alterar_nome}" WHERE idprofessores = {id_professor}'
        cursor.execute(sql)
        conexao.commit()
        print('\x1b[6;30;42m' + 'O Nome foi Alterado com Sucesso.' + '\x1b[0m')
        # print(f'O nome foi alterado para:{alterar_nome} com sucesso')
        cursor.close()
    

def editar_disciplina():
    cursor = conexao.cursor()
    id_professor = leilaInt("Informe o ID do Professor:") 
    seleciona = f'SELECT * FROM professores WHERE idprofessores = {id_professor}'
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    print(resultado)
    alterar_disciplina = str(input("Altere o nome da Disciplina: "))
    sql = f'UPDATE professores SET disciplina = "{alterar_disciplina}" WHERE idprofessores = {id_professor}'
    cursor.execute(sql)
    conexao.commit()    
    print('\n\x1b[6;30;42m' + 'O Nome da Disciplina foi Alterado com Sucesso.' + '\x1b[0m\n')
    cursor.close()



def tela_menu():
    print('/'*50)
    print('\n')
    print('CRUD VER.1.0\n')
    print('By Kemuel Kesley\n')
    print('/'*50)
    print('\n')
    print('-'*50)
    print('\n1 - Mostrar Professores:\n')
    print('-'*50)
    print('\n2 - Adicionar Professor:\n')
    print('-'*50)
    print('\n3 - Editar Nome do Professor:\n')
    print('-'*50)
    print('\n4 - Editar Nome da Disciplina:\n')
    print('-'*50)
    print('\n5 - Limpar Terminal:\n')
    print('-'*50)
    print('\n6 - Para Sair do Programa:\n')
    print('-'*50)

# Menu do Login

def tela_login():
    print('/'*50)
    print('\n')
    print('\n LOGIN \n')
    print('\n By Kemuel Kesley\n\n')
    print('/'*50)
    print('\n')
   


# teste de Login
def login():
    cursor = conexao.cursor()
    
    tela_login()

    nome = str(input("Usuario: "))
    senha = str(input("Senha: "))


    seleciona = f'SELECT * FROM usuarios WHERE nome = "{nome}" AND senha = "{senha}"'
    cursor.execute(seleciona)
    nome_usuario = cursor.fetchall()    
    # print(nome_usuario)
    
    if len(nome_usuario)!=0 and len(senha) != 0:  #Verifica se o retorno contém alguma linha        
        if senha:
            # print('\nUsuario Conectado\n')
            
            print('\n\x1b[6;30;42m' + 'Usuario Conectado.' + '\x1b[0m\n')

            while True:
                def escolha_opcao():
                    tela_menu()
                    # opc = int(input('Escolha a Opção desejada:'))

                    print('\n')
                    opc = leilaInt("Escolha a opção desejada:")

                    if opc == 1:
                        mostrar_professores()
                    
                    elif opc == 2:
                        adicionar_professor()

                    elif opc == 3:
                        editar_professor()
                        
                    elif opc == 4:
                        editar_disciplina()  

                    elif opc == 5:
                        print('Console limpadado com sucesso')
                        os.system('cls') or None
                        os.system('clear') or None 
                    
                    
                    elif opc == 6:
                        print()
                        print('\x1b[6;30;42m' + 'Programa finalizado com Sucesso.' + '\x1b[0m')
                        print()
                        exit()

                escolha_opcao()        
    
    else:
        # print('\n Usuario ou senha não existem, tente Novamente. \n')  
        print(f'\n {fg(1)}{bg(15)} Usuario ou senha não existe, tente Novamente. {attr(0)} \n')      

    cursor.close()    



if __name__== '__main__':
    login()
