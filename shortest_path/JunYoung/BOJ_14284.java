import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 간선 이어가기 2
 *
 * 정점 n개, 0개의 간선으로 이루어진 무방향 그래프가 주어진다.
 * m개의 가중치 간선의 정보가 있는 간선 리스트가 주어진다.
 * 간선리스트에 있는 간선을 하나씩 그래프에 추가해 나갈 것이다.
 * 이때, 특정 정점 s와 t가 연결이 되는 시점에서 간선 추가를 멈출 것이다.
 *
 * s와 t가 연결이 되는 시점의 간선의 가중치 합이 최소가 되게 한다면, 그 값은?
 *
 * [다익스트라]
 */
//public class BOJ_14284 {
//    static List<Integer[]>[] graph;
//    static boolean[] visited;
//    static int targetNode;
//    static int answer= 10000001; // 100000*100보단 클수 없다.
//
//    static void dfs(int node, int costSum){
//        visited[node] = true;
//        if(node==targetNode){
//            answer = Math.min(answer, costSum);
//        }
//
//        for(Integer[] adj: graph[node]){
//            if(!visited[adj[0]]){ // 아직 방문하지 않은 인접노드에 대해서
//                dfs(adj[0], costSum+adj[1]);
//            }
//        }
//
//        visited[node] = false;
//    }
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        int n = Integer.parseInt(st.nextToken()); // 정점의 개수(2~5000)
//        int m = Integer.parseInt(st.nextToken()); // 간선의 수(1~100,000=십만)
//
//        graph = new ArrayList[n+1];
//        for(int i=1; i<=n; i++){
//            graph[i] = new ArrayList<>();
//        }
//
//        for(int i=0; i<m; i++){
//            st = new StringTokenizer(br.readLine());
//            int a = Integer.parseInt(st.nextToken());
//            int b = Integer.parseInt(st.nextToken());
//            int c = Integer.parseInt(st.nextToken()); // 가중치 1~100
//            graph[a].add(new Integer[]{b, c});
//            graph[b].add(new Integer[]{a, c});
//        }
//
//        st = new StringTokenizer(br.readLine());
//        int s = Integer.parseInt(st.nextToken());
//        int t = Integer.parseInt(st.nextToken());
//        visited = new boolean[n+1];
//        targetNode = t;
//        dfs(s, 0);
//
//        System.out.println(answer);
//    }
//}

public class BOJ_14284 {
    static List<Integer[]>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 정점의 개수(2~5000)
        int m = Integer.parseInt(st.nextToken()); // 간선의 수(1~100,000=십만)

        graph = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken()); // 가중치 1~100
            graph[a].add(new Integer[]{b, c});
            graph[b].add(new Integer[]{a, c});
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        visited = new boolean[n+1];

        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b)->(Integer.compare(a[1],b[1])));
        pq.add(new Integer[]{s, 0});
        int[] dist = new int[n+1];
        for(int i=1; i<=n; i++){
            if(i==s) continue;
            dist[i] = 10000001;
        }

        while (!pq.isEmpty()){
            Integer[] poll = pq.poll();
            int pollNode = poll[0];
            int pollCost = poll[1];
            if(dist[pollNode] != pollCost) continue;

            for(Integer[] adj: graph[pollNode]){
                if(pollCost+adj[1]<dist[adj[0]]){
                    dist[adj[0]] =pollCost+adj[1];
                    pq.add(new Integer[]{adj[0], dist[adj[0]]});
                }
            }
        }

        System.out.println(dist[t]);
    }
}