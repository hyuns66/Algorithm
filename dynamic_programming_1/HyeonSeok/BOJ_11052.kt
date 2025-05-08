import kotlin.math.max

fun main() {
    val N = readln().toInt()
    val P = readln().split(" ").map{ it.toInt() }.toMutableList()
    val dp = (mutableListOf(0) + P).toMutableList()

    for (i in 0 .. N) {
        for (j in i .. N) {
            if (i + j > N) continue
            dp[i+j] = max(dp[i] + dp[j], dp[i+j])
        }
    }
    print(dp.last())
}