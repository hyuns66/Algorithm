import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 도로검문
 *
 * 어떤 범죄용의자가 도시를 가장 빠른 시간 내에 빠져나가려한다.
 * 경찰은 어떤 하나의 도로 위에서 검문을 한다.
 *
 * 이 문제는 도로 검문을 통해 얻을 수 있는 탈출의 최대 지연시간을 계산하는 것이다.
 * 용의자가 진입하는 지점은 항상 1번이고, 도시를 빠져나가기 위해서 최종적으로 도달해야하는 지점은 N번 지점이다.
 *
 * 입력도시의 도로망에 따라 경찰이 어떤 도로를 막으면, 용의자는 탈출을 못할 수도 있는데 이 경우 지연시킬 수 있는 탈출시간은 무한대이다.
 * -> 이 경우 -1을 출력해야한다.
 *
 * 입력 데이터에 표시된 도로망을 읽고, 경찰이 한 도로를 막고 검문함으로써 지연시킬 수 있는 최대 시간을 정수로 출력해야한다.
 * 지연효과가 없으면 0을 출력해야하고, 도시를 빠져나가지 못하게 할 수 있으면 -1을 출력해야한다.
 *
 * ============================================================================
 * 다익스트라 ElogE
 * 경찰 검문 = E
 * (25,000,000 = 2천5백만) * log5000
 *
 * 다익스트라
 * - 최단 경로 탐색
 * - 최단 경로에 있는 E하나씩 끊으면서 최대 지연 시간 찾기
 * ============================================================================
 * [그래프이론, 최단경로, 다익스트라, 역추적]
 */
public class BOJ_2307 {
    static int nodeNum;
    static List<Integer[]>[] graph;
    static int[] prev;
    static int maxDist = 50000000;

    static int dijkstra(int banA, int banB){
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[1], b[1]));
        pq.add(new Integer[]{1, 0});

        int[] dist = new int[nodeNum+1];
        Arrays.fill(dist, maxDist);
        dist[1] = 0;

        prev = new int[nodeNum+1];

        while (!pq.isEmpty()){
            Integer[] poll = pq.poll();

            if(dist[poll[0]]==poll[1]){
                for(Integer[] adj: graph[poll[0]]){
                    // 단속하는 길이면 지나지 않기
                    if((banA==poll[0] && banB==adj[0]) || (banB==poll[0] && banA==adj[0])) continue;

                    if(dist[adj[0]]>poll[1]+adj[1]){
                        dist[adj[0]] = poll[1]+adj[1];
                        pq.add(new Integer[]{adj[0], dist[adj[0]]});
                        prev[adj[0]] = poll[0];
                    }
                }
            }
        }

        int originTime = dist[nodeNum];
        return originTime;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        nodeNum = Integer.parseInt(st.nextToken()); // 지점의 수 (6~1000)
        int edgeNum = Integer.parseInt(st.nextToken()); // 도로의 수 (6~5000)

        // 인접리스트
        graph = new ArrayList[nodeNum+1];
        for(int i=1; i<=nodeNum; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<edgeNum; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken()); // a<b
            int t = Integer.parseInt(st.nextToken()); // 1~10000
            graph[a].add(new Integer[]{b, t});
            graph[b].add(new Integer[]{a, t});
        }

        // 다익스트라
        int originTime = dijkstra(0,0);

        // 최단 경로 탐색
        List<Integer> route = new ArrayList<>();
        int index = nodeNum;
        while (true){
            route.add(index);
            index= prev[index];
            if(index==0) break;
        }
        Collections.reverse(route);

        // 최단 경로 밴하면서 다익스트라
        int maxTime = 0;
        for(int i=0; i<route.size()-1; i++){
            int a = route.get(i);
            int b = route.get(i+1);
            int banTime = dijkstra(a, b);

            if(banTime==maxDist) maxTime = maxDist;
            else maxTime = Math.max(maxTime, banTime-originTime);
        }

        System.out.println(maxTime==maxDist? -1: maxTime);
    }
}
