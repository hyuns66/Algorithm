import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 역사
 *
 * 세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때,
 * 주어진 사건들의 전후 관계도 알 수 있을까?
 *
 * 앞에 있는 번호의 사건이
 * 먼저 일어났으면 -1
 * 뒤에 일어났으면 1
 * 어떤지 모르면 0
 *
 * ------------------------
 * 접근1(잘못된 접근). 전,후 관계가 있어서 위상정렬인가 생각했는데 그러면
 *    1 -> 2-> 3
 *    4-> 5-> 3
 *   에서 1,5의 전후관계는 알 수 없는데 위상정렬로 하면 1=4 / 2=5 / 3 이기 때문에
 *   1이 5보다 전에 일어난 일이라 생각할 수 있어서 XXXXX
 *
 * -------------------------
 *  접근2. 플로이드워셜
 *  - a->b 갈 수 있다면 a가 먼저 일어난 사건
 *  - b->a 갈 수 있다면 a가 뒤에 일어난 사건
 *  - 둘다 할 수 없다면 0
 *  으로 분류가능하다.
 */
public class BOJ_1613 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int caseNum = Integer.parseInt(st.nextToken());
    int infoNum = Integer.parseInt(st.nextToken());

    // 인접행렬
    int[][] graph = new int[caseNum+1][caseNum+1];
    int INF = 401; // 사건수가 400개니까 다 거쳐와도 가중치가 1이라면 401을 넘을 수 없음.
    for(int i=1; i<=caseNum; i++){
      for(int j=1; j<=caseNum; j++){
        if(i==j) graph[i][j] = 0;
        else graph[i][j] = INF;
      }
    }

    // pre->next 방향
    for(int i=0; i<infoNum; i++){
      st = new StringTokenizer(br.readLine());
      int pre = Integer.parseInt(st.nextToken());
      int next = Integer.parseInt(st.nextToken());
      graph[pre][next] = 1; // 가중치 1부여함
    }

    // 플로이드 워셜
    for(int k=1; k<=caseNum; k++){
      for(int s=1; s<=caseNum; s++){
        for(int e=1; e<=caseNum; e++){
          graph[s][e] = Math.min(graph[s][e], graph[s][k]+graph[k][e]);
        }
      }
    }

    int questionNum = Integer.parseInt(br.readLine());
    for(int i=0; i<questionNum; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      if(graph[a][b]<INF) {
        System.out.println(-1);
      } else if (graph[b][a]<INF){
        System.out.println(1);
      }else {
        System.out.println(0);
      }
    }
  }

}
