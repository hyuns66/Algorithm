import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 트리 수정
 *
 * 홍준이는 트리에서 간선을 하나 제거하고, 간선을 하나 추가하려고 한다.
 * 그랬을 때, 홍준이가 만들 수 있는 트리 중 가장 지름이 큰 것은?
 *
 * [트리의 지름, 브루트포스]
 */
public class BOJ_12912 {
    static List<Integer[]>[] adjs;
    static int[][] edges;
    static boolean[] visited;
    static int farNode;
    static long farDist;
    static int N;

    static void dfs(int current, long dist, int[] ignore){
        visited[current] = true;
        if(farDist<dist){
            farDist = dist;
            farNode = current;
        }

        for(Integer[] adj: adjs[current]){
            int to = adj[0];
            int cost = adj[1];

            if((to==ignore[0]&&current==ignore[1]) || (to==ignore[1]&&current==ignore[0])){
                continue;
            }

            if(!visited[to]) {
                dfs(to, dist+cost, ignore);
            }
        }
    }

    static void initialize(){
        visited = new boolean[N];
        farDist = 0;
    }

    static long diameter(int node, int[] ignoreEdge){
        farNode = node;
        initialize();
        dfs(node, 0, ignoreEdge);
        initialize();
        dfs(farNode, 0, ignoreEdge);
        return farDist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); // 트리의 정점의 개수 = 2~2000

        adjs = new ArrayList[N];
        for(int i=0; i<N; i++){
            adjs[i] = new ArrayList<>();
        }

        edges = new int[N-1][3];
        for(int i=0; i<N-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken()); // 1,000,000,000 = 10억
            edges[i][0] = from;
            edges[i][1] = to;
            edges[i][2] = cost;
            adjs[from].add(new Integer[]{to, cost});
            adjs[to].add(new Integer[]{from, cost});
        }

        long answer = 0;
        for (int i=0; i<N-1; i++){
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];

            long d1 = diameter(u, edges[i]);
            long d2 = diameter(v, edges[i]);
            //System.out.println(d1+" "+d2);

            answer = Math.max(answer, d1+d2+w);
        }

        System.out.print(answer);
    }
}
