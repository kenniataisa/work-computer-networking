import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "0.0.0.0"  
    port = 8000
    server.bind((server_ip, port))
    server.listen(1)
    print(f"Escutando em {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Conexão aceita de {client_address}")

    while True:
        request = client_socket.recv(1024)
        if not request:
            break

        request = request.decode("utf-8").strip()

        if request.lower() == "sair":
            client_socket.send("closed".encode("utf-8"))
            break

        try:
            peso, altura = map(float, request.split())
            imc = peso / (altura ** 2)
            if imc >= 25:
                response = "Fat"
            else:
                response = "Thin"
        except:
            response = "Erro: envie 'peso altura'"

        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    server.close()
    print("Servidor encerrado")

if __name__ == "__main__":
    run_server()
