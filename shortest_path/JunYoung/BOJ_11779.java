import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 최소비용 구하기 2
 *
 * n개의 도시가 있다 (1~1000)
 * 한도시에서 다른도시에 도착하는 m개의 버스(1~100,000)
 *
 * A도시에서 B번째 도시까지 가는데 드는 최소비용과 경로를 출력하라.
 * 버스 비용은 0~100,000(십만)
 *
 */
public class BOJ_11779 {

  static class Node implements Comparable<Node>{
    int vertex;
    int weight;

    Node(int vertex, int weight){
      this.vertex = vertex;
      this.weight = weight;
    }

    public int compareTo(Node o){
      // 오름차순 정렬
      return Integer.compare(this.weight, o.weight);
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int cityNum = Integer.parseInt(br.readLine());
    int busNum = Integer.parseInt(br.readLine());

    // 인접리스트
    List<Node>[] graph = new ArrayList[cityNum+1];
    for(int i=1; i<=cityNum; i++){
      graph[i] = new ArrayList<>();
    }

    for(int i=0; i<busNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      graph[start].add(new Node(end, weight));
    }

    // 우리가 구하고자하는 출발점과 도착점의 도시번호
    StringTokenizer st = new StringTokenizer(br.readLine());
    int start = Integer.parseInt(st.nextToken());
    int end = Integer.parseInt(st.nextToken());

    //// 다익스트라
    // 방문 배열
    boolean[] visited = new boolean[cityNum+1];
    // 최소 비용 배열
    int[] dist = new int[cityNum+1];
    int INF = 100000001; // 간선 최대비용 * 노드수 + 1;
    for(int i=1; i<=cityNum; i++){
      dist[i] = INF;
    }

    // 경로 배열
    int[] pre = new int[cityNum+1];

    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.add(new Node(start, 0));
    dist[start] = 0; // dist 배열 start 초기화 잊지 말기~ (이거 안하면 안돼!!!!!)

    while(!pq.isEmpty()){
      Node current = pq.poll();
      if(visited[current.vertex]) continue;

      visited[current.vertex] = true;
      for(Node adj : graph[current.vertex]){
        if (dist[adj.vertex]> dist[current.vertex]+ adj.weight){
          dist[adj.vertex] = dist[current.vertex]+ adj.weight;
          pq.add(new Node(adj.vertex, dist[adj.vertex]));

          // 경로 표시 (현재 노드가 다음 노드의 이전노드!)
          pre[adj.vertex] = current.vertex;
        }
      }
    }

    // 경로 복원
    List<Integer> path = new ArrayList<>();
    int cur = end;
    while(cur!=start){
      path.add(cur);
      cur = pre[cur];
    }
    path.add(cur);
    Collections.reverse(path);

    // 출발 도시에서 도착도시까지 가는데 드는 최소비용
    System.out.println(dist[end]);

    // 최소비용 경로에 포함되어있는 도시의 개수 (출발, 도착 도시 포함)
    System.out.println(path.size());

    // 최소비용 경로에 있는 도시를 순서대로 출력 (경로가 여러개면 아무거나 하나 출력)
    for(int p: path){
      System.out.print(p+" ");
    }




  }
}
