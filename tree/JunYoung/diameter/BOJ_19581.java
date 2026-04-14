import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 두 번째 트리의 지름
 *
 * 트리에 N개의 정점이 있고, 1~N번까지 번호가 붙어있다.
 * 트리의 두번째 지름이란..
 * 두번째로 가장 먼 두 정점간의 거리를 의미한다.
 *
 * -------------------------------------------
 * [반례]
 * 6
 * 1 5 4
 * 2 5 1
 * 3 6 2
 * 1 3 1
 * 1 4 1
 * ===============
 * 정답 = 7
 *
 * 7
 * 1 2 1
 * 2 3 2
 * 1 4 3
 * 1 5 1
 * 5 6 1
 * 6 7 1
 * ===============
 * 정답 = 6
 * -------------------------------------------
 * [트리의 지름(두번쩨 지름), 아이디어 문제] - 풀이법 보고 다시 품...
 * 처음에는 지름 중 하나를 찾고, 거기서 2번째 먼 곳을 찾으면 될 줄 알았는데,
 * 다른 지름노드에서 먼곳이 답이 될 수도 있었기에,
 * 지름 2곳 각각에서 가장 먼곳의 길이를 찾는게 두번째 지름 문제다.
 */
public class BOJ_19581 {
    static List<Integer[]>[] graph;
    static boolean[] visited;
    static int N;

    static int farNode = 0;
    static int farDist = 0;
    static int secondFarDist = 0;

    static int diaMeterA;
    static int diaMeterB;



    static void dfs(int node, int dist){
        visited[node] = true;

        if(dist>=farDist) { // 최고 거리랑 같을 때도 갱신 필요
            secondFarDist = farDist;
            farDist = dist;
            farNode = node;
        } else if (dist> secondFarDist) {
            secondFarDist = dist;
        }

        for(Integer[] adj: graph[node]){
            if(!visited[adj[0]]){
                dfs(adj[0], dist+adj[1]);
            }
        }
    }

    static int getSecondDiameter(int node){
        visited = new boolean[N+1];
        dfs(node, 0);

        farDist = 0;
        secondFarDist = 0;
        visited = new boolean[N+1];
        dfs(farNode, 0);
        int answer = secondFarDist;

        //
        farDist = 0;
        secondFarDist = 0;
        visited = new boolean[N+1];
        dfs(farNode, 0);
        return Math.max(answer, secondFarDist);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); // 정점의 개수 (3~100,000=십만)

        graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for(int i=0; i<N-1; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken()); //1~20,000
            graph[a].add(new Integer[]{b, cost});
            graph[b].add(new Integer[]{a, cost});
        }

        // 2,000,000,000 (20억)
        int sd = getSecondDiameter(1);
        System.out.print(sd);

    }
}
