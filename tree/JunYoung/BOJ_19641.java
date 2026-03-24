import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 중첩 집합 모델
 *
 * SQL은 계층적인 구조를 표현하는데에는 한계가 있다.
 * 이러한 한계를 보완하고자 나온 모델 중 하나가 중첩 집합 모델이다.
 *
 * 각각의 데이터는 서로 겹치지 않거나, 하나의 데이터가 다른 데이터를 포함한다.
 * A.left < B.left이고 B.right < A.right이면 A는 B를 포함한다.
 *
 * ----------------------------
 * 트리 정보가 주어지고, S번 루트노드부터 번호가 낮은 자식노드 순으로 방문해서 중첩 집합을 구성했을 때
 * 각 노드의 left 필드와 right필드를 출력해라.
 *
 * =============================
 * [트리, dfs, 오일러 경로 테크닉]
 * 이 문제와 같이 각 정점을 루트로 하는 서브트리를 구간으로 표현하는 테크닉을 '오일러 투어'라고 한다.
 * 서브트리..!
 */

import java.util.*;

public class BOJ_19641 {

    static boolean[] visited;
    static int[][] leftRight;
    static int order = 1;

    // 번호가 가장 낮은 노드부터 오름차순으로 방문하기
    static void dfs(int node, List<Integer>[] adjGraph){
        leftRight[node][0] = order++;
        visited[node] = true;
        Collections.sort(adjGraph[node]); // 번호가 가장 낮은 노드부터 오름차순으로 방문하기 위함
        for(int adj: adjGraph[node]){
            if(!visited[adj]) dfs(adj, adjGraph);
        }
        leftRight[node][1] = order++;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int nodeNum = Integer.parseInt(br.readLine()); // 트리의 정점의 개수(2~100,000=십만)


        List<Integer>[] adjGraph = new ArrayList[nodeNum+1];
        for(int i=1; i<=nodeNum; i++){
            adjGraph[i] = new ArrayList<>();
        }


        for(int i=0; i<nodeNum; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 정점에 연결된 간선의 정보
            int startNode = Integer.parseInt(st.nextToken());
            while (true){
                int node = Integer.parseInt(st.nextToken());
                if(node==-1) break;
                adjGraph[startNode].add(node);
            }
        }

        int root = Integer.parseInt(br.readLine());

        visited = new boolean[nodeNum+1];
        leftRight = new int[nodeNum+1][2];
        dfs(root, adjGraph);

        StringBuilder sb = new StringBuilder();
        for(int i=1; i<=nodeNum; i++){
            sb.append(i).append(" ").append(leftRight[i][0]).append(" ").append(leftRight[i][1]);
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
