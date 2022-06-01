class Connection:
  def __init__(self, first, second, cost):
    self.first = first
    self.second = second
    self.cost = cost
  
  def __lt__(self, other):
    return self.cost < other.cost
  
  def print(self):
    print(f"{self.first.node} -> {self.second.node} = {self.cost}")