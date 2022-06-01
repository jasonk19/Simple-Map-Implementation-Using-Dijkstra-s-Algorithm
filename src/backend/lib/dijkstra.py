import heapq
from importlib.resources import path

class Dijkstra:
  def __init__(self, collection, src, dest):
    self.collection = collection
    self.src = src
    self.dest = dest
    self.total_cost = 0
    self.path = []
  
  def solveDuaArah(self):
    self.path.append(self.src.node)

    pq = []
    heapq.heapify(pq)
    while self.path[-1] != self.dest.node:
      for connection in self.collection:
        if connection.first.node == self.path[-1] or connection.second.node == self.path[-1]:
          if (connection.first.node in self.path and connection.second.node in self.path) == False:
            heapq.heappush(pq, connection)
          
      first_element = heapq.heappop(pq)
      self.collection.remove(first_element)
      if self.path[-1] == first_element.first.node:
        self.path.append(first_element.second.node)
      elif self.path[-1] == first_element.second.node:
        self.path.append(first_element.first.node)
      self.total_cost += first_element.cost
      pq.clear()
    return self.path, self.total_cost

  def solveBerarah(self):
    self.path.append(self.src.node)

    pq = []
    heapq.heapify(pq)
    while self.path[-1] != self.dest.node:
      for connection in self.collection:
        if connection.first.node == self.path[-1]:
          heapq.heappush(pq, connection)
          
      first_element = heapq.heappop(pq)
      self.collection.remove(first_element)
      if self.path[-1] == first_element.first.node:
        self.path.append(first_element.second.node)
      self.total_cost += first_element.cost
      pq.clear()
    return self.path, self.total_cost
  
  def print(self):
    for i in range(len(self.path)):
      if i != len(self.path) - 1:
        print(f"{self.path[i]} -> ", end="")
      else:
        print(f"{self.path[i]}", end=" = ")
    print(f"{self.total_cost}")