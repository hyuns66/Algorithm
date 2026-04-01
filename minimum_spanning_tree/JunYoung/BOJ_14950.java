import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 정복자
 *
 * N개의 도시, M개의 도로
 * 모든 도시쌍에는 도시를 연결하는 도로로 구성된 경로가 존재
 *
 * 처음 점검하고 있는 도시는 1번 도시
 * 정복과정에서 드는 비용 = 도로를 연결하는 비용
 * 하나의 도시가 정복되면, 모든 도로의 비용은 t만큼 증가한다.
 *
 * =========================
 * [MST, PRIM 알고리즘 이용]
 * int[][] distance = new int[N+1][N+1]; // 메모리 초과남 (만의제곱만큼 int배열)
 * 메모리제한은 256MB
 * 1 KB = 1024 B
 * 1 MB = 1024^2 B = 10^6과 유사
 * 1 GB = 1024^3 B  = 10^9과 유사
 */
public class BOJ_14950 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 1~10000(만)
        int M = Integer.parseInt(st.nextToken()); // 1~30000(3만)
        int t = Integer.parseInt(st.nextToken()); // 1~10



        //int[][] distance = new int[N+1][N+1]; // 메모리 초과남
        List<Integer[]>[] graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[a].add(new Integer[]{b,cost});
            graph[b].add(new Integer[]{a,cost});
        }

        // 도로의 최댓값 : 10000(1만)~ 100000 + 10*100000(11만)까지 공차10인 수열의 합
        // = 600,060,000
        long answer = 0;
        int addedValue = 0; // 최대 10만까지 가능
        boolean[] visited = new boolean[N+1];
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b)->(Integer.compare(a[1], b[1])));
        pq.add(new Integer[]{1, 0});
        while (!pq.isEmpty()){
            Integer[] pollNode = pq.poll();
            int node = pollNode[0];
            int dist = pollNode[1];

            if(!visited[node]){
                visited[node] = true;

                if(node!=1){ // 첫 순서는 아래 비용 작업 건너 뛰기
                    //System.out.println(node+":"+dist + ":" + addedValue);
                    answer += (dist + addedValue);
                    addedValue += t;
                }

                // 인접노드 pq에 추가
                for(Integer[] adj : graph[node]){
                    if(visited[adj[0]]) continue;
                    // 주변노드 중에 방문하지 않은 노드에 대해서
                    pq.add(new Integer[]{adj[0], adj[1]});
                }
            }
        }

        System.out.println(answer);
    }
}
