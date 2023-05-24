import Pyro4

uri = input("Enter the server URI: ")
server = Pyro4.Proxy(uri)

print("Counter:", server.increment_counter())
print("Counter:", server.decrement_counter())
