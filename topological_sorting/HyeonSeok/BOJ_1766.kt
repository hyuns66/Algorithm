import java.util.PriorityQueue

fun addSoloNodes(minHeap : PriorityQueue<Int>, N : Int, restriction_count : MutableList<Int>, visited : MutableList<Boolean>) {
    for (i in 1 .. N) {
        if (restriction_count[i] == 0 && !visited[i]) {
            minHeap.add(i)
            visited[i] = true
        }
    }
}

fun main() {
    val (N, M) = readln().split(" ").map { it.toInt() }
    val restriction_count = MutableList(N+1) { 0 }
    val visited = MutableList(N+1) { false }
    val restriction_info = mutableMapOf<Int, MutableList<Int>>()
    for (i in 0 until M) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        restriction_count[b] += 1
        if (!restriction_info.containsKey(a)) restriction_info.put(a, mutableListOf())
        restriction_info[a]!!.add(b)
    }

    val minHeap = PriorityQueue<Int>()
    val answer = mutableListOf<Int>()
    addSoloNodes(minHeap, N, restriction_count, visited)

    // 위상 정렬
    while (minHeap.isNotEmpty()) {
        // 우선순위 가장 높은 노드 추출, 정답 업데이트
        val node = minHeap.poll()
        answer.add(node)
        // 해당 노드에 대한 간선 제거
        if (restriction_info.containsKey(node)) {
            val restrictions = restriction_info[node]!!
            for (r in restrictions) {
                restriction_count[r] -= 1
                // 간선 제거 후 해당 노드의 진입점이 모두 사라졌으면 힙에 삽입
                if (restriction_count[r] == 0 && !visited[r]) {
                    visited[r] = true
                    minHeap.add(r)
                }
            }
        }
    }

    print(answer.joinToString(" "))
}