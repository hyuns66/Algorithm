import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 택배
 *
 * 경로표 =
 * 한 집하장에서 다른 집하장으로 최단 경로로 화물을 이동시키기 위해
 * 가장 먼저 거쳐야하는 집하장
 */
public class BOJ_1719 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 집하장의 개수와, 집하장간 경로의 개수
    // nodeNum = 200이하의 자연수
    // edgeNum = 10,000이하의 자연수
    int nodeNum = Integer.parseInt(st.nextToken());
    int edgeNum = Integer.parseInt(st.nextToken());


    int INF = 200001;
    int[][] graph = new int[nodeNum+1][nodeNum+1];
    int[][] nextNode = new int[nodeNum+1][nodeNum+1];

    for(int i=1; i<=nodeNum; i++) {
      for (int j = 1; j <= nodeNum; j++) {
        graph[i][j] = INF; // Integer.MAX_VALUE로 하면 더 하기 할 때 오버플로우 날 수 있음!
        if(i==j) graph[i][j] = 0;

        nextNode[i][j] = j;
        nextNode[j][i] = i;
      }
    }

    for(int i=0; i<edgeNum; i++){
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      graph[nodeA][nodeB] = weight;
      graph[nodeB][nodeA] = weight;
    }

    // 플로이드 워셜 = 3중 for문!
    // 바깥쪽이 k, 출발, 도착
    // 기존값보다 k를 거쳐서 가는게 더 작으면 업데이트 해준다!
    for(int k=1; k<=nodeNum; k++){
      for(int s=1; s<=nodeNum; s++){
        for(int e=1; e<=nodeNum; e++){
          if(graph[s][k]+graph[k][e]<graph[s][e]){
            graph[s][e] = graph[s][k] + graph[k][e];
            nextNode[s][e] = nextNode[s][k];
          }
        }
      }
    }

    for(int s=1; s<=nodeNum; s++){
      for(int e=1; e<=nodeNum; e++){
        if(s==e) System.out.print("- ");
        else System.out.print(nextNode[s][e]+" ");
      }
      System.out.println();
    }

  }
}
