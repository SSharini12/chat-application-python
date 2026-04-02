import socket
import threading

host = input("Enter server IP: ")
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

username = input("Choose a username: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
