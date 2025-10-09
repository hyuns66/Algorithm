import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1학년
 *
 * 숫자가 줄지어있는 것을 보면 마지막 두 숫자 사이에는 =을 넣고,
 * 나머지 숫자 사이에는 + 또는 -를 넣어 등식을 만들어 놀았다.
 *
 * 중간에 나오는 수는 음수가 나올 수 없고, 0이상 20이하여야한다.
 * 숫자가 주어졌을 때 상근이가 만들 수 있는 올바른 등식의 수는?
 *
 * ===================================================
 * idea) 뭔가 dfs로 탐색했을 때 경우의 수가 너무 많아지면, dp를 생각해봐야겠다.
 */
public class BOJ_5557 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 숫자의 개수 = 3~100
        int num = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[num];

        // 접근2: i번째수까지 선택했을 때의 값이 뭐가 있는지
        // dp[i(0~N-1)][숫자(0~20)] : i번째수까지 선택했을 때 숫자값이 나올 경우의 수
        long[][] dp = new long[num-1][21];
        arr[0] = Integer.parseInt(st.nextToken());
        dp[0][arr[0]] = 1;

        for(int i=1; i<num-1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            for(int j=0; j<=20; j++){
                long freq = dp[i-1][j];

                if(freq==0) continue;
                if(j-arr[i]>=0) dp[i][j-arr[i]] += freq;
                if(j+arr[i]<=20) dp[i][j+arr[i]] += freq;
            }
        }

        int target = Integer.parseInt(st.nextToken());

//        for(int pick=0; pick<num-1; pick++){
//            for(int n=0; n<=20; n++){
//                System.out.print(dp[pick][n]+" ");
//            }
//            System.out.println();
//        }

        System.out.print(dp[num-2][target]);

        // 접근1: 모든 경우의 수 해보기  = 2^(N-1) = 최대 2^99
        // 접근2: i번째수까지 선택했을 때의 값이 뭐가 있는지
    }
}
