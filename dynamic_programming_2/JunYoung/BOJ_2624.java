import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 동전 바꿔주기
 *
 * 명보네 동네 가게의 현금 출납기에는
 * n1, n2, ~nk의 k가지 동전이 들어있다.
 *
 * 가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔주려고한다.
 *
 */
public class BOJ_2624 {
    static class Node{
        int value;
        int addValue;

        Node(int value, int addValue){
            this.value = value;
            this.addValue = addValue;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int money = Integer.parseInt(br.readLine()); // 지폐의 금액 (1~10000)
        int variety = Integer.parseInt(br.readLine()); // 동전의 가짓수 (1~100)

        int[] dp = new int[money+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int value = Integer.parseInt(st.nextToken());
        int num = Integer.parseInt(st.nextToken());
        for(int i=1; i<=num; i++){
            if(value*i>money) continue;
            dp[value*i] = 1;
        }
        dp[0] =1;
        //System.out.println(Arrays.toString(dp));

        // 100 * 1000 * 10000 = 1,000,000,000 (10억)

        // 첫번째 동전을 제외한 나머지 동전들에 대해서
        for(int i=1; i<variety; i++){ // 100
            st = new StringTokenizer(br.readLine());
            value = Integer.parseInt(st.nextToken());
            num = Integer.parseInt(st.nextToken());

            Queue<Node> queue = new ArrayDeque<>();
            for(int s=0; s<dp.length; s++){ // 10000
                if(dp[s]!=0){
                    for(int t=1; t<=num; t++){ // 1000
                        if(s+t*value>money) continue;
                        queue.add(new Node(s+t*value, dp[s]));
                    }
                }
            }

            while (!queue.isEmpty()){
                Node poll = queue.poll();
                dp[poll.value] += poll.addValue;
            }
            //System.out.println(Arrays.toString(dp));
        }


        // 정답 출력
        System.out.println(dp[money]);
    }
}
