import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 네크워크 복구
 *
 * N개의 컴퓨터로 구성된 네트워크가 있다.
 *
 * 어느 날 해커가 네트워크에 침입하였다.
 * 관리자는 보안시스템을 한 대의 슈퍼컴퓨터에 설치한다.
 * 한 컴퓨터가 공격을 받게 되면 네트워크를 통해 슈퍼컴퓨터에 이 사실이 전달되고,
 * 슈퍼컴퓨터에서는 보안 패킷을 전송하는 방식을 사용하기로 했다.
 *
 * 네트워크 회선을 복구하려고한다.
 * 슈퍼컴퓨터가 다른 컴퓨터와 통신하는데 걸리는 시간이
 * 원래 네트워크에서 통신하는데 드는 최소시간보다 커져선 안된다.
 * 1번 컴퓨터는 보안 시스템을 설치할 슈퍼 컴퓨터이다.
 * ===============================================
 * 복구할 회선의 개수 K를 출력한다.
 * K줄에는 복구할 회선 A, B를 출력한다.
 * 출력은 임의 순서대로 한다.
 *
 * [다익스트라 경로는 무조건 트리가 된다!!]
 */
public class BOJ_2211 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Integer[]>[] graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken()); // 통신시간 C (1~10)
            graph[a].add(new Integer[]{b, c});
            graph[b].add(new Integer[]{a, c});
        }

        // 다익스트라
        int[] prev = new int[N+1];
        int[] dist = new int[N+1];
        Arrays.fill(dist, 10*M);
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[1], b[1]));
        dist[1] = 0;
        pq.add(new Integer[]{1, 0});

        while (!pq.isEmpty()){
            Integer[] poll = pq.poll();
            int pollNode = poll[0];
            int pollDist = poll[1];

            if(dist[pollNode]!=pollDist) continue;

            for(Integer[] adj: graph[pollNode]){
                int adjNode = adj[0];
                int adjDist = adj[1];
                if(dist[adjNode]> pollDist+adjDist){
                    dist[adjNode] = pollDist+adjDist;
                    pq.add(new Integer[]{adjNode, dist[adjNode]});
                    prev[adjNode] = pollNode;
                }
            }
        }

        System.out.println(N-1);
        for(int i=2; i<=N; i++){
            System.out.println(i+" "+prev[i]);
        }

    }
}
