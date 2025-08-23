import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 트리의 지름
 * 지름 = 트리의 임의의 두 점 중 거리가 가장 긴것
 *
 * ------------------------------------------
 * 1. 아무노드 X에서 시작해 가장 먼 노드 Y를 찾는다.
 * 2. 노드 Y에서 가장 먼 노드 Z를 찾는다.
 */
public class BOJ_1167 {

  static class Node{
    int vertex;
    int weight;

    Node(int vertex, int weight){
      this.vertex = vertex;
      this.weight = weight;
    }

    @Override
    public String toString() {
      return this.vertex+":"+this.weight;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int nodeNum = Integer.parseInt(br.readLine()); // 2~100,000(십만)

    List<Node>[] graph = new ArrayList[nodeNum+1];
    for(int i=1; i<=nodeNum; i++) {
      graph[i] = new ArrayList<>();
    }

    for(int i=1; i<=nodeNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int cNode = Integer.parseInt(st.nextToken());
      while (true){
        int node = Integer.parseInt(st.nextToken());
        if(node==-1) break;
        int weight = Integer.parseInt(st.nextToken()); // 1~10,000
        graph[cNode].add(new Node(node, weight));
      }
    }

    // 트리의 지름구하기
    Node farNode = bfs(nodeNum, graph, 1);
    //System.out.println(farNode);
    Node answer = bfs(nodeNum, graph, farNode.vertex);
    //System.out.println(answer);
    System.out.println(answer.weight);
  }

  private static Node bfs(int nodeNum, List<Node>[] graph, int start) {
    boolean[] visited = new boolean[nodeNum +1];
    Queue<Node> queue = new ArrayDeque<>();
    queue.add(new Node(start, 0));
    visited[start] = true; // !! 큐에 넣을 때 visited 해주는거 잊지 말기~

    Node farNode = null;
    while (!queue.isEmpty()){
      Node now = queue.poll();
      boolean isLeaf = true;
      for(Node adj: graph[now.vertex]){
        if(visited[adj.vertex]) continue;
        isLeaf = false;
        visited[adj.vertex] = true;
        queue.add(new Node(adj.vertex, now.weight+adj.weight));
      }

      if(isLeaf){
        if(farNode==null) farNode=now;
        else{
          if(farNode.weight < now.weight){
            farNode = now;
          }
        }
      }
    }
    return farNode;
  }
}
