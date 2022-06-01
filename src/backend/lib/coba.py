from connection import Connection
from node import Node
from connection_collection import ConnectionCollection
from dijkstra import Dijkstra

# Test reader
file = open("test1.txt", 'r')
lines = file.readlines()
lines = [line.rstrip().replace(" ", "") for line in lines]

collection = ConnectionCollection()

for line in lines:
  n1 = Node(line[0].upper())
  n2 = Node(line[1].upper())
  c = int(line[2])
  connection = Connection(n1, n2, c)
  collection.add(connection)

list_collection = collection.getCollection()

source = Node("A")
destination = Node("Z")

solver = Dijkstra(list_collection, source, destination)
solver.solveDuaArah()
solver.print()