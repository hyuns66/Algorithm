import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_29198 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 문자열 개수 (1~300)
        int M = Integer.parseInt(st.nextToken()); // 문자열 길이 (1~300)
        int K = Integer.parseInt(st.nextToken()); // 선택할 문자열 수 (1<=K<=N<=300)

        // 300
        // 문자열 T중 사전순으로 가장 앞에 오는 것을 출력하세요
        PriorityQueue<String> pq = new PriorityQueue<>();;
        for(int i=0; i<N; i++){
            // 문자 내 철자들 정렬
            String str = br.readLine();
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            pq.add(sorted);
        }

        PriorityQueue<Character> pqChar = new PriorityQueue<Character>();
        // O(90000) = O(9만)
        for(int i=0; i<K; i++){
            String str = pq.poll();
            for(int j=0; j<M; j++){
                pqChar.add(str.charAt(j));
            }
            //System.out.println(str);
        }

        while (!pqChar.isEmpty()){
            System.out.print(pqChar.poll());
        }
    }
}
