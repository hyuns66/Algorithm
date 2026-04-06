import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 크냑과 3D 프린터
 * 히스토그램은 너비가 1로 동일한 막대 N개가 빈틈없이 일렬로 붙어있는 형태
 * 크냑은 이를 너비와 폭이 1이고, 높이가 hi인 N개의 직육면체로 이루어진 3D 모형으로 출력할 것이다.
 *
 * 히스토그램의 정보가 주어졌을 때, 3D 모형의 겉넓이를 구해보자.
 */
public class BOJ_30923 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numOfHist = Integer.parseInt(br.readLine()); // 히스토그램 막대수 (1~32768)

        StringTokenizer st = new StringTokenizer(br.readLine());

        long guk = 0; // 30000 * 30000* 4 = 3,600,000,000  (36억도 답이 될수도 있다.)
        int prevHeight = 0;
        for(int i=0; i<numOfHist; i++){
            int height = Integer.parseInt(st.nextToken());
            guk += 2; // 위 아래 넓이 더하기
            guk += 2L *height; // 앞, 뒤
            guk += Math.abs(prevHeight-height); // 좌
            prevHeight = height;
        }
        guk += prevHeight; // 마지막 히스토그램의 우

        System.out.println(guk);
    }
}
