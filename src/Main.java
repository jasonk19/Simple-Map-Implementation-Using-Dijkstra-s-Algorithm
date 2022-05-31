import lib.*;

import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter test file (*.txt): ");
    String fileName = scanner.next();
    System.out.print("Starting point: ");
    Character sourceNode = scanner.next().charAt(0);
    System.out.print("End point: ");
    Character destinationNode = scanner.next().charAt(0);
    scanner.close();

    ConnectionCollection collection = new ConnectionCollection();
    List<String> result = new ArrayList<>();
    FileReader fr = new FileReader();
    fr.readFile(fileName, result);

    for (String data : result) {
      String[] splitData = data.split("\\s+");
      Connection connection = new Connection(new Node(splitData[0].charAt(0)), new Node(splitData[1].charAt(0)), Integer.parseInt(splitData[2]));
      collection.addConnection(connection);
    }

    List<Connection> connections = collection.getCollection();
    Node source = new Node(Character.toUpperCase(sourceNode));
    Node destination = new Node(Character.toUpperCase(destinationNode));

    Dijkstra solver = new Dijkstra(connections, source, destination);
    solver.solve();
    solver.printSolution();
  }
}