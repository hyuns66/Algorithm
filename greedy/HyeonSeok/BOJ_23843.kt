fun main() {
    var (N, M) = readln().split(" ").map { it.toInt() }
    val charge_time = readln().split(" ").map{it.toInt()}.sorted()
    var idx = N-1
    var answer = 0

    while (idx >= 0) {
        val current_time = charge_time[idx]
        idx -= 1
        answer += current_time
        var plugs = M-1
        while (plugs > 0) {
            var temp = 0
            while (idx >= 0) {
                if (temp == current_time) break
                temp += charge_time[idx]
                idx -= 1
            }
            plugs -= 1
        }
    }
    print(answer)
}