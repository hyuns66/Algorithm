import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 플로이드 2
 *
 * n(1~100)개의 도시가 있다.
 * 그리고 한 도시에서 출발하여, 다른 도시에 도착하는 m(1~100,000=십만)개의 버스가 있다.
 * 각 버스는 한 번 사용할 때 필요한 비용이 있다.
 *
 * 모든 도시의 쌍에 대해 도시 A에서 도시 B로 가는 데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오
 *
 * 출력
 * = n개의 줄에 걸쳐서 dist 배열 출력
 * = n*n 줄에 걸쳐서 i*n+j번째 줄에는 도시 i에서 j로 가는 최소 비용에 포함되어있는 도시의 개수와, 가는 경로 출력 (없으면 0)
 *
 * ----------------------------------------------------------------------------------------------------------
 * [플로이드 워셜, 경로 복원]
 * - 경로 추적까지 들어가면 어렵다.
 * - dist[i][k]+ dist[k][j] 할때 오버플로우 조심하기!!
 * - dist값이 0인거랑 INF인거 둘다 고려하기
 *
 */
public class BOJ_11780 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cityNum = Integer.parseInt(br.readLine()); // 도시의 개수
        int busNum = Integer.parseInt(br.readLine()); // 버스의 개수


        // 최단 경로 배열
        long maxCost = 10000000001L; //100억(십만*십만=간선수*간선의 최대비용)+1
        long[][] dist = new long[cityNum+1][cityNum+1];
        for(int i=1; i<=cityNum; i++){
            for(int j=1; j<=cityNum; j++){
                if(i==j) continue;
                dist[i][j] = maxCost;
            }
        }


        // 경로 복원용
        int[][] next = new int[cityNum+1][cityNum+1];

        StringTokenizer st;
        for(int i=0; i<busNum; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()); // 시작도시와 도착도시가 같은 경우는 없다.
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken()); // 비용은 1~100,000

            if (cost < dist[a][b]) {
                dist[a][b] = cost;
                next[a][b] = b; // 바로 가는 경우
            }
        }

        // 플로이드 워셜
        for(int k=1; k<=cityNum; k++){
            for(int i=1; i<=cityNum; i++){
                for(int j=1; j<=cityNum; j++){
                    if (dist[i][k] == maxCost || dist[k][j] == maxCost) continue; // 오버플로우방지

                    if(dist[i][k]+dist[k][j]<dist[i][j]){ // 거쳐가는게 그냥 가는 것보다 작으면
                        dist[i][j] = dist[i][k]+dist[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        for(int i=1; i<=cityNum; i++){
            for(int j=1; j<=cityNum; j++){
                if (dist[i][j] == maxCost) sb.append("0 ");
                else sb.append(dist[i][j]).append(" ");
            }
            sb.append("\n");
        }

        // 최단 경로 도시의 개수, 경로 출력
        for(int i=1; i<=cityNum; i++){
            for(int j=1; j<=cityNum; j++){
                if(dist[i][j]==0 || dist[i][j] == maxCost) sb.append("0\n");
                else{ // 갈 수 있는 길이 있는 경우에는
                    List<Integer> path = new ArrayList<>();

                    int cur = i;
                    while (cur != j) {
                        path.add(cur);
                        cur = next[cur][j];
                    }
                    path.add(j);

                    sb.append(path.size()).append(" ");
                    for (int city : path) {
                        sb.append(city).append(" ");
                    }
                    sb.append("\n");
                }

            }
        }

        System.out.println(sb);

    }
}
