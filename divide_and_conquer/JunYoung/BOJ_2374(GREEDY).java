import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 같은 수로 만들기
 *
 * n=1~1000개의 자연수가 있다.
 * A[1]~A[n]
 *
 * Add(i)를 하면 A[i]와, A[i]와 좌우로 맞닿아있는 같은 수가 1씩 증가한다.
 *
 * Add연산을 사용하여 A[1]~A[n]이 같도록 하려한다.
 * 이때 Add 연산의 최소 사용횟수는?
 *
 * ========================================
 * A배열에 있는 수 중에 가장 큰 수에 맞춰야한다.
 *
 * 1 5 10
 * 2 5 10
 * 3 5 10
 * 4 5 10
 * 5 5 10
 * 6 6 10
 * 7 7 10
 * 8 8 10
 * 9 9 10
 * 10 10 10
 *
 * -----------------------------------------------
 * 1차시도) 4%에서 틀렸습니다.
 * 1차수정) answer가 10^25승인데 이 값이 int 범위를 넘나 -> 성공!
 * ------------------------------------------------
 * 나는 그냥 greedy로 풀었다.
 * 가장 낮은 수의 그룹부터 그 다음 낮은 수로 맞춰주고, 바닥을 높여오는 형식으로!
 *
 * O(N^2) = 1000*1000 정도인감.. 훔.. 계산하긴 어렵네..
 */
public class BOJ_2374 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n+1];
        Set<Integer> numbers = new HashSet<>();
        for(int i=1; i<=n; i++){
            arr[i] = Integer.parseInt(br.readLine());
            numbers.add(arr[i]);
        }


        List<Integer> sortedNumbers = new ArrayList<>(numbers);
        Collections.sort(sortedNumbers);

        long answer = 0;
        for(int i=0; i<sortedNumbers.size()-1; i++){
            int value = sortedNumbers.get(i);
            int nextValue = sortedNumbers.get(i+1);

            Queue<Integer> queue = new ArrayDeque<>();
            for(int j=1; j<=n; j++){
                // 시작하는 인덱스 (value가 처음 나온 곳)
                if (arr[j-1]!=value && arr[j]==value) {
                    queue.add(j);
                }

                // 끝나는 인덱스 (앞은 value였는데, 현재는 value가 아님)
                if(arr[j]!=value &&arr[j-1]==value) queue.add(j);
            }
            if(queue.size()%2!=0) queue.add(n+1);

            // 각 구간 마다
            while (!queue.isEmpty()){
                int startIdx = queue.poll();
                int endIdx = queue.poll()-1;
                //System.out.println(startIdx+"~"+endIdx);

                for(int s=startIdx; s<=endIdx; s++){
                    arr[s] = nextValue;
                }
                answer += nextValue-value;
            }
        }

        System.out.println(answer);
    }
}
