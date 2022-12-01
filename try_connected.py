
# def conectando_banco():
#     try:
#         conexao = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'bandaltkd',
#             database = 'bdyoutube'
#         )
#         print("Conexão estabelecida com Banco de dados.")

#     except mysql.connector.Error as error:
#         if error.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Banco de dados não existe.")
#         elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Nome do usuario ou Senha está errado.")         
#         else:
#             print(error)
#     else:
#         conexao.close()        

    

# conectando_banco()    

# try:
#     conexao = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'bandaltkd',
#         database = 'bdyoutube'
#     )
#     print("Conexão estabelecida com Banco de dados.")

# except mysql.connector.Error as error:
#         if error.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Banco de dados não existe.")
#         elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Nome do usuario ou Senha está errado.")         
#         else:
#             print(error)
# else:
#     conexao.close()        

