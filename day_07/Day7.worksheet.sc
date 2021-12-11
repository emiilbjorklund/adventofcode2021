import scala.io.Source


val source = Source.fromFile("day_7/sample.txt").getLines

val input = source.next.split(",").map(_.toInt)


// PART 1
val median = input.sortWith(_ < _).drop(input.length/2).head

val fuel = input.map(_ - median).map(_.abs)

fuel.sum



// PART 2
// val avg = (input.sum.toFloat/input.size).round
// val avg = input.sum/input.size

// val fuel2 = input.map(x => (1 to (x - avg).abs).sum)

// fuel2.sum
