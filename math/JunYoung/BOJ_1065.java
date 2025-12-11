import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 한 수
 * 양의 정수 X의 각자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
 * 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하시오
 * ====================================================
 * 처음에는 등차가 0이나 음수가 될 수 있는걸 고려하지 않았다..!!!
 * 그래서 각 두자리수, 세자리수, 네자리수에 대해서 등차가 x인걸 따려서
 * ex) 두자리수면 a+x<=9 && 11a+x<=N인 경우 count++ 했었다. -> 틀린 로직!
 */
public class BOJ_1065 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력
        int N = Integer.parseInt(br.readLine());

        System.out.println(arithmetic_sequence(N));
    }

    public static int arithmetic_sequence(int num) {
        int cnt = 0; // 한수 카운팅

        if (num < 100) {
            // 1. 1부터 99까지는 모두 한수임
            return num;
        } else {
            // 2. 100 이상의 수가 들어오면 일단 99개는 먹고 들어감
            cnt = 99;

            // 1000은 등차수열이 아니므로 예외처리 (또는 루프를 999까지만 돌림)
            if (num == 1000) {
                num = 999;
            }

            // 100부터 입력받은 num까지 반복
            for (int i = 100; i <= num; i++) {
                int hun = i / 100;       // 백의 자리
                int ten = (i / 10) % 10; // 십의 자리
                int one = i % 10;        // 일의 자리

                // 등차수열 조건: (백-십)의 차이와 (십-일)의 차이가 같아야 함
                if ((hun - ten) == (ten - one)) {
                    cnt++;
                }
            }
        }

        return cnt;
    }
}
