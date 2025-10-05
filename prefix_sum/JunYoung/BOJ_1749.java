import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 점수 따먹기
 *
 * 2 3 -21 -22 -23
 * 5 6 -22 -23 -25
 * -22 -23 4 10 2
 *
 * 정수의 합이 최대가 되는 부분행렬을 구해서 동주에게서 벗어나고 싶다.
 */
public class BOJ_1749 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int rowNum = Integer.parseInt(st.nextToken());
        int colNum = Integer.parseInt(st.nextToken());

        int[][] arr = new int[rowNum+1][colNum+1];
        for(int r=1; r<=rowNum; r++){
            st = new StringTokenizer(br.readLine());
            for(int c=1; c<=colNum; c++){
                int value = Integer.parseInt(st.nextToken());
                arr[r][c] = arr[r-1][c]+arr[r][c-1]-arr[r-1][c-1]+value;
            }
        }

        // 부분행렬
        int maxValue = arr[1][1]; // arr가 모두 음수일수도 있다..
        for(int endY=1; endY<=rowNum; endY++){
            for(int endX=1; endX<=colNum; endX++){
                for(int row=0; row<endY; row++){
                    for(int col=0; col<endX; col++){
                        // (startY~endY/startX~startY)
                        // [기본엔 row의 누적합을 구해서 이렇게 row별로 돌면서 했었는데 시간초과]
//                        for(int row = startY; row<=endY; row++){
//                            if(startX==endX) sum += arr[row][startX];
//                            else sum += arr[row][endX]-arr[row][startX];
//                        }
                        int sum = arr[endY][endX] - arr[endY][col] - arr[row][endX] + arr[row][col];
                        maxValue = Math.max(maxValue, sum);
                    }
                }
            }
        }
        System.out.println(maxValue);

    }
}
/**
 * 시도1) 4%에서 시간초과
 * 시도2) 음수가 답일 수 있는데 처음부터 maxValue=0으로 초기화함!
 */
