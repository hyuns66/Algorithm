import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

/**
 * 소셜 네트워킝 어플리케이션
 *
 * 두 사람 사이에 경로가 존재하는지 안하는지를 구해보자
 */
public class BOJ_7511 {
    static int[] parent;

    static int find(int node){
        if(parent[node]<0)
            return node;
        return parent[node] = find(parent[node]);
    }

    static boolean isSameParent(int a, int b){
        a = find(a);
        b = find(b);

        return a==b;
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);

        if(a==b) return;

        if(b<a){
            int temp = b;
            b = a;
            a = temp;
        }

        if(parent[a]==parent[b]){
            parent[a]--;
        }
        parent[b] = a; // b를 a의 자식으로 넣기
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testNum = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for(int tc=1; tc<=testNum; tc++){
            sb.append("Scenario ").append(tc).append(":\n");
            int userNum = Integer.parseInt(br.readLine()); // 1~10^6
            int relationNum = Integer.parseInt(br.readLine()); // 1~10^5

            parent = new int[userNum];
            for(int i=0; i<userNum; i++){
                parent[i] = -1;
            }

            for(int i=0; i<relationNum; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                union(a, b);
            }

            int queryNum = Integer.parseInt(br.readLine());
            for(int i=0; i<queryNum; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if(isSameParent(a,b)){
                    sb.append(1).append("\n");
                }else{
                    sb.append(0).append("\n");
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
