import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * IF문 좀 대신 써줘
 *
 * 혼자서 게임을 개발하느라 바쁜 밀리를 대신하여,
 * 캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성하자
 *
 * ------------------------------------------------
 * String[] 전투력문자열 (WEAK, NORMAL, STRONG)
 * int[] 전투력 (10000, 100000, 10000000)
 *
 * 접근방법1
 * - 하나씩 비교하면서 어디에 해당하는지 찾기 (10^5*10^5)
 *   (10,000,000,000 = 100억)
 * - 캐릭터의 전투력이 왼쪽 클래스보단 크고, 현재 클래스보단 작거나 같으면 현재클래스에 속한다.
 *
 * 정확한 값을 찾기 위한게 아닌 이분탐색
 * upperBound: wndjwls rk
 *
 */
public class BOJ_19637 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int typeNum = Integer.parseInt(st.nextToken()); // 1~100,000(십만)
        int characterNum = Integer.parseInt(st.nextToken()); // 1~100,000(십만)

        String[] typeName = new String[typeNum];
        int[] typeUpper = new int[typeNum];
        // 칭호는 전투력 상한값의 오름차순으로 주어진다.
        for(int i=0; i<typeNum; i++){
            st = new StringTokenizer(br.readLine());
            String type = st.nextToken();
            int upper = Integer.parseInt(st.nextToken());
            typeName[i] = type;
            typeUpper[i] = upper;
        }

        // 각 캐릭터의 전투력 판별
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<characterNum; i++){
            int stat = Integer.parseInt(br.readLine());

            int left=0;
            int right=typeNum-1;
            while (left<right){
                int mid = (left+right)/2;
                int midVal = typeUpper[mid];

                if(stat<=midVal){ // 캐릭터의 전투력이 upper전투력보다 작거나 같으면 해답이 될지도 모름
                    right=mid; // 유지
                }else{ // 캐릭터의 전투력이 upper전투력보다 높으면 다음레벨에 답이 있음
                    left=mid+1;
                }
            }
            sb.append(typeName[right]+"\n");
        }

        System.out.println(sb);
    }
}
