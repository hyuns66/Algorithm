import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 쿼드트리
 * 흑백 영상을 압축하여 표현하는 데이터 구조
 *
 * 흰점을 나타내는 0
 * 검은점을 나타내는 1
 *
 */
public class BOJ_1992 {
    public static String divide(int[][] arr, int startRow, int startCol, int length){
        int sum = 0;
        for(int r=startRow; r<startRow+length; r++){
            for(int c=startCol; c<startCol+length; c++){
                sum+=arr[r][c];
            }
        }

        //System.out.println(startRow+","+startCol+": length = "+ length);
        //System.out.println(sum);

        // 다 0으로 이뤄져있는 경우
        if(sum==0){
            //System.out.println("0으로 이뤄져있음");
            return "0";
        }

        // 다 1로 이뤄져있는 경우
        if(sum==length*length){
            //System.out.println("1으로 이뤄져있음");
            return "1";
        }

        // 섞여있는 경우 다시 divide
        //System.out.println("섞여있음");
        String leftTop = divide(arr, startRow, startCol, length/2);
        String rightTop = divide(arr, startRow, startCol+length/2, length/2);
        String leftBottom = divide(arr, startRow+length/2, startCol, length/2);
        String rightBottom = divide(arr, startRow+length/2, startCol+length/2, length/2);
        return "("+leftTop+rightTop+leftBottom+rightBottom+")";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][n];
        for(int row=0; row<n; row++){
            String line = br.readLine();
            for(int col=0; col<n; col++){
                arr[row][col] = line.charAt(col)-'0'; // 이 부분 주의해주기! 아스키값으로 저장안되고 문자가 가진 숫자로 저장되게끔!
            }
        }

        String answer = divide(arr, 0, 0, n);
        System.out.print(answer);
    }
}
