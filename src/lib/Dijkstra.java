package lib;

import java.util.*;

public class Dijkstra {
  private List<Connection> connections;
  private List<Character> path;
  private int totalWeight;
  private Node src;
  private Node dest;

  public Dijkstra(List<Connection> connections, Node src, Node dest) {
    this.connections = connections;
    this.src = src;
    this.dest = dest;
    this.path = new ArrayList<>();
    this.totalWeight = 0;
  }

  public void solve() {
    this.path.add(this.src.getNode());

    PriorityQueue<Connection> pq = new PriorityQueue<>(new ConnectionComparator());
    while (path.get(path.size() - 1) != this.dest.getNode()) {
      for (Connection connection : this.connections) {
        if (connection.getFirst().getNode() == this.path.get(path.size() - 1) || connection.getSecond().getNode() == this.path.get(path.size() - 1)) {
          if (!(this.path.contains(connection.getFirst().getNode()) && this.path.contains(connection.getSecond().getNode()))) {
            pq.add(connection);
          }
        }
      }
      this.connections.remove(pq.peek());
      try {
        if (path.get(path.size() - 1) == pq.peek().getFirst().getNode()) {
          this.path.add(pq.peek().getSecond().getNode());
        } else {
          this.path.add(pq.peek().getFirst().getNode());
        }
        this.totalWeight += pq.peek().getWeight();
      } catch (Exception e) {
        System.out.println("Null value in priority queue");
        return;
      }
      pq.clear();
    }
  }

  public void printSolution() {
    for (int i = 0; i < this.path.size(); i++) {
      if (i != this.path.size() - 1) {
        System.out.print(this.path.get(i) + " -> ");
      } else {
        System.out.print(this.path.get(i));
      }
    }
    System.out.print(" = " + this.totalWeight);
  }
}
