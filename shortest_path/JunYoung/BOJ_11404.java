import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 플로이드
 *
 * n개의 도시가 있다. (2~100)
 * 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다. (1~100,000=십만)
 *
 * 모든 도시의 쌍에서 도시 A에서 B로 가는데 필요한 비용의 최솟값?
 *
 * =============================
 * INF 설정 주의해서 하기!
 * =============================
 */
public class BOJ_11404 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int cityNum = Integer.parseInt(br.readLine());
    int busNum = Integer.parseInt(br.readLine());

    int[][] graph = new int[cityNum+1][cityNum+1];
    int INF = 100001*cityNum; // 비용은 100,000보다 작거나 같은 자연수이다.
    for(int s=1; s<=cityNum; s++) {
      for (int e = 1; e <= cityNum; e++) {
        graph[s][e] = INF;
        if(s==e) graph[s][e] = 0;
      }
    }

    for(int i=0; i<busNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      int cost = Integer.parseInt(st.nextToken());

      // 중복경로가 있을 수 있으므로
      graph[start][end] = Math.min(graph[start][end], cost);
    }

    // 플로이드 워셜
    for(int k=1; k<=cityNum; k++){
      for(int s=1; s<=cityNum; s++){
        for(int e=1; e<=cityNum; e++){
          graph[s][e] = Math.min(graph[s][e], graph[s][k]+graph[k][e]);
          //System.out.println(s+","+e+" 갱신됨 -> " + graph[s][e]);
        }
      }
    }

    // 출력
    for(int s=1; s<=cityNum; s++) {
      for (int e = 1; e <= cityNum; e++) {
        if(graph[s][e]==INF){
          System.out.print(0+" ");
        }else{
          System.out.print(graph[s][e]+" ");
        }
      }
      System.out.println();
    }


  }
}
