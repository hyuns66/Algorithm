import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 회전 초밥
 *
 * 벨트위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.
 * 1. 임의의 한 위치로부터 k개의 접시를 연속해서 먹을 경우 정액가격으로 제공한다.
 * 2. 초밥 종류가 적힌 쿠폰을 하나 발행해준다. 1번 행사에 참여할 경우 무료로 제공
 *
 * - 음식점의 벨트 상태
 * - 메뉴에 있는 초밥의 가짓수
 * - 연속해서 먹는 접시의 개수
 * - 쿠폰 번호가 주어졌을 때
 * 위 행사에 참여한, 손님이 먹을 수 있는 초밥 가짓수의 최댓값?
 *
 * ------------------------------------------------------------------
 * 접근1. 슬라이딩 윈도우 (현재 종류 셀 때에는 Set보다 Map이 빠를 것 같아서 Map 사용함. Set은 특정 원소 빼려면 결국 순회가 필요하다고 생각해 비효율적이라 생각함)
 * 레일에 있는 초밥의 개수가 삼백만이라 k개 구간에 대해 for문을 다 돌리면 최소(레일 넘어가지 않는 선만 계산) 3000000*3000 = 9,000,000,000(90억) -> 무조건 슬라이딩 윈도우써야함.
 */
public class BOJ_15961 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int dishNum = Integer.parseInt(st.nextToken()); // 2~3,000,000 (삼백만)
        int varietyNum = Integer.parseInt(st.nextToken()); // 2~3,000 (삼천)
        int dishInARow = Integer.parseInt(st.nextToken()); // 2~3,000 (삼천) // dishNum보단 작거나 같다.
        int coupon = Integer.parseInt(st.nextToken()); // 1~varietyNum

        int[] rail = new int[dishNum];
        Map<Integer, Integer> isIn = new HashMap<>();
        int varietyCount = 0;
        int maxVariety = 0;

        // 쿠폰은 무조건 넣기
        isIn.put(coupon, 1);
        varietyCount++;

        // 우선 무조건 k개 만큼 담아보기
        for(int i=0; i<dishInARow; i++){
            rail[i] = Integer.parseInt(br.readLine());
            // 아직 범위에 없는 초밥이면
            if(isIn.getOrDefault(rail[i],0)==0){
                varietyCount++; // 종류수 늘리기
            }
            isIn.put(rail[i], isIn.getOrDefault(rail[i], 0)+1);
        }
        maxVariety = Math.max(maxVariety, varietyCount);


        for(int i=dishInARow; i<dishNum; i++){
            rail[i] = Integer.parseInt(br.readLine());
            // 슬라이딩 윈도우 젤 앞에꺼 빼기
            int newCount = isIn.get(rail[i-dishInARow])-1;
            isIn.put(rail[i-dishInARow], newCount);
            if(newCount==0) varietyCount--;

            // 슬라이딩 윈도우에 새로운 원소 넣기
            // 아직 범위에 없는 초밥이면
            if(isIn.getOrDefault(rail[i],0)==0){
                varietyCount++; // 종류수 늘리기
            }
            isIn.put(rail[i], isIn.getOrDefault(rail[i], 0)+1);

            maxVariety = Math.max(maxVariety, varietyCount);
        }

        // 슬라이딩 윈도우의 마지막이 rail의 마지막 원소인데,
        // 슬라이딩 윈도우의 시작이 rail의 마지막 원소에 올때까지
        for(int i=dishNum; i<dishNum+dishInARow-1; i++){
            // 슬라이딩 윈도우 젤 앞에꺼 빼기
            int newCount = isIn.get(rail[(i-dishInARow)%dishNum])-1;
            isIn.put(rail[(i-dishInARow)%dishNum], newCount);
            if(newCount==0) varietyCount--;

            // 슬라이딩 윈도우에 새로운 원소 넣기
            // 아직 범위에 없는 초밥이면
            if(isIn.getOrDefault(rail[(i)%dishNum],0)==0){
                varietyCount++; // 종류수 늘리기
            }
            isIn.put(rail[(i)%dishNum], isIn.getOrDefault(rail[(i)%dishNum], 0)+1);

            maxVariety = Math.max(maxVariety, varietyCount);
        }

        System.out.println(maxVariety);
    }
}
