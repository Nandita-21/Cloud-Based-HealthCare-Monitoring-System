import threading
import Pyro4

from Pyro4 import expose


@expose
class Server(object):
    def __init__(self):
        self.counter = 0

    def increment_counter(self):
        self.counter += 1
        return self.counter

    def decrement_counter(self):
        self.counter -= 1
        return self.counter


daemon = Pyro4.Daemon()
server = Server()

uri = daemon.register(server)
print("Server URI:", uri)


def start_server():
    daemon.requestLoop()


server_thread = threading.Thread(target=start_server)
server_thread.start()
