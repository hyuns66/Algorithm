import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

/**
 * 회전하는 큐
 *
 * N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
 *
 * [3가지 연산]
 * 1. 첫번째 원소를 뽑아낸다
 * 2. 왼쪽으로 한칸 이동
 * 3. 오른쪽으로 한칸 이동
 *
 * 지민이가 뽑아내려고하는 원소 위치가 주어질 때,
 * 해당 원소를 뽑아내는데 드는 2번 3번 연산의 최솟값은?
 */
public class BOJ_1021 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken()); // 50보다 작은 자연수
        int pickNum = Integer.parseInt(st.nextToken()); // 지민이가 뽑아내려고 하는 수

        // 회전하는 큐 선언
        ArrayDeque<Integer> dequeue = new ArrayDeque<>();
        for(int i=1; i<=num; i++){
            dequeue.addLast(i);
        }


        int answer = 0;
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<pickNum; i++){
            int jiminPick = Integer.parseInt(st.nextToken());

            int queueSize = dequeue.size();
            int movement = -1;
            while (true){
                movement++;
                Integer peek = dequeue.pollFirst();
                //System.out.println("dequeue에서" + peek+"뽑음");
                if(peek==jiminPick) break;
                //System.out.println("jiminPick=" + jiminPick);
                dequeue.addLast(peek);
            }

            movement = Math.min(movement, queueSize-movement);
            //System.out.println(movement);
            answer += movement;
        }

        System.out.println(answer);
    }
}
