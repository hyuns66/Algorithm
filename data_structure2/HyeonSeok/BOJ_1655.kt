import java.util.PriorityQueue

fun main() {
    val N = readln().toInt()
    val smallHeap = PriorityQueue<Int>()
    val bigHeap = PriorityQueue<Int>()
    var middleNum = 10001

    for (i in 1 .. N) {
        val num = readln().toInt()
        // 중간 숫자보다 크거나 작은경우에 따라 힙 삽입
        if (num < middleNum) {
            // smallHeap 사이즈 초과 방지 (균형 맞추기)
            if (smallHeap.size > bigHeap.size) {
                smallHeap.poll().let {
                    bigHeap.add(-it)
                }
            }
            smallHeap.add(-num)
        } else {
            // bigHeap 사이즈 초과 방지 (균형 맞추기)
            if (bigHeap.size > smallHeap.size) {
                bigHeap.poll().let {
                    smallHeap.add(-it)
                }
            }
            bigHeap.add(num)
        }
        // 중간 수 업데이트
        if (smallHeap.size >= bigHeap.size) middleNum = -smallHeap.peek()
        else middleNum = bigHeap.peek()

        print("$middleNum\n")
    }
}
