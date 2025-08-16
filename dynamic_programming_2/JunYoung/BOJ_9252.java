import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * LCS2
 * : 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것?
 *   ACAYKP와 CAPCAK의 LCS는 ACAK
 *
 */
public class BOJ_9252 {

  static int[][] DP;
  static String strA;
  static String strB;
  static List<Character> path = new ArrayList<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    strA = br.readLine();
    strB = br.readLine();

    // DP 테이블 만들기
    DP = new int[strA.length()+1][strB.length()+1];
    for(int i=1; i<=strA.length(); i++){
      for(int j=1; j<=strB.length(); j++){
        if(strA.charAt(i-1)==strB.charAt(j-1)) DP[i][j] = DP[i-1][j-1]+1;
        else DP[i][j] = Math.max(DP[i-1][j], DP[i][j-1]);
      }
    }

    // 문자열 복원
    getText(strA.length(), strB.length());

    // 정답 출력
    System.out.println(DP[strA.length()][strB.length()]);
    for(int i=path.size()-1; i>=0; i--){
      System.out.print(path.get(i));
    }
    System.out.println();

  }

  static void getText(int row, int col){
    if(row==0 || col==0) return;

    if(strA.charAt(row-1)==strB.charAt(col-1)){
      // 문자열이 같으면 LCS에 add
      path.add(strA.charAt(row-1));
      getText(row-1, col-1);
    }else{
      // DP값이 더 높은 쪽으로 이동
      if(DP[row-1][col]<DP[row][col-1]){
        getText(row, col-1);
      }else{
        getText(row-1, col);
      }
    }
  }
}
