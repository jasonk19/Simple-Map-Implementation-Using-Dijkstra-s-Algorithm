package lib;

import java.util.Comparator;

public class ConnectionComparator implements Comparator<Connection> {
  @Override
  public int compare(Connection c1, Connection c2) {
    if (c1.getWeight() < c2.getWeight()) {
      return -1;
    } else if (c1.getWeight() > c2.getWeight()) {
      return 1;
    }
    return 0;
  }
}