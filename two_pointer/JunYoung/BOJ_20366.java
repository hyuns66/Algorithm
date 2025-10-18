import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 같이 눈사람 만들래?
 *
 * N개의 눈덩이가 있다.
 * 각 눈덩이의 지름은 Hi이다.
 *
 * 하나의 눈사람은 두개의 눈덩이로 구성되며,
 * 눈덩이 하나를 아래에 두고, 그 눈덩이보다 크지 않은 다른 눈덩이를 쌓아올리는 방식으로 만들 수 있다.
 *
 * N개의 눈덩이 중 서로 다른 4개를 골라 눈사람을 각자 1개씩, 총 2개를 만들려고 한다.
 * 두 자매는 두 눈사람의 키의 차이가 작을 수록 눈사람의 사이가 좋을 것이라 믿는다.
 *
 * 만들 수 있는 두 눈사람의 키 차이 중 최솟값은??
 */
public class BOJ_20366 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int snowBallNum = Integer.parseInt(br.readLine());

        List<Integer> snowBalls = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<snowBallNum; i++){
            snowBalls.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(snowBalls);

        int answer = Integer.MAX_VALUE;

        // 외부 눈사람
        for(int i=0; i<snowBallNum-3; i++){
            for(int j=i+3; j<snowBallNum; j++){
                // 내부 눈사람 (투 포인터)
                int sIdx = i+1;
                int eIdx = j-1;

                while (sIdx<eIdx){
                    int outsideSnowman = snowBalls.get(i) + snowBalls.get(j);
                    int insideSnowman = snowBalls.get(sIdx) + snowBalls.get(eIdx);

                    answer = Math.min(answer, Math.abs(outsideSnowman-insideSnowman));
                    if(insideSnowman<outsideSnowman) sIdx++;
                    else eIdx--;
                }
            }
        }

        System.out.println(answer);
    }
}
