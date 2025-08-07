import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 저울
 *
 * 무게가 다른 N개의 물건이 있다. (1~N)
 * 양팔 저울로 어떤 게 무거운지 측정한 결과표를 가지고 있다.
 *
 * N = 5~100
 * M = 0~2000
 *
 * 물건의 개수 N과 일부 물건 쌍의 비교결과가 주어졌을 때
 * 각 물건에 대해서, 그 물건과의 비교결과를 알 수 없는 물건의 개수를 출력하세요.
 *
 * ((플로이드 워셜로도 풀 수 있다고 적혀있어서 풀었지, 아니였음 그냥 dfs를 사용했을 것 같다.))
 */
public class BOJ_10159 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(br.readLine());
    int pair = Integer.parseInt(br.readLine());

    // 인접리스트
    int[][] graph = new int[num+1][num+1];
    int INF = 101;
    for(int s=1; s<=num; s++) {
      for (int e = 1; e <= num; e++) {
        graph[s][e] = INF; // INF
        if(s==e) graph[s][e] = 0;
      }
    }

    for(int i=0; i<pair; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int heavy = Integer.parseInt(st.nextToken());
      int light = Integer.parseInt(st.nextToken());
      graph[heavy][light]=1;
    }

    // 플로이드워셜
    for(int k=1; k<=num; k++){
      for(int s=1; s<=num; s++){
        for(int e=1; e<=num; e++){
          graph[s][e] = Math.min(graph[s][e], graph[s][k]+graph[k][e]);
        }
      }
    }

    int[] answer  = new int[num+1];
    for(int i=1; i<=num; i++){
      for(int j=1; j<=num; j++){
        if(graph[i][j] + graph[j][i] == 2*INF){
         // i와 j는 대소 비교를 할 수 없음
          answer[i]++;
        }
      }
    }

    for(int i=1; i<=num; i++){
      System.out.println(answer[i]);
    }

  }
}
