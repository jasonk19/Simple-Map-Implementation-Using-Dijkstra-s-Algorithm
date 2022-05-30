package lib;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class FileReader {

  public void readFile(String path, List<String> res) {
    try {
      File file = new File("../test/" + path);
      Scanner scanner = new Scanner(file);
      while(scanner.hasNextLine()) {
        String data = scanner.nextLine();
        res.add(data);
      }
      scanner.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occured");
      e.printStackTrace();
    }
  }

}
