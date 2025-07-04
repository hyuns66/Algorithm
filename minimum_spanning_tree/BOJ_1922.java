import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 네트워크 연결
 *
 * 도현이는 컴퓨터를 연결하려고한다.
 * 이왕이면 컴퓨터를 연결하는 비용을 최소로 하고 싶다.
 * 각 컴퓨터를 연결하는 데 필요한 비용이 주어졌을 때, 모든 컴퓨터를 연결하는데 필요한 최소비용은?
 * (모든 컴퓨터를 연결할 수 없는 경우는 없다.)
 *
 * ---------------
 * MST
 * 1. 크루스칼(간선) 
 * 2. 프림(노드) -> 이 문제의 경우 간선수보다 노드수가 적기에 이 방법을 택하여 풀이함!
 *
 */
public class BOJ_1922 {

  static class Edge implements Comparable<Edge>{
    int vertex;
    int weight;

    public Edge(int vertex, int weight){
      this.vertex = vertex;
      this.weight = weight;
    }

    public int compareTo(Edge o){
      return Integer.compare(this.weight, o.weight);
    }

  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int computerNum = Integer.parseInt(br.readLine()); // 1~1000
    int edgeNum = Integer.parseInt(br.readLine()); // 1~100,000(십만)

    // 인접리스트
    List<Edge>[] adjList = new ArrayList[computerNum+1];
    for(int i=0; i<computerNum+1; i++){
      adjList[i] = new ArrayList<>();
    }

    for(int i=0; i<edgeNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine().trim());
      // a와 b가 같을수도 있다.
      int aCom = Integer.parseInt(st.nextToken());
      int bCom = Integer.parseInt(st.nextToken());
      int cost = Integer.parseInt(st.nextToken()); // 1~10,000(만)

      // 인접리스트 생성
      adjList[aCom].add(new Edge(bCom, cost));
      adjList[bCom].add(new Edge(aCom, cost));
    }

    // 모든 컴퓨터를 연결하는데 필요한 최소비용은?
    // 프림 알고리즘
    boolean[] visited = new boolean[computerNum+1]; // 노드의 방문여부
    PriorityQueue<Edge> pq = new PriorityQueue<>();
    pq.offer(new Edge(1,0));

    int answer = 0;
    while (!pq.isEmpty()){
      Edge edge = pq.poll();
      int adjVertex = edge.vertex;
      int weight = edge.weight;

      if(visited[adjVertex]) continue;

      // MST에 추가
      visited[adjVertex] = true;
      answer += weight;

      for(Edge e : adjList[adjVertex]) {
        if (!visited[e.vertex]) {
          pq.add(e);
        }
      }
    }

    System.out.println(answer);

  }

}
