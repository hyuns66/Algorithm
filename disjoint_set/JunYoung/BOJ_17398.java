import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 통신망 분할
 *
 * 통신망을 분할할때 발생하는 비용을 분석하고자한다.
 * 1~N번까지의 총 N개의 통신탑이 존재
 * 통신탑 간의 연결이 M개 존재.
 *
 * 총 Q번 통신탑 간의 연결을 제거함으로써 하나의 통신망을 여러개의 통신망으로 분리하고자한다.
 * 제거비용 = 나눠지지 않으면 0원
 * 나눠진다면, 두개의 통신망에 속한 통신탑들의 갯수의 곱
 *
 * Q번의 제거를 통해 나오는 비용의 합은??
 *
 * ================================
 * [역으로 union-find]
 * 끊는 것의 반대는 잇는 것!
 */
public class BOJ_17398 {
    static int[] parents;
    static int[] childs;

    static int union(int a, int b){
        int pa = find(a);
        int pb = find(b);

        if(pa==pb) return 0;

        int temp = childs[pa]*childs[pb];
//        System.out.println(a+":"+b);
//        System.out.println(pa+","+pb+","+temp);
        if(pa<pb){
            // 부모가 더 작은 숫자 = pa
            parents[pb] = pa;
            childs[pa] += childs[pb];
        }
        else{
            // 부모가 더 작은 숫자  = pb
            parents[pa] = pb;
            childs[pb] += childs[pa];
        }

        return temp;
    }

    static int find(int a){
        if(a==parents[a]) return a;
        return parents[a] = find(parents[a]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 통신탑의 개수 (1~100,000 = 십만)
        int M = Integer.parseInt(st.nextToken()); // 통신탑 사이의 연결의 개수 (1~100,000=십만)
        int Q = Integer.parseInt(st.nextToken()); // 통신망 연결 분할 횟수

        parents = new int[N+1];
        childs = new int[N+1];
        for(int i=1; i<=N; i++){
            parents[i] = i;
            childs[i] = 1;
        }

        int[][] network = new int[M][2];
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            // x와 y 통신탑 사이에 연결이 있음. (중복된 연결은 주어지지 않는다.)
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            network[i][0] = x;
            network[i][1] = y;
        }

        boolean[] isInput = new boolean[M];
        int[] input = new int[Q];
        for(int i=0; i<Q; i++){
            // 입력받는 순서대로 결합..
            int index = Integer.parseInt(br.readLine())-1;
            isInput[index] = true;
            input[i] = index;
        }

        for(int i=0; i<M; i++){
            if(isInput[i]) continue;
            int x = network[i][0];
            int y = network[i][1];
            union(x, y);
        }

        long answer = 0;
        for(int i=Q-1; i>=0; i--){
            // 입력받는 순서의 반대로 결합..
            int index = input[i];
            answer += union(network[index][0], network[index][1]);
        }

        System.out.println(answer);
    }
}
