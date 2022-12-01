import mysql.connector
from mysql.connector import errorcode

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'bandaltkd',
    database = 'bdyoutube'
)

print('\n \x1b[6;30;42m' + 'Conexão estabelecida com Banco de dados.' + '\x1b[0m \n')



