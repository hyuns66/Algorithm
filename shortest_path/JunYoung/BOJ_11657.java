import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 타임머신
 *
 * 1번 도시에서 출발해, 어떤 도시로 가는 과정에서 시간을 무한히 오래전으로 되돌릴 수 있다면(=음수 사이클) 첫째줄에 -1을 출력
 * 그렇지 않다면, N-1개 줄에 걸쳐서 각 줄에 1번 도시에서 출발해 2,3,4,..N번 도시까지 가는 가장 빠른 순서를 출력해라.
 * 해당 동시로 가는 경로가 없다면 -1을 출력한다.
 *
 * ----------------------------------------------------------
 * [벨만 포드]
 * int로 최단거리 저장하니까 출력초과났었다.
 * "음수 사이클이 있다는 사실을 정확히 판별하기 위해" 언더플로우가 절대 발생하지 않는 long을 사용하는 것입니다.
 */
public class BOJ_11657 {
    static class Edge{
        int a;
        int b;
        int cost;

        Edge(int a, int b, int cost){
            this.a = a;
            this.b = b;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int cityNum = Integer.parseInt(st.nextToken()); // 1~500
        int busLineNum = Integer.parseInt(st.nextToken()); // 1~6000

        Edge[] edges = new Edge[busLineNum];
        for(int i=0; i<busLineNum; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()); // 1~N
            int b = Integer.parseInt(st.nextToken()); // 1~N
            int cost = Integer.parseInt(st.nextToken()); // -10000~10000
            edges[i] = new Edge(a, b, cost);
        }

        // [벨만 포드]
        // 1. 초기화
        long maxCost = Long.MAX_VALUE;
        long[] dist = new long[cityNum+1]; // 최단 거리 배열
        for(int i=1; i<=cityNum; i++){
            dist[i] = maxCost;
        }
        dist[1] = 0; // 1번 도시에서 시작

        // 2. 업데이트
        // 반복문 N번
        boolean isNCycle = false;
        for(int i=1; i<=cityNum; i++){
            for(Edge e: edges){
                if(dist[e.a] == maxCost) continue;

                if(dist[e.a] + e.cost <dist[e.b]){
                    if(i==cityNum) isNCycle = true;
                    dist[e.b] = dist[e.a] + e.cost;
                }
            }
        }

        if (isNCycle) System.out.println(-1);
        else{
            for(int i=2; i<=cityNum; i++){
                System.out.println(dist[i]==maxCost? -1:dist[i]);
            }
        }
    }
}
