import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 동전
 *
 * 우리나라 화폐단위 동전에는 1원,5원,10원,50원,100원,500원이있다.
 * 동전의 종류가 주어졌을 때, 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오
 */
public class BOJ_9084 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for(int tc=0; tc<testCase; tc++){
            int coinVariety = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            // 코인의 종류 (1~10000원)
            int[] coins = new int[coinVariety];
            for(int i=0; i<coinVariety; i++){
                coins[i] = Integer.parseInt(st.nextToken());
            }

            int target =Integer.parseInt(br.readLine());

            // dp[coinValue] = coinValue값을 만들기 위한 경우의 수
            int[] dp = new int[target+1];
//            int minCoin = 10001;
//            for(int i=0; i<coinVariety; i++){
//                int coinValue = coins[i];
//                if(coinValue<minCoin) minCoin = coinValue;
//                dp[coinValue] = 1;
//            }

            // 2*minCoin부터 target까지 dp를 구하기
//            for(int i=2*minCoin; i<=target; i++){
//                int count = dp[i];
//                for(int j=0; j<coinVariety; j++){
//                    int coinValue = coins[j];
//                    if(i-coinValue<=0) continue;
//                    count += dp[i-coinValue];
//                }
//                dp[i] = count;
//            }

            for(int i=0; i<coinVariety; i++){
                int coinValue = coins[i];
                if(coinValue>target) continue;

                dp[coinValue] +=1;
                for(int j=coinValue+1; j<=target; j++){
                    dp[j] += dp[j-coinValue];
                }

//                System.out.println("coinValue"+coinValue);
//                for(int s=1; s<=target; s++){
//                    System.out.print(dp[s]+" ");
//                }
//                System.out.println();
            }



            System.out.println(dp[target]);
        }
    }
}
