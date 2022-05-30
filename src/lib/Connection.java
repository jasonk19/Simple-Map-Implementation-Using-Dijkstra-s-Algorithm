package lib;

public class Connection {
  private Node first;
  private Node second;
  private int weight;

  public Connection(Node first, Node second, int weight) {
    this.first = first;
    this.second = second;
    this.weight = weight;
  }

  public Node getFirst() {
    return this.first;
  }

  public Node getSecond() {
    return this.second;
  }

  public int getWeight() {
    return this.weight;
  }

  public void print() {
    System.out.println(this.first.getNode() + " -> " + this.second.getNode() + " = " + this.weight);
  }
}
