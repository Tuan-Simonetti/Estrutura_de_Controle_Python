import datetime, time, pprint

feed = []

register_date = {}

register_balance = {}

funcionalidades = (
"register", "del_register", "transfer", "deposit", "saque", "balance", "show_feed", "help_desafio", "logoff")


def introdução():
    print("""

     _______   _______     _______.     ___       _______  __    ______             _______   ___________    ____ 
    |       \ |   ____|   /       |    /   \     |   ____||  |  /  __  \           |       \ |   ____\   \  /   / 
    |  .--.  ||  |__     |   (----`   /  ^  \    |  |__   |  | |  |  |  |          |  .--.  ||  |__   \   \/   /  
    |  |  |  ||   __|     \   \      /  /_\  \   |   __|  |  | |  |  |  |          |  |  |  ||   __|   \      /   
    |  '--'  ||  |____.----)   |    /  _____  \  |  |     |  | |  `--'  |          |  '--'  ||  |____   \    /    
    |_______/ |_______|_______/    /__/     \__\ |__|     |__|  \______/           |_______/ |_______|   \__/     

    \n\n

    Olá, este programa é um exercício de avaliação para o processo seletivo na área de desenvolvimento do PicPay. 

    O enunciado do exercício é:

            Tem-se usuários comuns e lokistas, ambos têm carteira. Usuários podem enviar dinheiro (efetuar transações)
            para lojistas e entre usuários. Lojistas não podem enviar dinheiro para usuários. Cada transação gera um 
            registro de feed. A operação de depósito insere dinheiro na carteira do usuário. A operação de exibir feed
            retorna, em linguagem amigável, todas as transações que acontecerem desde que sua aplicação foi iniciada.
            Todos os dados devem ser armazenados em memória. Comandos que precisam ser imprementados:

            * Cadastro de usuário: register username seller | consumer
            * Inserir dinheiro na carteira de usuário: deposit username value
            * Efetuar transferências de valor: transfer source destination value
            * Exibir saldo: balance username
            * Exibir feed: show_feed

            Exemplo de funcionamento da aplicação no terminal:
            > register usrula1996 consumer
            ursula1996 registrado com sucesso

            > deposit ursula1996 10.0
            ursula1996 agora tem R$ 10.0 em sua carteira

            > register celso1993 consumer
            celso1993 registrado com sucesso

            > transfer celso1993 ursula 1996  2.00
            Não foi possível completar transação

            > transfer ursula1996 celso1993 2.50
            ursula1996 enviou R$ 2.5 para celso1993

            > balance ursula1996
            ursula1996 tem R$ 5.5 em sua carteira

            > show_feed
            ursula1996 enviou R$ 2.0 para celso1993
            ursula1996 enviou R$ 2.5 para celso1993

    Neste programa foi realizada a implementação da função "help_desafio". Por meio dela, uma lista das funções é exibida,
    contendo explicações de cada uma delas.

    Espero que gostem, vamos ao programa.

    Data Inicio: 28/03/2020, às 13:26h
    Data Conclusão: 28/03/2020, às 15:10h.

    Atualizações: 
    * 30/03/2020, às 10:47h - Foi adicionado os logs de erros quando deixa de escrever todos os parâmetros de cada função.
    * 30/03/2020, às 11:35h - Foi adiocionado o log de erro quando não escreve uma função válida.
    """)
    print(80 * '-')
    proximo = input(str("Pressione 'Enter' para continuar..."))


def register(username, tipo):
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    if username in register_date.keys():
        feed.append(f"Tentativa de registro inexitosa, porque o username {username} já existia. {time}")
        print(f"Este username já existe. Por gentileza, tente registrar outro. {time}.")

    else:
        register_date[username] = tipo
        register_balance[username] = float(0)
        feed.append(f"{username} se cadastrou como {tipo}, {time}.")
        print(f"Cadastro realizado com sucesso, no dia {time}.\n{80 * '-'}.")


