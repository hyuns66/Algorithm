import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * RGB거리2
 *
 * RGB 거리에는 집에 N개 있다. (거리는 선분)
 * 집은 빨강, 초록, 파랑 중 하나의 색
 * 집들은 좌우집의 색과 같지 않아야한다.
 *
 * 모든 집을 칠하는 비용의 최소는??
 *
 * =======================================
 * 풀이 참조함. 다시 풀어보기
 */
public class BOJ_17404 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 집의 수 = N = 2~1,000
        int houseNum = Integer.parseInt(br.readLine());

        int[][] cost = new int[houseNum][3];
        for(int i=0; i<houseNum; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 칠하는 비용 1~1000
            int redCost = Integer.parseInt(st.nextToken());
            int greenCost = Integer.parseInt(st.nextToken());
            int blueCost = Integer.parseInt(st.nextToken());
            cost[i][0] = redCost;
            cost[i][1] = greenCost;
            cost[i][2] = blueCost;
        }

        // 3^1000 (모든 경우의 수를 칠해보는 수) = 엄~~청 큰 수
        int[][] redDp = new int[houseNum][houseNum];
        int[][] greenDp = new int[houseNum][houseNum];
        int[][] blueDp = new int[houseNum][houseNum];

        redDp[0][0] = cost[0][0];
        redDp[0][1] = Integer.MAX_VALUE;
        redDp[0][2] = Integer.MAX_VALUE;

        greenDp[0][0] = Integer.MAX_VALUE;
        greenDp[0][1] = cost[0][1];
        greenDp[0][2] = Integer.MAX_VALUE;

        blueDp[0][0] = Integer.MAX_VALUE;
        blueDp[0][1] = Integer.MAX_VALUE;
        blueDp[0][2] = cost[0][2];

        for(int i=1; i<houseNum; i++){
            for(int j=0; j<3; j++){
                redDp[i][j] = Math.min(redDp[i-1][(3+(j-1))%3],redDp[i-1][(j+1)%3]);
                if(redDp[i][j]!=Integer.MAX_VALUE) redDp[i][j] += cost[i][j];

                greenDp[i][j] = Math.min(greenDp[i-1][(3+(j-1))%3],greenDp[i-1][(j+1)%3]);
                if(greenDp[i][j]!=Integer.MAX_VALUE) greenDp[i][j] += cost[i][j];

                blueDp[i][j] = Math.min(blueDp[i-1][(3+(j-1))%3],blueDp[i-1][(j+1)%3]);
                if(blueDp[i][j]!=Integer.MAX_VALUE) blueDp[i][j] += cost[i][j];
            }
        }

//        for(int[] arr: greenDp){
//            System.out.println(Arrays.toString(arr));
//        }

        int firstRedCaseCost = Math.min(redDp[houseNum-1][1], redDp[houseNum-1][2]);
        int firstGreenCaseCost = Math.min(greenDp[houseNum-1][0], greenDp[houseNum-1][2]);
        int firstBlueCaseCost = Math.min(blueDp[houseNum-1][0], blueDp[houseNum-1][1]);

        int answer = Math.min(firstRedCaseCost, firstGreenCaseCost);
        answer = Math.min(answer, firstBlueCaseCost);
        System.out.println(answer);
    }
}
