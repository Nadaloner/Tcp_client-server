import socket

target_host="127.0.0.1"
target_port=9998

#creazione ogetto socket --> SOCK_STREAM == tcp 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connessione al client
client.connect((target_host,target_port))

#invio di dati
client.send(b"let's gosky")

#ricezione della risposta
response=client.recv(4096)

print(response.decode("utf-8"))

#chiusura del socket
client.close()