def del_register(username):
    time = (
        f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    if float(register_balance[username]) == 0:
        del register_date[username]
        del register_balance[username]
        feed.append(f"{username} foi removido do sistema. {time}.")
        print(f"{username} foi removido com sucesso. {time}.")

    if float(register_balance[username]) > 0:
        feed.append(
            f"Foi feita uma tentativa de remoção do usuário {username}. Porém, não foi possível em virtude do mesmo possuir saldo remanscente, no valor de R$ {register_balance[username]}. {time}.")
        print(
            "Esta conta ainda possui saldo remanescente. Para que esta conta seja removida, é necessário realizar um saque do seu saldo de carteira.")


def transfer(source, destination, value):
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    if register_date[source] == "consumer":
        if float(register_balance[source]) >= float(value):
            transaction = (f"{source} realizou um pagamento para {destination}, no valor de R$ {value}. {time}.")
            register_balance[source] = float(register_balance[source]) - float(value)
            register_balance[destination] = float(register_balance[destination]) + float(value)
            feed.append(transaction)
            print("Pagamento realizado com sucesso.")

        else:
            feed.append(
                f"{source} não possui saldo suficiente. {source} desejou realizar uma transfarência no valor de {value}. Porém, seu saldo era de {register_balance[source]}. {time}")
            print("Você não tem saldo suficiente.")
    if register_date[source] == "seller":
        feed.append(
            f"O usuário {source} realizou uma tentativa de pagamento. Porém, sua conta não está apta a realizá-la. {time}.")
        print(f"O tipo da conta do usuário {source} não está apta a realizar transações, apenas receber. {time}.")


def deposit(username, value):
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    register_balance[username] = float(register_balance[username]) + float(value)
    feed.append(f"{username} realizou uma adição de saldo à sua carteira, no valor de R$ {value}. {time}.")
    print(f"Sua adição, no valor de R$ {value}, foi realizada com sucesso. {time}.")


def saque(username, banco, value):
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    if float(register_balance[username]) >= float(value):
        register_balance[username] = float(register_balance[username]) - float(value)
        feed.append(
            f"{username} realizou um saque de saldo à sua carteira, para o banco {banco}, no valor de R$ {value}. {time}.")
        print(f"Sua retirada, no valor de R$ {value}, foi realizada com sucesso. {time}.")

    else:
        feed.append(
            f"{username} tentou realiza um saque de saldo à sua carteira, para o banco {banco}, no valor de R$ {value}. Mas seu saldo era de R$ {register_balance[username]}. Solicitação inexitosa. {time}.")
        print(
            f"Você não possui saldo suficiente para retirar o valor de R$ {value}. Seu saldo atual é de R$ {register_balance[username]}. {time}.")


def balance(username):
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    feed.append(
        f"Foi realizada consulta de saldo do usuário {username}, ao qual possuía R$ {register_balance[username]} de saldo. {time}.")
    print(
        f"O usuário {username} possui R$ {register_balance[username]}. Consulta realizada no dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}.")


def show_feed():
    time = (
        f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
    feed.append(f"Foi realizada uma consulta dos feeds. {time}.")
    pprint.pprint(feed)


def help_do_programa():
    print("""
    1) A função REGISTER exerce a tarefa de criar uma conta com o username indicado.
    Esta função necessita de 2 parametros: "USERNAME" e "TIPO".
    - USERNAME: nome de usuário que deseja cadastrar;
    - TIPO: se a conta é CONSUMER (consumidor pessoa física) ou SELLER (pessoa jurídica/lojista)
    EXEMPLO:
    Terminal > register tuan consumer
    Terminal > register biricast seller


    2) A função DEL_REGISTER realiza a função de excluir o username indicado. 
    Esta função necessita de 1 parâmetro: "username".
    - USERNAME: nome de usuário que deseja excluir;
    EXEMPLO:
    Terminal > del_register tuan


    3) A função TRANSFER realiza a tarefa de transferir valores, como se fosse um pagamento. 
    Esta função pede 3 parâmetros: "souce", "destination" e "value".
    - SOUCE: username do pagador;
    - DESTINATION: username do recebedor;
    - VALUE: quantia que o SOUCE deseja pagar ao DESTINATION;
    EXEMPLO:
    Terminal > transfer tuan cozendey 10.0


    4) A função DEPOSIT realiza a tarefa de adicionar quantias à sua conta. 
    Esta função pede 2 parâmetros: "USERNAME" e "VALUE".
    - USERNAME: nome de usuário que deseja cadastrar;
    - VALUE: quantia monetária;
    EXEMPLO:
    Terminal > deposit tuan 10.0


    5) A função SAQUE realiza a tarefa de transferir o valor desejado para um banco.
    Esta função pede 3 parâmtros: "USERNAME", "BANCO" e "VALUE".
    - USERNAME: nome de usuário que deseja cadastrar;
    - VALUE: quantia monetária;
    EXEMPLO:
    Terminal > saque tuan original 10.0


    6) A função BALANCE realiza a tarefa de indicar o seu saldo naquele exato momento. 
    Esta função requer 1 parâmetro: "USERNAME".
    - USERNAME: nome de usuário que deseja cadastrar;
    EXEMPLO:
    Terminal > balance tuan


    7) A função SHOW_FEED realiza a tarefa de exibir todas as funções executadas e,
    também, aquelas que não tiveram êxito. Esta função não pede parâmetros, basta 
    escrevê-la.
    EXEMPLO:
    Terminal > show_feed


    8) A função HELP_DESAFIO exibe na tela todas as funções criadas e que podem ser 
    executadas neste programa.
    Ela exibe, ainda, os parâmetros necessários e demonstra exemplos. 
    Assim como a função SHOW_FEED, esta função não requer parâmetros, basta escrevê-la.
    EXEMPLO:
    Terminal > help_desafio


    9) A função LOGOFF desliga o sistema. Assim como a função SHOW_FEED, esta função 
    não requer parâmetros, basta escrevê-la.
    EXEMPLO:
    Terminal > logoff
    """)


# ----------------------------------------- Montagem do algoritmo ------------------------------------------------------
introdução()
logoff = "não"
while logoff != "sim":
    menu = str(input(f"""\n{80 * '-'}\nTerminal > """))
    menu_minusculas = menu.lower()
    funcoes = menu_minusculas.split()

    if funcoes[0] == "register":
        try:
            username = funcoes[1]
        except:
            print("Você deixou de informar o USERNAME. A consturação da função é: 'register username consumer/seller'.")

        try:
            tipo = funcoes[2]
        except:
            print(
                "Você deixou de informar o tipo (CONSUMER/SELLER). A consturação da função é: 'register username consumer/seller'.")

        try:
            register(username, tipo)
        except:
            print("Erro na função: 'register(username, tipo)'.")

    if funcoes[0] == "del_register":
        try:
            username = funcoes[1]
            confirmacao = str(input(f"Você tem certeza que deseja excluir a conta {username} [s/n]? "))
            if confirmacao == "s":
                try:
                    del_register(username)
                except:
                    print("Erro na execução da função: 'del_register(username)'.")

            else:
                time = (
                    f"Dia {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, às {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
                feed.append(f"Exclusão da conta {username} não foi completada. {time}.")
                print(f"Não houve exclusão da conta. {time}.")
        except:
            print("Você deixou de informar o USERNAME. A consturação da função é: 'del_register username'.")

    if funcoes[0] == "transfer":
        try:
            source = funcoes[1]
        except:
            print("Você deixou de informar o SOURCE. A consturação da função é: 'transfer source destination value'.")

        try:
            destination = funcoes[2]
        except:
            print(
                "Você deixou de informar o DESTINATION. A consturação da função é: 'transfer source destination value'.")

        try:
            value = funcoes[3]
        except:
            print("Você deixou de informar o VALUE. A consturação da função é: 'transfer source destination value'.")

        try:
            transfer(source, destination, value)
        except:
            print("Erro na função: 'transfer(source, destination, value)'.")

    if funcoes[0] == "deposit":
        try:
            username = funcoes[1]
        except:
            print("Você deixou de informar o USERNAME. A consturação da função é: 'deposit username value'.")

        try:
            value = float(funcoes[2])
        except:
            print("Você deixou de informar o VALUE. A consturação da função é: 'deposit username value'.")

        try:
            deposit(username, value)
        except:
            print("Erro na função: 'deposit(username, value)'.")

    if funcoes[0] == "saque":
        try:
            username = funcoes[1]
        except:
            print("Você deixou de informar o USERNAME. A consturação da função é: 'saque username, banco valor'.")

        try:
            banco = funcoes[2]
        except:
            print("Você deixou de informar o BANCO. A consturação da função é: 'saque username, banco valor'.")

        try:
            value = float(funcoes[3])
        except:
            print("Você deixou de informar o VALOR. A consturação da função é: 'saque username, banco valor'.")

        try:
            saque(username, banco, value)
        except:
            print("Erro na função: 'saque(username, banco, value)'.")

    if funcoes[0] == "balance":
        try:
            username = funcoes[1]
        except:
            print("Você deixou de informar o USERNAME. A consturação da função é: 'saque username, banco valor'.")

        try:
            balance(username)
        except:
            print("Erro na função: 'balance(username)'.")

    if funcoes[0] == "show_feed":
        try:
            show_feed()

        except:
            print("Erro na função: 'show_feed()'.")

    if funcoes[0] == "help_desafio":
        try:
            help_do_programa()
        except:
            print("Erro na função: 'show_feed()'.")

    if funcoes[0] == "logoff":
        print("Sistema está fazendo logoff...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("..")
        time.sleep(2)
        print(".")
        print("Sistema desligado.")
        break

    if funcoes[0] not in funcionalidades:
        print(
            f"'{funcoes[0]}' não é uma função reconhecida pelo programa. Recomendamos consultar a função 'help_desafio'.")