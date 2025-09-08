import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

/**
 * 다각형의 면적
 *
 * 2차원 평면 상에 N = 3~10,000개의 점으로 이루어진 다각형이 있다.
 * 이 다각형의 면적을 구하시오
 * https://oozoowos.tistory.com/entry/%EA%B8%B0%ED%95%98-%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EB%8A%94-%EA%B3%B5%EC%8B%9D
 * 공식보고 따라함
 *
 * long타입이 필요!
 */
public class BOJ_2166 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        long[] xArr = new long[num+1];
        long[] yArr = new long[num+1];

        for(int i=0; i<num; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            xArr[i] = x;
            yArr[i] = y;
        }

        xArr[num] = xArr[0];
        yArr[num] = yArr[0];

        // 신발끈 공식
        long x = 0;
        long y = 0;
        for(int i=1; i<xArr.length; i++){
            x+= xArr[i-1]*yArr[i];
            y+= xArr[i]*yArr[i-1];
        }

        System.out.printf("%.1f\n", Math.abs(x-y)/2.0);
        // Math.round로 하니까 지수 표현법으로 된다.
    }
    
}
