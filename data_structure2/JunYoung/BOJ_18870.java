import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 좌표 압축
 * X1,X2,...,XN
 * => 정렬, 좌표압축
 */
public class BOJ_18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 1~1,000,000(백만)

        int[] arr = new int[N]; // -10^9~10^9(1,000,000,000=10억)
        int[] sortedArr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            sortedArr[i] = arr[i];
        }
        Arrays.sort(sortedArr);
        //System.out.println(Arrays.toString(sortedArr));

        // 좌표 압축
        int index = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<N; i++){
            if(!map.containsKey(sortedArr[i])){
                map.put(sortedArr[i], index++);
            }
        }

        // 정답출력
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<N; i++){
            sb.append(map.get(arr[i])).append(" ");
        }
        System.out.println(sb);

    }
}
