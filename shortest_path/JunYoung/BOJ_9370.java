import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 미확인 도착지
 *
 * 서커스 에술가 한쌍이 한 도시의 거리들을 이동하고 있다.
 * 너의 임무는 그들이 어디로 가고 있는지 알아내는 것이다.
 *
 * 우리가 알아낸 것은 그들이 s지점에서 출발했다는 것.
 * 목적지 후보들 중 하나가 그들의 목적지라는 것이다.
 * 그들이 급한 상황이기 때문에 우회하지 않고 최단거리로 갈 것이다.
 *
 * 그들이 g와 h 교차로로 도로를 지나갔다는 것을 알아냈다.
 *
 * - 교차로 사이에는 도로가 많아봐야 1개다.
 *
 * => 테스트 케이스마다 입력에서 주어진 목적지 후보들 중 불가능한 경우를 제외한 목적지들을
 * 공백으로 분리시킨 오름차순의 정수를 출력한다.
 *
 * ------------------------------------------------------------------------
 * [다익스트라, 경로 추척]
 * - 경로 추척해서 g,h의 엣지를 안포함하면 후보지에서 빼는 식으로 풀이
 * => 같은 길이 경로인데 g->h를 안지나는 최단경로가 있을 수 있음
 *
 * 1. 가중치 조절 기법 (추천)가장 효율적이고 똑똑한 방법입니다.
 * 모든 도로의 양방향 가중치에 2를 곱해서 짝수로 만듭니다.
 * 그리고 문제에서 반드시 지나야 하는 도로(g와 h 사이)의 가중치에서만 1을 뺍니다.
 * 원리: 최단 거리를 구할 때 g-h를 지나면 결과값이 무조건 홀수가 됩니다.
 * 장점: 다익스트라 한 번으로 끝낼 수 있고, 경로 추적 로직이 필요 없습니다.
 */
public class BOJ_9370 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for(int tc=0; tc<T; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 교차로, 2~2000
            int m = Integer.parseInt(st.nextToken()); // 도로, 1~50000
            int t = Integer.parseInt(st.nextToken()); // 목적지 후보의 개수, 1~100

            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken()); // 예술가들의 출발지
            int g = Integer.parseInt(st.nextToken()); // g: 예술가가 지나간 경로
            int h = Integer.parseInt(st.nextToken()); // h: 예술가가 지나간 경로

            List<Integer[]>[] graph = new ArrayList[n+1];
            for(int i=1; i<=n; i++){
                graph[i] = new ArrayList<>();
            }

            // 도로 입력
            for(int i=0; i<m; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken()); // a(1~n, a<b)
                int b = Integer.parseInt(st.nextToken()); // b(1~n, a<b)
                int d = Integer.parseInt(st.nextToken()); // 길이 d(1~1000)

                if((a==g&&b==h) || (a==h&&b==g)){
                    graph[a].add(new Integer[]{b, 2*d-1});
                    graph[b].add(new Integer[]{a, 2*d-1});
                }else{
                    graph[a].add(new Integer[]{b, 2*d});
                    graph[b].add(new Integer[]{a, 2*d});
                }
            }

            // 최단거리 배열
            int[] dist = new int[n+1];
            int maxDist = 500000000; // 5억
            Arrays.fill(dist, maxDist);

            PriorityQueue<Integer[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[1], b[1]));

            // 출발지 설정
            dist[s] = 0;
            pq.add(new Integer[]{s, 0});

            // 다익스트라
            while (!pq.isEmpty()){
                Integer[] poll = pq.poll();
                int currentNode = poll[0];
                int currentDist = poll[1];

                if(dist[currentNode]!=currentDist) continue;

                for(Integer[] adj: graph[currentNode]){
                    int adjNode = adj[0];
                    int adjDist = adj[1];

                    if(dist[adjNode] > currentDist+adjDist){
                        dist[adjNode] = currentDist+adjDist;
                        pq.add(new Integer[]{adjNode, dist[adjNode]});
                    }
                }
            }

            // 목적지 후보 입력
            List<Integer> answer = new ArrayList<>();
            for(int i=0; i<t; i++){
                int candidate = Integer.parseInt(br.readLine());
                if(dist[candidate]%2!=0) answer.add(candidate);
            }

            Collections.sort(answer);
            for(int i=0; i<answer.size(); i++){
                sb.append(answer.get(i)+" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
