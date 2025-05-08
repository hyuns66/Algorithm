fun main() {
    val N = readln().toInt()
    val graph = mutableListOf<MutableList<Int>>()

    for (idx in 0 until N) {
        val temp = readln().split(" ").map { it.toInt() }.toMutableList()
        graph.add(temp)
    }

    for (x in 0 until N) {
        for (y in 0 until N) {
            for (z in 0 until N) {
                if (graph[y][x] == 1 && graph[x][z] == 1) {
                    graph[y][z] = 1
                }
            }
        }
    }

    for (g in graph) {
        println(g.joinToString(" "))
    }
}