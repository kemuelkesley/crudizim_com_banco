
def leilaInt(msg):
    ok = False
    valor = 0
    while True:
        id_professor = str(input(msg))
        if id_professor.isnumeric():
            valor = int(id_professor)
            ok = True
        else:
            print('Erro digite um número novamente')
        if ok:
            break
    return valor

# original
# def leilaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('Erro digite um número novamente')
#         if ok:
#             break
#     return valor

# n = leilaInt("Digite um número: ")

# Receber apenas números no input.


# id_professor = leilaInt("Digite um número: ")
# print(f"Vc acabou de digitar {id_professor}")                