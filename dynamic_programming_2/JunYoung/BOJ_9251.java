import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

/**
 * 최장 공통 부분 수열
 */
public class BOJ_9251 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String s1 = br.readLine();
    String s2 = br.readLine();

    // dp 배열
    int[][] dp = new int[s1.length()+1][s2.length()+1];

    for (int i=1; i<=s1.length(); i++){
      for(int j=1; j<=s2.length(); j++){
        if(s1.charAt(i-1)==s2.charAt(j-1)){
          dp[i][j] = dp[i-1][j-1] + 1;
        }else{
          dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j]);
        }
      }
    }

    System.out.println(dp[s1.length()][s2.length()]);

  }
}
