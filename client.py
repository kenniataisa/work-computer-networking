import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"  
    server_port = 8000
    client.connect((server_ip, server_port))

    while True:
        msg = input("Digite peso e altura (ou 'sair' para encerrar): ")
        client.send(msg.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        if response.lower() == "closed":
            break
        print("Resposta do servidor:", response)

    client.close()

if __name__ == "__main__":
    run_client()
