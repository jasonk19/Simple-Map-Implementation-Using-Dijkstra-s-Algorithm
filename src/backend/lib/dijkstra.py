import heapq
import time
from importlib.resources import path

class Dijkstra:
  def __init__(self, collection, src, dest):
    self.collection = collection
    self.src = src
    self.dest = dest
    self.total_cost = 0
    self.iteration = 0
    self.exec_time = 0
    self.steps = ""
    self.path = []
  
  def solveDuaArah(self):
    start_time = time.time()
    self.path.append(self.src.node)

    pq = []
    heapq.heapify(pq)
    while self.path[-1] != self.dest.node:
      for connection in self.collection:
        if connection.first.node == self.path[-1] or connection.second.node == self.path[-1]:
          if (connection.first.node in self.path and connection.second.node in self.path) == False:
            heapq.heappush(pq, connection)
            self.iteration += 1

      in_pq = False
      dest_connection = None
      for connection in pq:
        if connection.second.node == self.dest.node:
          in_pq = True
          dest_connection = connection

      if in_pq:
        first_element = dest_connection
      else:
        first_element = heapq.heappop(pq)    

      first_element_to_string = first_element.first.node + " -> " + first_element.second.node + " = " + str(first_element.cost) + ", "
      self.steps += first_element_to_string
      self.collection.remove(first_element)
      if self.path[-1] == first_element.first.node:
        self.path.append(first_element.second.node)
      elif self.path[-1] == first_element.second.node:
        self.path.append(first_element.first.node)
      self.total_cost += first_element.cost
      pq.clear()
    self.exec_time = time.time() - start_time
    return self.path, self.total_cost, self.iteration, self.exec_time, self.steps

  def solveBerarah(self):
    start_time = time.time()
    self.path.append(self.src.node)

    pq = []
    heapq.heapify(pq)
    while self.path[-1] != self.dest.node:
      for connection in self.collection:
        if connection.first.node == self.path[-1]:
          heapq.heappush(pq, connection)
          self.iteration += 1
      
      in_pq = False
      dest_connection = None
      for connection in pq:
        if connection.second.node == self.dest.node:
          in_pq = True
          dest_connection = connection

      if in_pq:
        first_element = dest_connection
      else:
        first_element = heapq.heappop(pq)
      
      first_element_to_string = first_element.first.node + " -> " + first_element.second.node + " = " + str(first_element.cost) + ", "
      self.steps += first_element_to_string
      self.collection.remove(first_element)
      if self.path[-1] == first_element.first.node:
        self.path.append(first_element.second.node)
      self.total_cost += first_element.cost
      pq.clear()
    self.exec_time = time.time() - start_time
    return self.path, self.total_cost, self.iteration, self.exec_time, self.steps

  def print(self):
    for i in range(len(self.path)):
      if i != len(self.path) - 1:
        print(f"{self.path[i]} -> ", end="")
      else:
        print(f"{self.path[i]}", end=" = ")
    print(f"{self.total_cost}")