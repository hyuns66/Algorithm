import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 돈 갚기
 *
 * 상근이는 B달러를 빌렸다.
 * 매월 초에 내야하는 금액의 R퍼센트가 이자로 붙는다.
 * 매월 말 과외비 M달러를 받고, 이 금액 만큼 선영이한테 갚을 수 이따.
 *
 * 상근이나 이 상황에서 돈을 다 갚는데 몇 달이 걸리는 지 구하는 프로그램을 작성하시오.
 * ================================================================
 * 부동소수점 때문에 아예 정수 연산으로 바꿔버렸다!!!
 */
public class BOJ_9333 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine()); // 테스트 케이스의 수 (1~1000)

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<tc; i++){
            //System.out.println(i+"번째");
            StringTokenizer st = new StringTokenizer(br.readLine());
            float r = Float.parseFloat(st.nextToken()); // R<=50.00
            float b = Float.parseFloat(st.nextToken()); // B<=50000.00
            float m = Float.parseFloat(st.nextToken()); // M<=50000.00

            int month = 1;

            // Math.round를 사용해 소수점 오차를 제거하며 정수로 변환
            long R = Math.round(r * 100);
            long B = Math.round(b * 100);
            long M = Math.round(m * 100);
            while (true){
                // 이자 매기기
                B += Math.round(B*R/10000.0);
                //System.out.println("needToPay = "+needToPay);

                // 지불
                B-= M;
                if(B<=0) break;

                // 다음달로 이동
                month++;
                if(month>1200) break;
            }

            if(month>1200){
                sb.append("impossible\n");
            }else {
                sb.append(month).append("\n");
            }
        }

        System.out.println(sb);
    }
}
