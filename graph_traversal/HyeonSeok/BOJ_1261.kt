import java.util.PriorityQueue

fun main() {
    val (M, N) = readln().split(" ").map { it.toInt() }
    val graph = Array(N) { IntArray(M) {0} }
    for (i in 0 until N) {
        val inputString = readln()
        val inputArray = inputString.map{
            it.digitToInt()
        }.toIntArray()
        for (j in 0 until M) {
            graph[i][j] = inputArray[j]
        }
    }

    val pq = PriorityQueue<Triple<Int, Int, Int>>(
        compareBy {
            it.first
        }
    )
    val visited = Array(N) { BooleanArray(M) { false } }
    val dirs = arrayOf(
        intArrayOf(-1, 0),
        intArrayOf(1, 0),
        intArrayOf(0, 1),
        intArrayOf(0, -1)
    )
    pq.add(Triple(0, 0, 0))
    while (pq.isNotEmpty()) {
        val (count, y, x) = pq.poll()
        if (y == N-1 && x == M-1) {
            println(count)
            break
        }
        for ((dy, dx) in dirs) {
            val ty = y + dy
            val tx = x + dx
            if (ty < 0 || tx < 0 || ty >= N || tx >= M) continue
            if (visited[ty][tx]) continue
            visited[ty][tx] = true
            val newCount = if (graph[ty][tx] == 1) count+1 else count
            pq.add(Triple(newCount, ty, tx))
        }
    }
}
