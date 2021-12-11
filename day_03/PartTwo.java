import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;


public class PartTwo {

   private static void run(List<String> input) {

      List<String> oxygen = new ArrayList<>();
      List<String> co2 = new ArrayList<>();

      oxygen.addAll(input);
      co2.addAll(input);

      for (int _i = 0; _i < input.get(0).length(); _i++) {
         var i = _i;
         var freq = oxygen.stream().map(k -> k.charAt(i)).collect(Collectors.groupingBy(j -> j, Collectors.counting()));

         var bit = freq.get('0') == freq.get('1') ? '1'
               : Collections.max(freq.entrySet(), Comparator.comparingLong(Map.Entry::getValue)).getKey();
         var filter = oxygen.stream().filter(k -> k.charAt(i) == bit).collect(Collectors.toList());
         oxygen.clear();
         oxygen.addAll(filter);
      }

      for (int _i = 0; _i < input.get(0).length(); _i++) {
         var i = _i;
         var freq = co2.stream().map(k -> k.charAt(i)).collect(Collectors.groupingBy(j -> j, Collectors.counting()));

         var bit = freq.get('0') == freq.get('1') ? '0'
               : Collections.min(freq.entrySet(), Comparator.comparingLong(Map.Entry::getValue)).getKey();
         var filter = co2.stream().filter(k -> k.charAt(i) == bit).collect(Collectors.toList());
         co2.clear();
         co2.addAll(filter);
      }

      System.out.println(Integer.parseInt(oxygen.get(0), 2) * Integer.parseInt(co2.get(0), 2));

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