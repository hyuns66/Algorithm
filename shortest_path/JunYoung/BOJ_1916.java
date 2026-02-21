import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 최소비용 구하기
 *
 * N개의 도시가 있다.
 * 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
 * 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
 * A->B 도시까지 가는데 드는 최소비용은?
 */
public class BOJ_1916 {
    static class Node implements Comparable<Node>{
        int vertex;
        int weight;

        public Node(int vertex, int weight){
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o){
            return Integer.compare(this.weight, o.weight); // 오름차순
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cityNum = Integer.parseInt(br.readLine()); // 도시의 개수 = 1~1,000(천)
        int busNum = Integer.parseInt(br.readLine()); // 버스의 개수 = 1~100,000(십만)

        List<Node>[] graph = new ArrayList[cityNum+1];
        for(int i=1; i<=cityNum; i++){
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for(int i=0; i<busNum; i++){
            st = new StringTokenizer(br.readLine());
            int fromCity = Integer.parseInt(st.nextToken());
            int toCity = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken()); // 0보다 크거나 같고, 100,000보다 작은 정수이다.
            graph[fromCity].add(new Node(toCity, cost));
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        // 최단 거리 배열
        int[] dist = new int[cityNum+1];
        for(int i=1; i<=cityNum; i++){
            dist[i] = cityNum*100000; // 모든 노드를 거쳐서 가더라도 N-1개의 버스를 타게됨. 따라서 N*100000이하의 가격보다 클 수 없음.
        }
        dist[s] = 0; // 시작점은 0

        // 우선 순위 큐
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s,0));

        // 다익스트라
        while (!pq.isEmpty()){
            Node poll = pq.poll();
            if(dist[poll.vertex] != poll.weight) continue; // 과거의 정보면 새로 뽑기

            // System.out.println("현재 노드 = "+ poll.vertex);
            // 인접리스트에 대해서, 해당노드를 거쳐서 최단거리가 되면 갱신
            for(Node adj: graph[poll.vertex]){
                // System.out.println("인접 노드 = "+ adj.vertex);
                // System.out.println("현재 거리 "+ dist[adj.vertex] + ", 현재노드를 거쳐간다면 " + (dist[poll.vertex] + adj.weight));
                if(dist[adj.vertex]>dist[poll.vertex] + adj.weight){ // ist[poll.vertex] + poll.weight 하지 않도록 주의하기!!
                    dist[adj.vertex] = dist[poll.vertex] + adj.weight;
                    pq.add(new Node(adj.vertex, dist[adj.vertex]));
                }
            }
        }

        System.out.println(dist[e]);
    }
}
