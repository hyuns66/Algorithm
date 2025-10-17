import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * 피자 (Small)
 *
 * 갑은 피자 N판을 시켰습니다.
 * 높이가 N인 피자탑을, 높이가 1인 피자탑들로 분리시켜야합니다.
 *
 * 갑은 식탁위에 있는 피자탑들 중 하나를 고릅니다. -> 고른 피자탑을 두개의 피자탑으로 분리합니다.
 * 이때 갑은 분리된 피자탑의 높이의 곱만큼 즐거움을 느낍니다.
 *
 * 단, 높이가 1인 피자탑은 더는 분리시키지 않습니다.
 * 갑은 계속 피자탑들을 분리해나갑니다.
 * 이 놀이를 하다가 식탁위에 더 이상 분리할 수 있는 피자탑이 없어진다면,
 * 갑의 개강총회 준비 일을 끝나게 됩니다.
 *
 * 갑이 얻을 수 있는 즐거움의 총합의 최댓값은??
 */
public class BOJ_14606 {

    static Queue<Integer> queue = new ArrayDeque<Integer>();

    public static int calculateJoy(int num){
        int half = num/2;
        int others = num-half;

        if(half!=1) {
            queue.add(half);
        }
        if(others!=1){
            queue.add(others);
        }

        int joy = half*others;
        return joy;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        if(N!=1){
            queue.add(N);
        }

        int answer = 0;
        while(!queue.isEmpty()){
            int poll = queue.poll();
            int j =  calculateJoy(poll);
            //System.out.println(j);
            answer += j;
        }

        System.out.println(answer);
    }
}
