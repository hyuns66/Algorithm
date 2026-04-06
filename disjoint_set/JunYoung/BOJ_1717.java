import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 유니온 파인드
 */
public class BOJ_1717 {
    static int[] parent;

    static void union(int a, int b){
        int parentA = find(a);
        int parentB = find(b);

        if(parentA==parentB) return; // 부모가 같으면 조기 종료

        // 최적화1: union by rank
        if(parent[parentB]<parent[parentA]){
            int parentTmp = parentB;
            parentB = parentA;
            parentA = parentTmp;
        }

        if(parent[parentA]==parent[parentB]) {
            parent[parentA]--;
        }
        parent[parentB] = parentA;
    }

    static int find(int a){
        if(parent[a] < 0)
            return a;
        return parent[a] = find(parent[a]); // 최적화2: 내 "부모의 부모"를 부모로
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 1000000(백만)
        int m = Integer.parseInt(st.nextToken()); // 100000(십만)

        parent = new int[n+1];
        for(int i=0; i<=n; i++){
            parent[i] = -1;
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(command==0){
                union(a,b);
            }else{
                int parentA = find(a);
                int parentB = find(b);

                if(parentA==parentB) System.out.println("YES");
                else System.out.println("NO");
            }
        }
    }
}
