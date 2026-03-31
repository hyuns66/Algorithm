import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 별자리 만들기
 *
 * n개의 별들을 이어서, 별자리를 하나 만들것이다.
 * - 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져있어야한다.
 * 선을 하나 이을 때마다 두 별 사이의 거리만큼 비용이 든다.
 * => 별자리를 만드는 최소 비용??
 *
 * [MST, 가장 최소 비용으로 트리를 구성하기]
 * 연결성 (Connected): 고립된 노드 없이 모든 노드 사이에 경로가 존재해야 합니다.
 * 비순환성 (Acyclic): 어느 노드에서 출발해도 자기 자신으로 돌아오는 경로(사이클)가 없어야 합니다.
 * 간선의 개수: 노드의 개수가 N개일 때, 간선의 개수는 반드시 N-1개여야 합니다.
 *
 *  [아래 풀이는 프림을 사용해서 MST를 구성함. 우선순위 큐 사용]
 */
public class BOJ_4386 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 별의 개수 = n (1~100)

        StringTokenizer st;
        float[][] pos = new float[n+1][2];
        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            float x = Float.parseFloat(st.nextToken()); // 0~1000 (최대 소수점 둘째자리)
            float y = Float.parseFloat(st.nextToken());
            pos[i][0] = x;
            pos[i][1] = y;
        }

        // 프림을 이용한 MST
        boolean[] visited = new boolean[n+1];
        PriorityQueue<Double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(a[1], b[1]));
        pq.add(new Double[]{1d, 0d});

        double answer = 0d;
        int count = 0;
        while (count<n){
            Double[] poll = pq.poll();
            int node = poll[0].intValue();
            double dist =poll[1];

            // 방문하지 않은 노드면, 방문하기
            if(!visited[node]) {
                visited[node] = true;
                answer += dist;
                count++;
            }

            // 인접 노드들에 대해서
            for(int i=1; i<=n; i++){
                if(!visited[i]) { // 방문하지 않은 노드 넣기
                    float x1 = pos[node][0];
                    float x2 = pos[i][0];
                    float y1 = pos[node][1];
                    float y2 = pos[i][1];
                    double xSquare = Math.pow((x1-x2), 2);
                    double ySquare = Math.pow((y1-y2), 2);
                    double adjDist = Math.sqrt(xSquare+ySquare);

                    pq.add(new Double[]{(double)i,adjDist});
                }
            }
        }

        System.out.println(Math.round(answer * 100.0)/ 100.0);
    }
}
