import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 홀수와 짝수 게임
 *
 * 1. 채완이부터 시작한다.
 * 2. 각 플레이어는 바닥에 있는 카드에서 한장 가지고 갈 수 있다.
 *    - 각 플레이어가 첫번째로 들고갈 수 있는 카드엔 제약 X
 *    - 두번째부터는 첫번째로 들고간 카드와 홀짝 여부가 동일해야한다.
 * 3. 카드를 더 이상 들고 갈수 없다면 해당 틀레이어 패배
 */
public class BOJ_33011 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for(int tc=0; tc<testCase; tc++){
            int cardNum = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int oddNum = 0;
            int evenNum = 0;
            for(int i=0; i<cardNum; i++){
                int value = Integer.parseInt(st.nextToken());
                if(value%2==0) evenNum++;
                else oddNum++;
            }

            if(oddNum==evenNum){ // 홀짝이 동일하면 후플레이어가 승
                System.out.println("heeda0528");
            }else{ // 홀짝의 수가 동일하지 않으면 선플레이어가 승
                int pickNum = Math.max(oddNum, evenNum);
                if(pickNum%2==0){
                    System.out.println("heeda0528");
                }else{
                    System.out.println("amsminn");
                }
            }
        }
    }
}
