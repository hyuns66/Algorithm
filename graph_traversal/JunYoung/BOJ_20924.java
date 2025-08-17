import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 트리의 기둥과 가지
 * - 시에 있는 나무의 기둥 길이와, 가장 긴 가지의 길이를 파악해라!
 * - 기가노드를 정의
 *   - 루트노드에서 순회를 시작했을 때, 처음으로 자식노드가 2개 이상인 노드
 *   - 기둥-가지를 줄여 기가노드라 이름 붙였다 ㅎㅎㅎㅎ
 *   - 리프노드까지 갈 경우, 리프노드가 기가노드가 된다. (자식이 0개)
 *
 * [기둥] : 루트노드~기가노드까지의 간선의 합
 * [가지] : 기가노드~임의의 리프노드의 간선의 합
 *
 * ===========================================================================================
 * 풀긴 풀었는데, 쵸콤 더럽게 푼 느낌이다!
 */
public class BOJ_20924 {

  static class Node{
    int vertex;
    int weight;

    Node(int vertex, int weight){
      this.vertex = vertex;
      this.weight = weight;
    }
  }

  static void dfs(int node, int weightSum){
    visited[node] = true;
    // 기둥길이가 초기화 되지 않았을 때,
    if (gigaLength==-1){
      // 자식수가 1이 아니면 기가노드이므로 현재까지의 합을 기둥길이로 저장!
      if(weightSum==0){ // 루트노드기준으론 연결된게 1이어야함
        if(graph[node].size()!=1){
          gigaLength = weightSum;
          weightSum = 0;
        }
      }else{ // 루트노드 이후론 연결된게 2이어야 기둥임
        if(graph[node].size()!=2){
          gigaLength = weightSum;
          weightSum = 0;
        }
      }
    }else { // 기가노드를 이후에 0(리프노드)을 만났다면,
      if(graph[node].size()==1){
        maxBranchLength=Math.max(maxBranchLength,weightSum);
      }
    }

    // 자식노드로 이동
    for(Node child : graph[node]){
      if(visited[child.vertex]) continue;
      dfs(child.vertex, weightSum+child.weight);
    }
    visited[node] = false;
  }

  static boolean[] visited;
  static List<Node>[] graph;
  static int gigaLength = -1;
  static int maxBranchLength=0;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int nodeNum = Integer.parseInt(st.nextToken()); // 1~200,000(이십만)
    int root = Integer.parseInt(st.nextToken()); // 1~N

    // 그래프 생성
    graph = new ArrayList[nodeNum+1];
    for(int i=1; i<=nodeNum; i++){
      graph[i] = new ArrayList<>();
    }

    for(int i=0; i<nodeNum-1; i++){
      st = new StringTokenizer(br.readLine());

      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken()); // 1~1,000

      graph[nodeA].add(new Node(nodeB, weight));
      graph[nodeB].add(new Node(nodeA, weight));
    }

    visited= new boolean[nodeNum+1];
    dfs(root, 0);

    System.out.printf("%d %d\n", gigaLength, maxBranchLength);
  }
}
