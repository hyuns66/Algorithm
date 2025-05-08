fun backtracking(chars : List<String>, idx: Int, depth : Int, answer : List<String>, R : Int, C : Int) {
    val vowels = listOf("a", "e", "o", "i", "u")
    if (depth == R) {
        var vowel_cnt = 0
        var consonant_cnt = 0
        for (a in answer) {
            if (a in vowels) vowel_cnt += 1
            else consonant_cnt += 1
        }
        if (vowel_cnt >= 1 && consonant_cnt >= 2) println(answer.joinToString(""))
        return
    }
    for (i in idx until C) {
        val next_answer = answer + listOf(chars[i])
        backtracking(chars, i+1, depth+1, next_answer, R, C)
    }
}

fun main() {
    val (R, C) = readln().split(" ").map {it.toInt()}
    val inputs = readln().split(" ")
    val chars = inputs.sorted()

    backtracking(chars, 0, 0, listOf(), R, C)
}