import socket

# Cria o socket(Do tipo 'internet' e 'stream')
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Adiciona o ip e a porta para a comunicação
host = socket.gethostname()
port = 50000
# Conecta o socket de acordo com a porta e o ip
clientsocket.connect((host, port))
print('################################################################################=-')
print('Conversor de unidades')
print('################################################################################')

opcao = ''
opcaoprosv = ''
while opcao != '0':
    print(' Escolha qual conversão você deseja fazer:')
    print('1 - Conversor de Comprimento')
    print('2 - Conversor de Moedas')
    print('3 - Conversor de Temperatura')
    print('4 - Encerrar o programa')
    print('################################################################################')
    opcao = input('Escolha: ')
    print('################################################################################')
    if opcao == '1':
        while opcao != '4':
            print('Escolha qual conversão você deseja fazer:')
            print('1 - Metro => km')
            print('2 - Metro => Cm')
            print('3 - Metro => Mm')
            print('4 - Voltar => menu principal!')
            opcao = input('Escolha: ')
            print('################################################################################')

            if opcao == '1':
                opcaoprosv = '1'
                print('1 - Converter de Metros para Quilometros')
                medida = (input('Digite valor em metros para conversão: '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(medida.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  Valor em Km = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')
                # opcao = '4'

            elif opcao == '2':
                opcaoprosv = '2'
                print('2 - Converter de Metros para Centimetros')
                medida = (input('Digite valor em metros para conversão: '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(medida.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  Valor em Cm = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')
                # opcao = '4'

            elif opcao == '3':
                opcaoprosv = '3'
                print('3 - Converter de Metros para Milimetros')
                medida = (input('Digite valor em metros para conversão: '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(medida.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  Valor em Mm = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')
                # opcao = '4'

    elif opcao == '2':
        while opcao != '4':
            print('  Escolha sua conversao:')
            print('  1 - Real => Dolar')
            print('  2 - Real => Euro')
            print('  3 - Real => Libra')
            print('  4 - Voltar => Menu')
            opcao = input('  Escolha: ')
            print('################################################################################')

            if opcao == '1':
                opcaoprosv = '4'
                real = (input('Digite valor em reais para conversão: R$ '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(real.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('Valor em Dolar = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')

            elif opcao == '2':
                opcaoprosv = '5'
                real = (input('Digite valor em reais para conversão: R$ '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(real.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  \33[1:Valor em Euro = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')

            elif opcao == '3':
                opcaoprosv = '6'
                real = (input('Digite valor em reais para conversão: R$ '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(real.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  \33[1:Valor em Libra = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')

    elif opcao == '3':
        while opcao != '4':
            print('  Escolha sua conversao:')
            print('  1 - Celsius => Farenheit')
            print('  2 - Celsius => Kelvin')
            print('  4 - Voltar => Menu Principal')
            opcao = input('  Escolha: ')
            print('################################################################################')

            if opcao == '1':
                opcaoprosv = '7'
                c = (input('Digite valor em Celsius para conversão:  '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(c.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  Temperatura em FARENHEIT = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')

            elif opcao == '2':
                opcaoprosv = '8'
                c = (input('Digite valor em Celsius para conversão:  '))
                clientsocket.send(opcaoprosv.encode('ascii'))
                clientsocket.send(c.encode('ascii'))
                calculos = clientsocket.recv(2048)
                print('  Temperatura em KELVIN = {0}'.format(calculos.decode('ascii')))
                print('################################################################################')

    elif opcao == '4':
        print('Conexão Encerrada! Volte Sempre.')
        print('################################################################################')
        clientsocket.close()
        exit()
    else:
        print(' Opção Invalida')
        print('################################################################################')
