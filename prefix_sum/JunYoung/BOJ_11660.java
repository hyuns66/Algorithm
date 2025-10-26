import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

/**
 * 구간 합 구하기5
 *
 * NxN개의 수가 NxxN크기의 표에 채워져있다.
 * N = 1~1024
 * M = 합을 구해야하는 횟수 M = 1~100,000(십만)
 * M개의 줄에 네 개의 정수 x1,y1,x2,y2가 주어지며, (x1,y1)~(x2,y2)의 합을 구해 출력해야한다.
 * x1<=x2, y1<=y2
 *
 * 표에 채워져있는 수는 1000보다 작거나 같은 자연수이다. => NxNx1000이 int 범위인지 -> 10억 정도로 int 범위!!
 *
 * --------------------------------------------------------------------------------------------------
 * 헷갈렸던 부분 (x1,y1)가 들어오는데, 나는 평소에 x를 col인덱스로 생각하고 있었는데 여기서 x는 row, 즉 행의 역할을 한다!
 */
public class BOJ_11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int mapSize = Integer.parseInt(st.nextToken());
        int queryNum = Integer.parseInt(st.nextToken());

        // 1. 맵 입력받기 & 2. 누적합 계산하기 = O(N^2) = O(1024x1024)
        int[][] map = new int[mapSize+1][mapSize+1];
        int[][] dp = new int[mapSize+1][mapSize+1];
        for(int i=1; i<=mapSize; i++){
            st = new StringTokenizer(br.readLine());
            int rowSum = 0;
            for(int j=1; j<=mapSize; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                rowSum += map[i][j];
                dp[i][j] = rowSum;
            }
        }

        // 3. (x1,y1)~(x2,y2)까지 합을 구하기
        // 시간복잡도 = O(MxN) = O(100000x1024) = O(102,400,000) = 1억
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<queryNum; i++){
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            int result = 0;
            for(int row=r1; row<=r2; row++){
                result += dp[row][c2] - dp[row][c1-1]; // x1~x2까지의 합은 (x2까지합 - x1이전까지의합)
            }
            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
