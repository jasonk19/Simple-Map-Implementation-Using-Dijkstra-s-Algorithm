class ConnectionCollection:
  def __init__(self):
    self.collection = []

  def add(self, connection):
    self.collection.append(connection)
  
  def getCollection(self):
    return self.collection
  
  def print(self):
    for connection in self.collection:
      connection.printConnection()