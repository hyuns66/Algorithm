import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 호텔
 *
 * 수입을 늘리기 위해 홍보를 하려고한다.
 *
 * 각 도시별로 홍보하는데 드는 비용과, 그 때 몇명의 고객이 늘어나는지 정보가 있다.
 * 이러한 정보에 나타난 돈의 정수배 만큼 투자할 수 있다.
 *
 * 각 도시에는 무한명의 잠재적인 고객이 있다.
 * 고객을 적어도 C명 늘이기 위해 투자해야하는 돈의 최솟값은?
 *
 * ------------------
 * 특이하게 그러면
 * dp[4] = 4인데 하나의값에 최소를 담는게 아니라, 가능한 뒤에껄 다보네..?
 * 적어도 C명 늘이기 위한거라 그런지! 적어도..!!
 *
 * ------------------
 * 배낭 문제
 */
public class BOJ_1106 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int target = Integer.parseInt(st.nextToken()); // 1~1000
    int cityNum = Integer.parseInt(st.nextToken()); // 1~20

    int dp[] = new int[target+101];
    for(int i=1; i<=target+100; i++){
      dp[i] = 100*i; // 1명 섭외에 드는 최대비용은 100이니까
    }

    for(int i=0; i<cityNum; i++){
      st = new StringTokenizer(br.readLine());
      int cost = Integer.parseInt(st.nextToken()); // 1~100
      int customer = Integer.parseInt(st.nextToken()); // 1~100

      for(int j=customer; j<=target+100; j++){
        dp[j] = Math.min(dp[j], dp[j-customer]+cost);
      }
    }

    int answer = Integer.MAX_VALUE;
    for(int i=target; i<=target+100; i++){
        answer = Math.min(answer, dp[i]);
    }

    // 가장 작은돈으로 target만큼의 투자자를 모으려면??
    System.out.println(answer);
  }
}
