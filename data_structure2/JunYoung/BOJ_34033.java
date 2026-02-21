import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 공금 횡령 (검출)
 *
 * 쿠미니는 동아리 공금을 다음과 같은 방법으로 횡령했다.
 * - 필요한 물품이 있을 때, 자신의 사업체에 구매 요청을 한다.
 * - 자신의 사업체는 해당 물품의 정가 105%를 초과하는 가격으로 청구하고, 결제를 진행한다.
 *
 * 동일한 사업체에서 비싼 가격으로 구매한 것이 의심스러웠던 캡틴은 조사를 진행하고자한다.
 * 물품의 정가 정보와 실제 거래 내역이 주어질 때, 횡령이 의심되는 거래의 건수?
 *
 * ======================================================================
 * 알고리즘 유형 = 정가를 저장할 해시맵
 */
public class BOJ_34033 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken()); // 물품의 개수 (1~100,000=십만)
        int tradeNum = Integer.parseInt(st.nextToken()); // 거래의 개수 (1~100,000=십만)

        Map<String, Integer> priceMap = new HashMap<>();
        for(int i=0; i<num; i++){
            st = new StringTokenizer(br.readLine());
            String product = st.nextToken(); // 물품의 이름 (1~10길이)
            int price = Integer.parseInt(st.nextToken()); // 물품의 정가 (1~100,000=십만)
            priceMap.put(product, price);
        }

        int suspicion = 0;
        for(int t=0; t<tradeNum; t++){
            st = new StringTokenizer(br.readLine());
            String product = st.nextToken(); // 물품의 이름 (1~10길이) // 앞에 등록해둔 문자 중 하나임을 보장한다!
            int price = Integer.parseInt(st.nextToken()); // 물품의 정가 (1~100,000=십만)

            // 정가 알아내기
            int priceOrigin = priceMap.get(product);
            if(1.05*priceOrigin<price){
                // 정가의 1.05배보다 비싸면 횡령을 의심!
                suspicion++;
            }
        }

        System.out.println(suspicion);
    }
}
