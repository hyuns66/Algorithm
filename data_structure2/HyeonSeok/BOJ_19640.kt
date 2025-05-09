import java.util.PriorityQueue

fun main() {
    val (N, M, K) = readln().split(" ").map { it.toInt() }
    val info = mutableListOf<List<Int>>()
    for (i in 0 until N) {
        val temp = readln().split(" ").map { it.toInt() }
        info.add(temp)
    }

    val minHeap = PriorityQueue(
        compareBy<List<Int>> { it[0] }
            .thenBy { it[1] }
            .thenBy { it[2] }
    )
    var line_num = 1
    val line_info = mutableListOf<ArrayDeque<List<Int>>>()
    for (i in 0 .. M-1) {
        line_info.add(ArrayDeque())
    }
    for (i in 0 until N) {
        val (D, H) = info[i]
        line_info[line_num-1].addFirst(listOf(D, H, i))
        line_num += 1
        if (line_num > M) line_num = 1
    }

    for (i in 0 until M) {
        if (i >= N) break
        val (D, H, person_num) = line_info[i].removeLast()
        minHeap.add(listOf(-D, -H, i, person_num))   // 근무일수, 급한정도, 줄번호, 사람번호
    }
    var answer = 0
    while (minHeap.isNotEmpty()) {
        val info = minHeap.poll()
        val line_num = info[2]
        if (line_info[line_num].isNotEmpty()) {
            val (D, H, person_num) = line_info[line_num].removeLast()
            minHeap.add(listOf(-D, -H, line_num, person_num))   // 근무일수, 급한정도, 줄번호, 사람번호
        }
        if (info[3] == K) break
        answer += 1
    }
    print(answer)
}