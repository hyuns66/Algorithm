import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * 숫자세는 양(Small)
 *
 * - 숫자 N을 뽑는다.
 * - N, 2N, 3N등을 떠올린다.
 * - 숫자의 모든 자리수의 숫자들을 적어놓는데, 이미 적은 숫자는 적지 않는다.
 * - 0~9사이의 모든 숫자가 적히게 되면 잠에 든다.
 * -----------------------------------------------------------
 * N이 0만 아니면 결국 0~9사이의 자리수가 한번은 나오나보다.
 */
public class BOJ_14381 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testNum = Integer.parseInt(br.readLine());

        for(int tc=0; tc<testNum; tc++){
            int N = Integer.parseInt(br.readLine());
            if(N==0) {
                System.out.printf("Case #%d: %s\n", tc+1, "INSOMNIA");
                continue;
            }

            // 9가 될때까지 곱하기
            Set<Integer> set = new HashSet<>();
            int currentN = 0;
            while (set.size()<10){
                // N은 (i+1)N으로 만들기
                currentN += N;

                // tempN의 각 자리수를 set에 더하기
                int tempN = currentN;
                while (tempN>0){
                    set.add(tempN%10);
                    tempN = tempN/10;
                }
            }

            // 잠에 빠진 숫자 출력
            System.out.printf("Case #%d: %d\n", tc+1, currentN);
        }
    }
}
