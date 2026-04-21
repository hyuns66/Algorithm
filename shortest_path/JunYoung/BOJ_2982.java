import java.io.*;
import java.util.*;
/**
 * 국왕의 방문
 * 고돌라가 한국에 도착했다.
 * 고돌라는 매우 중요한 사람이다.
 * 따라서 경찰은 그가 타고 있는 차량이 길에 진입했을 때, 다른 차량이 들어올 수 없게 통제할 것이다.
 * 하지만, 그가 진입하기 전부터 길에 있던 차량은 계속 있을 수 없다.
 * 상근이는 피자 배달자이다.
 * 상근이는 고둘라가 한국에 왔었을 때 어떤 길로 이동을 했어야 배달을 가장 빠르게 할 수 있었는지 알아보려고 한다.
 *
 * 상근이가 배달을 하는 데 걸리는 최솟값을 구하시오
 * 상근이는 고둘라가 출발하고 K분이 지난 후에 배달을 시작한다.
 *
 * ----------------------------------------------------
 * [다익스트라 + 시간까지..]
 * 그냥 다익스트라 그대로 쓰고,
 * 막혀있는 경우에만 단순히 이웃 Edge의 cost를 더하는게 아니라,
 * 기다리는 시간 + cost해서 가는걸 고려
 */
public class BOJ_2982 {

    static class Edge {
        int to, cost;
        Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    static int N, M;
    static List<Edge>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());

        int[] route = new int[G];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < G; i++) {
            route[i] = Integer.parseInt(st.nextToken());
        }

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();

        // 간선 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[u].add(new Edge(v, cost));
            graph[v].add(new Edge(u, cost));
        }

        // 🔥 1. 고돌라의 이동 시간 기록
        // key: "u v", value: {start, end}
        Map<String, int[]> block = new HashMap<>();

        int time = 0;
        for (int i = 0; i < G - 1; i++) {
            int u = route[i];
            int v = route[i + 1];

            int cost = getCost(u, v);

            block.put(u + " " + v, new int[]{time, time + cost});
            block.put(v + " " + u, new int[]{time, time + cost});

            time += cost;
        }

        // 🔥 2. 다익스트라
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

        // 시작 시간 = K
        dist[A] = K;
        pq.add(new int[]{A, K});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int now = cur[0];
            int nowTime = cur[1];

            if (dist[now] < nowTime) continue;

            for (Edge next : graph[now]) {
                int nextNode = next.to;
                int cost = next.cost;

                int nextTime = nowTime;

                String key = now + " " + nextNode;

                // 🔥 막힌 간선이면 기다림
                if (block.containsKey(key)) {
                    int[] t = block.get(key);
                    int start = t[0];
                    int end = t[1];

                    if (nextTime >= start && nextTime < end) {
                        nextTime = end; // 기다림
                    }
                }

                nextTime += cost;

                if (dist[nextNode] > nextTime) {
                    dist[nextNode] = nextTime;
                    pq.add(new int[]{nextNode, nextTime});
                }
            }
        }

        // 🔥 실제 걸린 시간 출력
        System.out.println(dist[B] - K);
    }

    // u -> v 간선 비용 찾기
    static int getCost(int u, int v) {
        for (Edge e : graph[u]) {
            if (e.to == v) return e.cost;
        }
        return 0;
    }
}