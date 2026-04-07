import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 성냥개비
 *
 * 성냥개비는 숫자를 나타내기에 아주 이상적인 도구다.
 * 성냥개비의 개수가 주어졌을 때,
 * 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰수를 찾는 프로그램을 만들자
 *
 *  [가장 작은 수 만들기 =  dp]
 *  2~7개로 만들 수 있는 가장 작은 수를 미리 세팅합니다.
 *  dp[i] = min(dp[i], text합치기(dp[i - j], weight[숫자_j]))
 *  j는 2~7의 숫자
 *
 * [가장 큰 수 만들기 = 그리디]
 * 성냥개비가 홀수라면: 가장 앞에 7을 놓고, 나머지는 모두 1로 채운다.
 * 성냥개비가 짤수라면: 모든 자릿수를 1로 채운다.
 *
 * -------------------------------------------------------------------------
 * [그리디, dp, 근데 두뇌를 잘써야하는...]
 * - 답지 보고 품...
 */
public class BOJ_3687 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testNum = Integer.parseInt(br.readLine()); // 테스트 케이스의 수(1~100)

        // 해당 성냥개비로 만들 수 있는 최소 숫자
        long[] minDp = new long[101];
        Arrays.fill(minDp, Long.MAX_VALUE);
        minDp[2] = 1;
        minDp[3] = 7;
        minDp[4] = 4;
        minDp[5] = 2;
        minDp[6] = 6;
        minDp[7] = 8;

        String[] add = {"1", "7", "4", "2", "0", "8"}; // 각 성냥 2~7개로 만들 수 있는 가장 작은 수
        // 2~7까지는 위에서 수동으로 초기화 완료
        for (int i = 8; i <= 100; i++) {
            for (int j = 2; j <= 7; j++) {
                // minDp[i-j]가 아직 초기값(MAX)이라면 유효한 숫자가 아니므로 건너뜁니다.
                if (minDp[i - j] == Long.MAX_VALUE) continue;

                // i개에서 j개를 뺀 결과(dp[i-j]) 뒤에,
                // j개로 만들 수 있는 가장 작은 '숫자'를 이어 붙임
                String current = minDp[i - j] + String.valueOf(add[j-2]);
                long val = Long.parseLong(current);

                if (minDp[i] > val) {
                    minDp[i] = val;
                }
            }
        }

        for(int i=0; i<testNum; i++){
            int fireStickNum = Integer.parseInt(br.readLine()); // 성냥개비의 수(2~10)
            // 각 테스트 케이스에 대해서 입력으로 주어진 성냥개비를 모두!! 이용해 만들 수 있는 가장 작은 수와 큰수를 출력해라

            StringBuilder sb = new StringBuilder();
            int temp = fireStickNum;
            if (temp%2!=0){
                sb.append("7");
                temp-=3;
            }
            while(temp>0){
                sb.append("1");
                temp-=2;
            }

            System.out.println(minDp[fireStickNum]+" "+sb.toString());
        }
    }
}
