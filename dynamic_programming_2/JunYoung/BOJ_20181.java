import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 꿈틀꿈틀 호석 애벌레 - 효율성
 *
 * N개의 먹이가 일렬로 나열된 나뭇가지
 * 시작 위치 = 0
 *
 * 호석 애벌레는 한번 먹이를 먹기 시작하면 연속적으로 먹어야한다.
 * 누적된 만족도가 K이상이거나 먹을 게 없을 떄 멈춘다.
 *
 * 최소 만족도 이상이 되면 탈피 에너지 축적
 *
 * ----------------------------------------
 * 탈피 에너지의 최대?
 *
 */
public class BOJ_20181 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    int[] branch = new int[N];
    for(int i=0; i<N; i++){
      branch[i] = Integer.parseInt(st.nextToken());
    }

    int left = 0;
    int right = 0;
    long[] dp = new long[N+1];
    long sum = Integer.toUnsignedLong(branch[right]);
    while(true){
//      System.out.println(left+":"+right);
//      System.out.println("sum="+sum);
      if(sum>=K){
        dp[right+1] = Math.max(dp[right+1],dp[left]+(sum-K));
        // 에너지 감소
        sum -= branch[left];
        left++;
        if(!(left>right)){
          continue;
        }
      }

      // 에너지 증가
      right++;
      // 종료 조건
      if (right==N){
        break;
      }
      dp[right+1]= dp[right];
      sum += branch[right];
    }

//    for(int i: dp){
//      System.out.print(i+" ");
//    }

    System.out.println(dp[N]);
  }
}
