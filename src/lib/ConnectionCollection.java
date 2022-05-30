package lib;

import java.util.*;


public class ConnectionCollection {
  private List<Connection> collection;

  public ConnectionCollection() {
    this.collection = new ArrayList<>();
  }

  public List<Connection> getCollection() {
    return this.collection;
  }

  public void addConnection(Connection connection) {
    this.collection.add(connection);
  }

  public void printConnection() {
    for (Connection connection : collection) {
      connection.print();
    }
  }
}
