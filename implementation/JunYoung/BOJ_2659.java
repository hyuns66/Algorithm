import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 십자카드 문제
 *
 * 십자모양의 카드: 네 모서리에 1~9이하의 숫자
 * 시계수: 카드의 숫자들을 시계방향으로 읽어서 만들어지는 수 중 가장 작은 수
 *
 * 입력으로 주어진 카드의 시계수를 계산하여,
 * 그 시계수가 모든 시계수들 중에서 몇 번째로 작은 시계수인지 알아내는 프로그램을 작성하시오.
 *
 * 1111~9999까지 1씩 증가
 * - 0을 포함하면 조기종료
 * - 4!을 하면서 시계수 찾기 -> 시계수가 이미 등록되어있으면 등록 X
 * => 시간 복잡도 O(8888x4!) = O(213312)
 *
 * [최적화 방안]
 * - 4!을 돌릴 때 String으로 돌리지 않고, temp = (temp % 1000) * 10 + (temp / 1000); // 실행할 때마다 한 칸씩 밀림
 * - 직관성: "전체 시계수를 미리 다 구해서 Map에 넣기"보다 "1111부터 내 목표까지 가면서 시계수만 세기"가 코드가 더 짧고 실수할 확률이 적습니다.
 */
public class BOJ_2659 {
    static Map<Integer, Integer> clockNumMap  = new HashMap<>();

    private static void makeClockNum() {
        int num = 1110;
        int order = 1;
        while (num<=9999){
            num++;

            String numStr = String.valueOf(num);
            if(numStr.contains("0")) continue; // 0을 포함하면 스킵!

            int minValue = Integer.MAX_VALUE;
            for(int i=0; i<4; i++){
                int value = Integer.parseInt(numStr.substring(i, 4)+numStr.substring(0,i));
                minValue = Math.min(minValue, value);
            }

            if(clockNumMap.containsKey(minValue)) continue; // 이미 등록된 시계수라면 스킵!
//            System.out.println("===============");
//            System.out.println(num);
//            System.out.println(minValue);
//            System.out.println(order);
//            System.out.println("===============");
            clockNumMap.put(minValue, order++);
        }
    }

    private static int findClockNum(String initValue){
        int minValue = Integer.MAX_VALUE;
        for(int i=0; i<4; i++){
            int value = Integer.parseInt(initValue.substring(i, 4)+initValue.substring(0,i));
            minValue = Math.min(minValue, value);
        }
        return minValue;
    }

    public static void main(String[] args) throws IOException {
        makeClockNum();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<4; i++){
            sb.append(st.nextToken());
        }

        int clockNum = findClockNum(sb.toString());
        //System.out.println("주어진 입력의 시계수: " + clockNum);
        System.out.println(clockNumMap.get(clockNum));

    }
}
