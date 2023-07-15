import socket

import Utils

class Client:
    def start_connection(self, ip, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.out = self.client_socket.makefile('w')
            self.inp = self.client_socket.makefile('r')
            return True
        except Exception as e:
            print("Error starting the connection:", str(e))
            return False

    @staticmethod
    def create():
        client = Client()
        client_connected = client.start_connection("127.0.0.1", 4444)

        if not client_connected:
            Utils.client_logger("Erro al conectarse al servidor.")
            return

        Utils.client_logger("Se conecto al servidor correctamente")

        for i in range(Utils.NUM_GENERACIONES):
            Utils.client_logger("Esperando la poblacion")
            populationAsString = client.receive_message()
            # Imprime los mensajes que son enviados del server y lo que recibe del cliente
            Utils.server_logger(populationAsString)
            Utils.client_logger(populationAsString)

            population = Utils.string_to_population(populationAsString)
            Utils.evaluarPoblacion(population)
            Utils.seleccionar_mejores(population)
            population = Utils.realizar_cruzamiento(population)
            Utils.realizar_mutacion(population)
            population_to_string = Utils.population_to_string(population)
            print('Enviando ... ')
            Utils.client_logger(population_to_string)
            client.send_message(population_to_string)



    def send_message(self, msg):
        try:
            self.out.write(msg + '\n')
            self.out.flush()
        except Exception as e:
            print("TCP Client: Error sending message - ", e)

    def receive_message(self):
        return self.inp.readline().strip()

    def close_connection(self):
        self.client_socket.close()

    def stopConnection(self):
        try:
            self.inp.close()
            self.out.close()
            self.client_socket.close()
            return True
        except Exception as e:
            print("Error stopping the connection: ", str(e))
            return False





