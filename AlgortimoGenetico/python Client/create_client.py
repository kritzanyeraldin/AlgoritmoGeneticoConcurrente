import threading
from Client import Client



def main():
    clients_size = 25
    for _ in range(clients_size):
        thread = threading.Thread(target=Client.create, name=str(_))
        print(thread.getName())
        thread.start()

if __name__ == '__main__':
    main()
