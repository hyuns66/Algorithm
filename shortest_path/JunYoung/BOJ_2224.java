import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 명제 증명
 *
 * 수학, 논리학에서 P=>Q (P: 전건, Q: 후건)
 * 같은 명제가 여러 번 주어질 수도 있다.
 *
 * 삼단 논법
 * P => Q
 * Q => R
 * ---------
 * P => R
 *
 * 'A'의 아스키 코드 값: 65
 * 'a'의 아스키 코드 값: 97
 *
 */
public class BOJ_2224 {

    private static int atoi(char c){
        if(c>='a') return c-'a'+26;
        return c-'A';
    }

    private static char itoa(int idx){
        if(idx<26) return (char)('A'+idx);
        return (char)('a'+(idx-26));
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 1~10,000

        boolean[][] graph = new boolean[52][52];

        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            char p = st.nextToken().charAt(0);
            st.nextToken();
            char q = st.nextToken().charAt(0);
            graph[atoi(p)][atoi(q)] = true;
        }

        for(int k=0; k< 52; k++){
            for(int s=0; s< 52; s++){
                for(int e=0; e< 52; e++){
                    if(s==e||s==k||k==e||graph[s][e]) continue;
                    if(graph[s][k] && graph[k][e]) graph[s][e] = true;
                }
            }
        }

        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<52; i++){
            for(int j=0; j<52; j++){
                if(i==j||!graph[i][j]) continue;
                count++;
                sb.append(itoa(i)).append(" => ").append(itoa(j)).append('\n');
            }
        }

        System.out.println(count);
        System.out.println(sb);
    }
}
