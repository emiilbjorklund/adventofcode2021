import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

import javax.sound.sampled.SourceDataLine;

public class PartOne {

   private static void run(List<String> input) {

      String gamma = "";
      String epsilon = "";


      for (int _i = 0; _i < input.get(0).length(); _i++) {
         var i = _i;
         var freq = input.stream().map(k -> k.charAt(i)).collect(Collectors.groupingBy(j -> j, Collectors.counting()));
         gamma += Collections.max(freq.entrySet(), Comparator.comparingLong(Map.Entry::getValue)).getKey();
         epsilon += Collections.min(freq.entrySet(), Comparator.comparingLong(Map.Entry::getValue)).getKey();
      }

      System.out.println(Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2));

   }

   public static void main(String[] args) throws IOException {

      List<String> input = new ArrayList<>();

      try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
         String line;
         for (;;) {
            line = reader.readLine();
            if (null == line || line.length() == 0)
               break;
            input.add(line);
         }
      }

      run(input);
   }

}