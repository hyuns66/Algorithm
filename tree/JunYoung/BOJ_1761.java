import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 정점들의 거리
 *
 * N(2~40,000)개의 정점으로 이루어진 트리가 주어지고
 * M(1~10,000)개의 두 노드쌍을 입력받을 때, 두 노드 사이의 거리?
 * 두 점 사이의 거리는 10,000보다 작거나 같은 자연수이다.
 *
 * [LCA]
 */
public class BOJ_1761 {
    static class Node{
        int node;
        int dist;

        Node(int node, int dist){
            this.node = node;
            this.dist = dist;
        }
    }

    static int[][] parent;
    static int[][] parentDist;
    static int[] depth;

    static int LCA(int a, int b, int kMax){
        // 깊이 맞추기
        int da = depth[a];
        int db = depth[b];

        if(db<da){ // db를 더 크게 만들기
            int temp = a;
            a = b;
            b = temp;
        }

        int bDist= 0;
        for(int k=kMax; k>=0; k--){
            if(Math.pow(2, k) <= depth[b]-depth[a]){
                bDist += parentDist[b][k];
                b = parent[b][k];
            }
        }

        // 공통 조상 찾기
        int aDist= 0;
        for(int k=kMax; k>=0; k--){
            if(parent[a][k]!=parent[b][k]){
                aDist += parentDist[a][k];
                bDist += parentDist[b][k];
                a = parent[a][k];
                b = parent[b][k];
            }
        }

        int LCA = a;
        if(a!=b){ // 둘이 다르면 한칸만 더 올라가기
            aDist+=parentDist[a][0];
            bDist+=parentDist[b][0];
            LCA = parent[LCA][0];
        }

        //System.out.println(aDist+", "+ bDist);
        return aDist+bDist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        // 연결리스트
        List<Node>[] graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        // 간선 입력 받기
        for(int i=0; i<N-1; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b,dist));
            graph[b].add(new Node(a, dist));
        }

        // parent 배열 만들기
        int temp = 1;
        int kMax = -1;
        while(temp<=N){
            temp<<=1;
            kMax++;
        }

        parent = new int[N+1][kMax+1]; // N노드의 부모
        parentDist = new int[N+1][kMax+1]; // N노드의 부모까지의 거리
        depth = new int[N+1]; // N노드의 깊이

        boolean[] visited = new boolean[N+1];
        Queue<Integer[]> queue = new ArrayDeque<>();
        queue.add(new Integer[]{1,0});
        visited[1] = true;
        while (!queue.isEmpty()){
            Integer[] node = queue.poll();
            int currentNode = node[0];
            int currentDepth = node[1];
            for(Node adj: graph[currentNode]){
                if(!visited[adj.node]){
                    visited[adj.node] = true;
                    parent[adj.node][0] = currentNode; // 바로 위 부모 기록
                    parentDist[adj.node][0] = adj.dist; // 바로 위 부모까지의 거리 기록
                    depth[adj.node] = currentDepth+1;
                    queue.add(new Integer[]{adj.node, currentDepth+1});
                }
            }
        }

        // parent, parentDist 채우기
        for(int k=1; k<=kMax; k++){
            for(int n=1; n<=N; n++){
                parent[n][k] = parent[parent[n][k-1]][k-1];
                parentDist[n][k] = parentDist[n][k-1] + parentDist[parent[n][k-1]][k-1];
                //System.out.println(n+"의"+Math.pow(2,k-1)+"번째 부모까지의 거리 = "+ parentDist[n][k-1]);
                //System.out.println(parent[n][k-1]+"의"+Math.pow(2,k-1)+"번째 부모까지의 거리 = "+ parentDist[parent[n][k-1]][k-1]);

            }
        }

//        for(int k=0; k<=kMax; k++){
//            for(int n=1; n<=N; n++){
//                System.out.print(parentDist[n][k]+" ");
//            }
//            System.out.println();
//        }


        // 쿼리 개수
        int M = Integer.parseInt(br.readLine());
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(LCA(a, b, kMax));
        }
    }
}
