import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 서강 그라운드
 *
 * 각 지역에 아이템들이 몇 개 있는지 알려주는 프로그램 개발함
 * 어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있을까?
 *
 * 각 지역은 일정한 길이 l(1~15)의 길로 다른 지역과 연결되어있고
 * 이 길은 양방향 통행이 가능하다.
 * 예은이는 수색범위 m(1~15)이내의 모든 지역의 아이템을 습득가능하다.
 * 예은이가 얻을 수 있는 아이템의 최대 개수?
 *
 * [플로이드 워셜 = O(N^3)]
 * [다익스트라 N번 = O(V * E log V)]
 * [사실 다익스트라*N이 더 시간복잡도 적네! - 나는 플로이드워셜로 품!]
 */
public class BOJ_14938 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 지역의 개수 (1~100)
        int m = Integer.parseInt(st.nextToken()); // 수색범위 (1~15)
        int r = Integer.parseInt(st.nextToken()); // 길의 개수 (1~100)

        int[] items = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=n; i++){
            items[i] = Integer.parseInt(st.nextToken()); // 해당 지역 아이템의 수 (1~30)
        }

        int[][] dist = new int[n+1][n+1];
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if (i==j) continue;
                dist[i][j] = 1501; // max 밸류
            }
        }

        for(int i=0; i<r; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            dist[a][b] = l;
            dist[b][a] = l;
        }

        // 플로이드워셜 시간 복잡도(1,000,000=백만)
        for(int middle=1; middle<=n; middle++){
            for(int start=1; start<=n; start++){
                for(int end=1; end<=n; end++){
                    dist[start][end] = Math.min(dist[start][end], dist[start][middle]+dist[middle][end]);
                }
            }
        }

        //
        int answer = 0;
        for(int drop=1; drop<=n; drop++){
            int itemSum = 0;
            for(int dest=1; dest<=n; dest++){
                if(dist[drop][dest]<=m) itemSum+=items[dest];
            }
            answer = Math.max(answer, itemSum);
        }

        System.out.println(answer);
    }
}
