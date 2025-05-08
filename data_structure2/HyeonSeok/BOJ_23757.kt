import java.util.PriorityQueue

fun main() {
    val (N, M) = readln().split(" ").map { it.toInt() }
    val count = readln().split(" ").map{ it.toInt() }
    val want = readln().split(" ").map{ it.toInt() }

    val minHeap = PriorityQueue<Int>()
    for (c in count) {
        minHeap.add(-c)
    }

    var answer = 1
    for (w in want) {
        val c = -(minHeap.poll())
        if (c < w) {
            answer = 0
            break
        }
        minHeap.add(-(c-w))
    }
    print(answer)
}