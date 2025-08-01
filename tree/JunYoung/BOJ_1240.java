import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 노드 사이의 거리
 * N개의 노드로 이루어진 트리
 * M개의 노드 쌍을 입력 -> 두 노드 사이의 거리?
 *
 * ----------------------------
 *  관련 문제 : 백준 1761 풀어보자 (LCA 알고리즘 필요)
 *  https://www.acmicpc.net/problem/1761
 */
public class BOJ_1240 {

  static class Node{
    int vertex;
    int weight;

    Node (int vertex, int weight){
      this.vertex = vertex;
      this.weight = weight;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int nodeNum = Integer.parseInt(st.nextToken()); // 2~1000
    int questionNum = Integer.parseInt(st.nextToken()); // 1~1000
    // 연결된 두 점과 거리는 10,000 이하인 자연수


    // 인접 리스트 만들기
    // 인덱스 0은 사용 X
    List<Node>[] graph = new List[nodeNum+1];
    for(int i=1; i<=nodeNum; i++){
      graph[i] = new ArrayList<>();
    }

    for(int i=0; i<nodeNum-1; i++){
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());

      graph[nodeA].add(new Node(nodeB, weight));
      graph[nodeB].add(new Node(nodeA, weight));
    }

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<questionNum; i++){
      st = new StringTokenizer(br.readLine());
      int nodeA = Integer.parseInt(st.nextToken());
      int nodeB = Integer.parseInt(st.nextToken());
      sb.append(bfs(graph, nodeA, nodeB)+"\n");
    }

    System.out.print(sb);
  }

  static int bfs(List<Node>[] graph, int nodeA, int nodeB){
    Queue<Node> queue = new ArrayDeque<>();
    boolean[] visited = new boolean[graph.length];
    queue.add(new Node(nodeA, 0));
    visited[nodeA] = true;
    while (!queue.isEmpty()){
      Node current = queue.poll();
      if (current.vertex == nodeB){
        // 두노드사이의 거리를 구함!
        return current.weight;
      }

      for(Node adjNode: graph[current.vertex]){
        if(!visited[adjNode.vertex]){
          queue.add(new Node(adjNode.vertex, current.weight+adjNode.weight));
          visited[adjNode.vertex] = true;
        }
      }
    }

    return -1;
  }
}
