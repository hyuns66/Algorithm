import kotlin.math.max

fun main() {
    val (N, M) = readln().split(" ").map { it.toInt() }
    val graph = mutableListOf<MutableList<Int>>()
    val dp = MutableList(N) {
        MutableList(M) { 0 }
    }
    for (i in 1 .. N) {
        val list = readln().split(" ").map { it.toInt() }.toMutableList()
        graph.add(list)
    }

    dp[0][0] = graph[0][0]
    for (y in 0 until N) {
        for (x in 0 until M) {
            val cost = graph[y][x]
            for ((dy, dx) in listOf(listOf(-1, 0), listOf(0, -1), listOf(-1, -1))) {
                val py = y+dy
                val px = x+dx
                if (py < 0 || px < 0 || py >= N || px >= M) continue
                dp[y][x] = max(dp[y][x], dp[py][px] + cost)
            }
        }
    }

    print(dp[N-1][M-1])
}
