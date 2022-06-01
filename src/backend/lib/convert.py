from backend.lib.connection import Connection
from backend.lib.node import Node
from backend.lib.connection_collection import ConnectionCollection

def convert(file):
  lines = file.replace(" ", "").split("\n")
  collection = ConnectionCollection()

  for line in lines:
    n1 = Node(line[0].upper())
    n2 = Node(line[1].upper())
    c = int(line[2])
    connection = Connection(n1, n2, c)
    collection.add(connection)

  list_collection = collection.getCollection()
  return list_collection

def getNodes(file):
  lines = file.replace(" ", "").split("\n")
  nodes = []
  for line in lines:
    if line[0] not in nodes:
      nodes.append(line[0])
    if line[1] not in nodes:
      nodes.append(line[1])
  return nodes