import sqlite3

conn = sqlite3.connect('Clientest.db')
cursor = conn.cursor()
#Criando a tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Cpf TEXT,
    Contato TEXT,
    Nome TEXT,
    Custo REAL,
    Preco REAL,
    Lucro REAL,
    Envio TEXT,
    Chegada TEXT
    );""")
#Decidindo pra onde ir no menu
resp = int(input('O que você deseja fazer:\n'
                 '1 - Inserir dados\n'
                 '2 - Todos os clientes e seus contatos\n'
                 '3 - O custo de todos os processos\n'
                 '4 - O lucro obtido em todos os processos\n'
                 '0 - Para sair \n'))
c = 0
while(resp !=0):
#Parte 1, onde exibe as perguntas que inserem dados
    if (resp == 1):
        while(c != 's'):
            cpf = str(input('CPF(11 dígitos): '))
            while(len(cpf)!= 11):
                print('Erro no CPF, digite novamente')
                cpf = str(input('CPF(11 dígitos): '))
            nome = str(input('Nome: '))
            while(len(nome)>50):
                print('ERRO, nome muito longo!')
                nome = str(input('Nome: '))
            tel = str(input('Telefone: '))
            cust = float(input('Custo: '))
            prec = float(input('Preço: '))
            lucro = float(prec - cust)
            env = str(input('Data de envio: (DDMMAA) '))
            while(len(env)!= 6):
                print('Erro na data de envio, digite novamente')
                env = str(input('Data de envio: (DDMMAA) '))
            ch = str(input('Data de chegada: (DDMMAA) '))
            while(len(ch)!= 6):
                print('Erro na data de chegada, digite novamente')
                ch = str(input('Data de chegada: (DDMMAA) '))

            cursor.execute("""INSERT INTO clientes(Cpf, Nome, Contato, Custo,Preco, Lucro, Envio, Chegada )
            VALUES(?,?,?,?,?,?,?,?)""", (cpf, nome, tel, float(cust), float(prec), float(lucro), env, ch))
            conn.commit()
            c = str(input('Deseja parar? SIM ou NÃO ').lower())
            if (c != 'sim'):
                continue
        resp = int(input('O que você deseja fazer:\n'
                         '1 - Inserir dados\n'
                         '2 - Todos os clientes e seus contatos\n'
                         '3 - O custo de todos os processos\n'
                         '4 - O lucro obtido em todos os processos\n'
                         '0 - Para sair \n'))

#Parte 2, onde exibe o CPF, contato e o nome
    elif(resp == 2):
        cont = cursor.execute("SELECT * FROM clientes")
        print('CPF          Contato             Nome')
        for row in cont:
            print(row[1], '  ',row[2], '           ', row[3])
        resp = int(input('O que você deseja fazer:\n'
                         '1 - Inserir dados\n'
                         '2 - Todos os clientes e seus contatos\n'
                         '3 - O custo de todos os processos\n'
                         '4 - O lucro obtido em todos os processos\n'
                         '0 - Para sair \n'))
#Parte 3, onde exibe o CPF e o custo
    elif(resp == 3):
        sum_cust = []
        lc = cursor.execute("SELECT * FROM clientes")
        for row in lc:
            print('    CPF          Custo')
            print(row[1], '    ','R$', row[4])
            sum_cust.append(row[4])


        print(' Gasto total: R$',sum(sum_cust))
        resp = int(input('O que você deseja fazer:\n'
                         '1 - Inserir dados\n'
                         '2 - Todos os clientes e seus contatos\n'
                         '3 - O custo de todos os processos\n'
                         '4 - O lucro obtido em todos os processos\n'
                         '0 - Para sair \n'))
#Parte 4, onde exibe CPF, custo, preço e o lucro
    elif(resp == 4):
        sum_lucro = []
        sl = cursor.execute("SELECT * FROM clientes")
        for row in sl:
            print('CPF             Custo        Preço        Lucro')
            print(row[1],'    R$',row[4],'    R$',row[5],'    R$',row[6] )
            sum_lucro.append(float(row[6]))
        print('Lucro total: R$',sum(sum_lucro))
        resp = int(input('O que você deseja fazer:\n'
                         '1 - Inserir dados\n'
                         '2 - Todos os clientes e seus contatos\n'
                         '3 - O custo de todos os processos\n'
                         '4 - O lucro obtido em todos os processos\n'
                         '0 - Para sair \n'))
#Parte 5, onde você fecha o menu
    elif(resp==0):
        break
#Parte '6', onde há um looping caso alguém digite um número além dos que estão dispostos no menu
    else:
        print('Não há essa opção, veja o menu e responda novamente.')
        resp = int(input('O que você deseja fazer:\n'
                         '1 - Inserir dados\n'
                         '2 - Todos os clientes e seus contatos\n'
                         '3 - O custo de todos os processos\n'
                         '4 - O lucro obtido em todos os processos\n'
                         '0 - Para sair \n'))


conn.close()
