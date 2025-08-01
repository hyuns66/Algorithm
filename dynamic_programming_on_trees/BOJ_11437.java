import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * LCA : 최소 공통 조상
 */
public class BOJ_11437 {

  static class Node{
    int vertex;
    int depth;

    Node(int vertex, int depth){
      this.vertex = vertex;
      this.depth = depth;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int nodeNum = Integer.parseInt(br.readLine());

    // 1. 인접 리스트
    List<Integer>[] tree = new List[nodeNum+1];
    for(int i=1; i<=nodeNum; i++){
      tree[i] = new ArrayList<>();
    }

    for(int i=0; i<nodeNum-1; i++){
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      tree[nodeA].add(nodeB);
      tree[nodeB].add(nodeA);
    }

    // 2. 탐색 알고리즘으로 노드의 깊이와 바로 위 부모노드를 구해야한다.
    int[] depth = new int[nodeNum+1];

    // k 구하기
    int temp = 1;
    int kmax = 0;
    while (temp <= nodeNum){
      temp <<=1;
      kmax++;
    }
    int[][] parent = new int[nodeNum+1][kmax+1];
    for(int i=1; i<=nodeNum; i++){
      depth[i] = -1;
    }

    // bfs
    Queue<Node> queue = new ArrayDeque<>();
    queue.add(new Node(1,0)); // 루트는 1번이라고 주어짐
    depth[1] = 0;
    while(!queue.isEmpty()){
      Node node = queue.poll();
      for(int adj: tree[node.vertex]){
        if (depth[adj] == -1) { // 방문하지 않은 노드에 대해 방뭄ㄴ
          queue.add(new Node(adj, node.depth+1));
          depth[adj] = node.depth+1; // 깊이 기록
          parent[adj][0] = node.vertex; // 바로 위 부모 기록
        }
      }
    }

    /**
     * [Node처럼 클래스 선언 안하고 하는 방법]
     * 초기값
     * now_size = 1;
     *
     * count로 측정하다가 now_size와 같아지면
     * count = 0하고
     * now_size = 큐의 사이즈
     * level 증가 시키기
     */

    // 3. 점화식으로 parent 채우기 (?)
    for(int k=1; k<kmax; k++){
      for(int n=1; n<=nodeNum; n++){
        parent[n][k] = parent[parent[n][k-1]][k-1];
      }
    }

    // 가장 가까운 공통 조상을 알고싶은 쌍의 개수
    int questionNum = Integer.parseInt(br.readLine());
    for(int i=0; i<questionNum; i++){
      st= new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());

      // LCA 구하는 로직 수행
      int lca = executeLCA(parent, depth, kmax, nodeA, nodeB);
      System.out.println(lca);
    }

  }

  private static int executeLCA(int[][] parent, int[] depth, int kmax, int nodeA, int nodeB) {
    // 무조건 nodeB의 깊이가 클 수 있도록
    if(depth[nodeA]> depth[nodeB]){
      int temp = nodeA;
      nodeA = nodeB;
      nodeB = temp;
    }

    // 깊이 맞추기
    for(int k= kmax; k>=0; k--){
      // 깊이의 차이가 2^k보다 더 크면
      if(Math.pow(2, k) <= depth[nodeB]-depth[nodeA]){
        nodeB = parent[nodeB][k]; // 2^k 만큼 뛰기
      }
    }

    // 동시에 올라가면서 조상을 찾기
    for(int k= kmax; k>=0; k--){
      // 둘이 조상이 다를때까지
      if(parent[nodeA][k] != parent[nodeB][k]){
        nodeA = parent[nodeA][k];
        nodeB = parent[nodeB][k];
      }
    }

    int LCA = nodeA;
    if(nodeA!=nodeB){ // 둘이 다르면 한칸만 더 올라가기
      LCA = parent[LCA][0];
    }

    return LCA;
  }

}
