import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 파티
 *
 * N개의 숫자로 구분된 각 마을에 한명의 학생이 살고 있다.
 * N명의 학생이 X번 마을에 모여 파티를 벌이기로 했다.
 *
 * 총 M개의 단반향 도로들이 있고 i번째 길을 지나는데 Ti의 시간을 소비한다.
 * N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생의 "소요시간"은?
 *
 * N = 1~1000
 * M = 1~10,000
 *
 */

public class BOJ_1238 {

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
    StringTokenizer st = new StringTokenizer(br.readLine());

    int nodeNum = Integer.parseInt(st.nextToken());
    int roadNum = Integer.parseInt(st.nextToken());
    int meetingNode = Integer.parseInt(st.nextToken());

    int INF = 100001; // 100 * 1000 + 1

    // 1. 인접행렬 대신 인접 리스트로 구현
    List<Node>[] graph = new ArrayList[nodeNum+1];
    List<Node>[] reverseGraph = new ArrayList[nodeNum+1];
    for(int i=1; i<=nodeNum; i++){
      graph[i] = new ArrayList<>();
      reverseGraph[i] = new ArrayList<>();
    }
    for(int i=0; i<roadNum; i++){
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      graph[start].add(new Node(end, weight));
      reverseGraph[end].add(new Node(start, weight));
    }

    // 2. 최단 거리 배열
    int[] dist = new int[nodeNum+1];
    int[] reverseDist = new int[nodeNum+1];
    for(int i=1; i<=nodeNum; i++){
      dist[i] = INF;
      reverseDist[i] = INF;
    }

    // 3. 방문 배열
    boolean[] visited = new boolean[nodeNum+1];
    boolean[] reverseVisited = new boolean[nodeNum+1];
    dist[meetingNode] = 0;
    reverseDist[meetingNode] = 0;

    // 4. 값이 가장 작은 노드 중 방문하지 않은 노드를 골라, 최단 거리 배열 갱신하기
    PriorityQueue<Node> pq = new PriorityQueue(); // 최대힙(값을 음수화하여 최소힙으로 이용해주기)
    pq.add(new Node(meetingNode, 0));

    while(!pq.isEmpty()){
      Node current = pq.poll();
      if(visited[current.vertex]==true) continue;

      visited[current.vertex] = true;

      for(Node adjNode: graph[current.vertex]){
        // dist[다음노드] > dist[현재노드] + 현재노드에서 다음노드 가는 비용이면 갱신
        if(dist[adjNode.vertex]>dist[current.vertex]+adjNode.weight){
          dist[adjNode.vertex] =  dist[current.vertex]+adjNode.weight;
          pq.add(new Node(adjNode.vertex, dist[adjNode.vertex]));
        }
      }
    }

    PriorityQueue<Node> reversePq = new PriorityQueue(); // 최대힙(값을 음수화하여 최소힙으로 이용해주기)
    reversePq.add(new Node(meetingNode, 0));
    while(!reversePq.isEmpty()){
      Node current = reversePq.poll();
      if(reverseVisited[current.vertex]==true) continue;

      reverseVisited[current.vertex] = true;

      for(Node adjNode: reverseGraph[current.vertex]){
        // dist[다음노드] > dist[현재노드] + 현재노드에서 다음노드 가는 비용이면 갱신
        if(reverseDist[adjNode.vertex]>reverseDist[current.vertex]+adjNode.weight){
          reverseDist[adjNode.vertex] =  reverseDist[current.vertex]+adjNode.weight;
          reversePq.add(new Node(adjNode.vertex, reverseDist[adjNode.vertex]));
        }
      }
    }

    // 정답 구하기
    int maxDist = -1;
    for(int i = 1 ; i <= nodeNum ; i++) {
      dist[i] = dist[i] + reverseDist[i];
      if(dist[i]>maxDist){
        maxDist = dist[i];
      }
    }

    System.out.print(maxDist);
  }
}
