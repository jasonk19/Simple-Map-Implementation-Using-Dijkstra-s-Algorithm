import lib.*;

import java.util.*;

public class Main {
  public static void main(String[] args) {
    ConnectionCollection collection = new ConnectionCollection();
    List<String> result = new ArrayList<>();
    FileReader fr = new FileReader();
    fr.readFile("test1.txt", result);

    for (String data : result) {
      String[] splitData = data.split("\\s+");
      Connection connection = new Connection(new Node(splitData[0].charAt(0)), new Node(splitData[1].charAt(0)), Integer.parseInt(splitData[2]));
      collection.addConnection(connection);
    }

    List<Connection> connections = collection.getCollection();
    Node source = new Node('A');
    Node destination = new Node('Z');

    Dijkstra solver = new Dijkstra(connections, source, destination);
    solver.solve();
    solver.printSolution();
  }
}