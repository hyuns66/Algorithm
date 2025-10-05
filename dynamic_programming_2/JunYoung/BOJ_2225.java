import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 합 분해
 *
 * 0~N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하시오
 * 덧셈의 순서가 바뀐 경우는 다른 경우다 (1+2!=2+1)
 *
 * N = 1~200
 * K = 1~200
 *
 * 사실.. 풀이 조큼 봤음..
 */
public class BOJ_2225 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numberMax = Integer.parseInt(st.nextToken());
        int splitNum = Integer.parseInt(st.nextToken());

        int[][] dp = new int[splitNum+1][numberMax+1];

        for(int i=0; i<=numberMax; i++){
            dp[1][i] = 1; // i번 숫자까지 1개로 만드는 거는 1가지 경우 뿐!
        }

        if(splitNum>=2){
            // 2개~splitNum개로
            for(int split=2; split<=splitNum; split++){
                // 숫자 num을 만들 수 있는 경우의 수 넣기
                for(int num = 0; num<=numberMax; num++){
                    for(int n=0; n<=num; n++){
                        dp[split][num] += dp[split-1][n];
                        dp[split][num] %= 1000000000;
                    }
                }
            }
        }

        System.out.println(dp[splitNum][numberMax]);

    }
}
