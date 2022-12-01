from connected_database import conexao
from colored import fg, bg, attr

def login():
    cursor = conexao.cursor()
    
    nome = str(input("Insira seu usuario: "))
    senha = str(input("Insira sua Senha: "))


    seleciona = f'SELECT * FROM usuarios WHERE nome = "{nome}" AND senha = "{senha}"'
    cursor.execute(seleciona)
    nome_usuario = cursor.fetchall()    
    # print(nome_usuario)


    
    if len(nome_usuario)!=0 and len(senha) != 0:  #Verifica se o retorno contém alguma linha        
        if senha:
            print('Usuario Conectado')
    else:
        print('usuario ou senha não existem')
        print(f'{fg(1)}{bg(15)} usuario ou senha não existem {attr(0)}')
    cursor.close()    


login()    