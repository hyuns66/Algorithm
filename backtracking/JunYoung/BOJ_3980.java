import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 선발 명단
 *
 * 4-4-2 다이어몬드 전술
 * 11명의 선수의 각 포지션에서의 능력 = 0~100
 * (능력치가 0인 포지션에는 배치 X)
 *
 * 모든 선수의 포지션을 정하는 프로그램
 * 모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값을 한 줄에 하나씩 출력한다.
 */
public class BOJ_3980 {

  static boolean[] assigned;
  static int answer = 0;
  static int tempAnswer = 0;
  static int[][] playerPower;

  public static void func(int currentPlayer){
    if (currentPlayer>=12) {
      answer = Math.max(answer, tempAnswer);
      return;
    }

    for(int pos=1; pos<=11; pos++){
      if(playerPower[currentPlayer][pos]!=0 && assigned[pos]!=true){
        assigned[pos] = true;
        tempAnswer+= playerPower[currentPlayer][pos];
        func(currentPlayer+1);
        tempAnswer-= playerPower[currentPlayer][pos];
        assigned[pos] = false;
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int testCaseNum = Integer.parseInt(br.readLine());

    int[] answers = new int[testCaseNum];
    for(int i=0; i<testCaseNum; i++){
      // 각 테스트마다,
      assigned = new boolean[12];
      playerPower = new int[12][12];
      for(int player=1; player<=11; player++){
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int position=1; position<=11; position++){
          int power = Integer.parseInt(st.nextToken());
          playerPower[player][position] = power;
        }
      }

      // 모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값?
      func(1);

      // 정답 입력
      answers[i] = answer;
      answer = 0;
    }

    for(int i=0; i<testCaseNum; i++){
      System.out.println(answers[i]);
    }

  }
}
