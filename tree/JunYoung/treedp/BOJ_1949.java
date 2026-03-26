import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 우수 마을
 * N개의 마을로 이루어진 트리구조의 나라
 * 마을 = 1~N의 번호가 붙여진 N개의 마을
 * 마을을 잇는 길 = N-1개
 * 인접하다 = 두 마을에 직접 잇는 길이 있을 때
 *
 * 우수마을
 * 1. 우수 마을 주민수의 총합을 최대로 해야한다.
 * 2. 우수 마을끼리는 인접해 있을 수 없다.
 * 3. 우수마을로 선정되지 못한 마을은 적어도 하나의 우수마을과 인접해있어야한다.
 *
 * '우수 마을'의 주민 수의 총 합??
 * ------------------------
 * [트리에서의 dp]
 * - 트리에서의 dp = [자식 -> 부모]로 계산 (트리는 사이클이 없어서, 자식결과 알면 부모 결정가능)
 * - dp[node][0] = 해당 노드를 선택하지 않았을 때
 * - dp[node][1] = 해당 노드를 선택했을 때 값으로 초기화
 *
 * - 인접노드들에 대해서
 * - dp[node][0] += Math.max(dp[child][0], dp[child][1]);
 * - dp[node][1] += dp[child][0];
 * ------------------------
 */
public class BOJ_1949 {

    static int answer = 0;
    static void dfs(int node,  List<Integer>[] graph, int[] people, boolean[] visited, int[][] dp){
        visited[node] = true;

        dp[node][0] = 0;
        dp[node][1] = people[node];

        // 인접노드 방문하기
        for(int adj: graph[node]) {
            if (!visited[adj]) {
                dfs(adj, graph, people, visited, dp);
                dp[node][0] += Math.max(dp[adj][0], dp[adj][1]);
                dp[node][1] += dp[adj][0];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 마을의 수 입력받기
        int N = Integer.parseInt(br.readLine()); // 1~10,000(만)

        // 마을 별 주민의 수 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] people = new int[N+1];
        for(int i=1; i<=N; i++){
            int pNum = Integer.parseInt(st.nextToken()); // 주민수는 10,000(만)이하
            people[i] = pNum;
        }

        // 인접한 마을을 입력받기
        List<Integer>[] graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<N-1; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        boolean[] visited = new boolean[N+1];
        int[][] dp = new int[N+1][2];
        dfs(1, graph, people, visited, dp);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }
}
