import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 숫자 카드 2
 *
 * 상근이는 숫자카드 N개를 가지고 있다.
 * 정수 M개가 주어졌을 때, 이 수의 카드를 상근이가 몇개 가지고 있을까?
 *
 * [맵으로 빈도수 카운팅하는 문제]
 */
public class BOJ_10816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 1~500,000=오십만

        StringTokenizer st = new StringTokenizer(br.readLine());

        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<N; i++){
            int cardValue = Integer.parseInt(st.nextToken());
            int cardCount = map.getOrDefault(cardValue,0);
            map.put(cardValue, cardCount+1);
        }

        int M = Integer.parseInt(br.readLine()); // 1~500,000=오십만
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++){
            int value = Integer.parseInt(st.nextToken());
            sb.append(map.getOrDefault(value, 0)+" ");
        }

        System.out.print(sb.toString());
    }
}
