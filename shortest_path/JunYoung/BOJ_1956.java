import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 운동
 *
 * V개의 마을과, E개의 도로로 구성되어 있는 도시
 * 도로는 일방통행이다.
 *
 * 운동 경로를 찾자!
 * 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.
 *
 */
public class BOJ_1956 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int vertex = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());

        // 그래프
        int max = 10000*vertex+1;
        int[][] graph = new int[vertex+1][vertex+1];
        for(int i=1; i<=vertex; i++){
            for(int j=1; j<=vertex; j++){
                graph[i][j] = max;
            }
        }

        // 도로 정보
        for(int i=0; i<edge; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph[a][b] = weight;
        }

        // 플로이드-워셜
        for(int k=1; k<=vertex; k++){
            for(int s=1; s<=vertex; s++){
                for(int e=1; e<=vertex; e++){
                    graph[s][e] = Math.min(graph[s][k]+graph[k][e], graph[s][e]);
                }
            }
        }

        //--------------------------------------------------//
        int minCycle = max;
        for(int s=1; s<=vertex; s++){
            for(int k=1; k<=vertex; k++){
                if(k==s) continue;
                int value = graph[s][k]+graph[k][s];
                if(value<minCycle) minCycle = value;
            }
        }

        // 불가능 한 경우는 -1을 출력한다.
        if(minCycle==max) minCycle = -1;

        System.out.println(minCycle);
    }
}
