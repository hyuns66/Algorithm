import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 스도쿠
 */
public class BOJ_2239 {
  static int N = 9;
  static int[][] arr;
  static boolean[][] rowVisited;
  static boolean[][] colVisited;
  static boolean[][] boxVisited;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    arr = new int[N][N];
    rowVisited = new boolean[N][N+1]; // i번 row에 1~9번이 사용됨 여부
    colVisited = new boolean[N][N+1]; // j번 col에 1~9번이 사용됨 여부
    boxVisited = new boolean[N][N+1]; // x번 사각형에 1~9번이 사용됨 여부

    for(int i=0; i<N; i++){
      String s = br.readLine();
      for(int j=0; j<N; j++){
        int value = s.charAt(j)-'0';
        arr[i][j] = value;

        if(value==0) continue;
        // 1~9가 어떻게 사용되었는지 기록
        rowVisited[i][value] = true;
        colVisited[j][value] = true;
        int whichBox = (i/3)*3+(j/3);
        boxVisited[whichBox][value] = true;
      }
    }

    sudoku(0);
  }

  private static boolean sudoku(int index){
    if(index == N*N){ // 완성조건(0부터 시작했으니까 80이 마지막, 81이면 종료)
      for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
          System.out.print(arr[i][j]);
        }
        System.out.println();
      }
      return true; // 사전순으로 첫번째로 완성된거만 출력하고 종료하면 된다.
    }

    int row = index/N;
    int col = index%N;
    if(arr[row][col]!=0){
      return sudoku(index+1);
    }

    // 0인 부분에 대해서 1~9사이의 숫자를 채워넣기
    for(int n=1; n<=9; n++){
      if(rowVisited[row][n]) continue;
      if(colVisited[col][n]) continue;
      int whichBox = (row/3)*3+(col/3);
      if(boxVisited[whichBox][n]) continue;

      // 숫자 배치
      arr[row][col] = n;
      rowVisited[row][n] = true;
      colVisited[col][n] = true;
      boxVisited[whichBox][n] = true;

      if(sudoku(index+1)) return true;

      // 되돌리기
      arr[row][col] = 0;
      rowVisited[row][n] = false;
      colVisited[col][n] = false;
      boxVisited[whichBox][n] = false;
    }

    return false;
  }

}
