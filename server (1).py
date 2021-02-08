import socket
import time
import json
import conversor



# Cria o socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Adiciona o ip e a porta.
host = socket.gethostname()
port = 50000
# Disponibiliza o socket dentro do servidor.
serversocket.bind((host, port))
# Disponibiliza o socket para ser utilizado 'x' vezes se for necessário.
serversocket.listen()

while True:
    # Aceita a conexão.
    clientsocket, addr = serversocket.accept()   

    while True:
        opcao = clientsocket.recv(1024)
        opcao = opcao.decode('ascii')
        valor = clientsocket.recv(1024)
        valor = float(valor.decode('ascii'))

        if opcao == '1':
            unidades = conversor.Comprimento(valor)
            unidades = unidades.quilometro()

        elif opcao == '2':
            unidades = conversor.Comprimento(valor)
            unidades = unidades.centimetro()

        elif opcao == '3':
            unidades = conversor.Comprimento(valor)
            unidades = unidades.milimetro()

        elif opcao == '4':
            unidades = conversor.Moedas(valor)
            unidades = unidades.dolar()

        elif opcao == '5':
            unidades = conversor.Moedas(valor)
            unidades = unidades.euro()

        elif opcao == '6':
            unidades = conversor.Moedas(valor)
            unidades = unidades.libra()

        elif opcao == '7':
            unidades = conversor.Temperatura(valor)
            unidades = unidades.far()

        elif opcao == '8':
            unidades = conversor.Temperatura(valor)
            unidades = unidades.kelvin()

        unidades = json.dumps(unidades)
        clientsocket.send(unidades.encode('ascii'))
        print(' \33[1:32mInformaçao enviada com sucesso!\33[m ')
        del unidades