import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 스테판 쿼리
 *
 * 게임은 다음과 같이 진행된다.
 * 총 N라운드
 * 게임은 진사람이 탈락하고, 이긴 사람이 게임을 계속하는 서바이벌 형태
 * (비긴 경우 새로 출전한 사람이 승리한다. / 첫판에는 비기는 경우가 없다고 하자)
 * 가위 =1, 바위 = 2, 보 = 3
 * 가장 많은 승리를 거머쥐고 상을 받게될 선수는 몇연승을 거둘 수 있을까?
 *
 * ---------------------------------------------------------------
 * static 변수를 좀 많이 빼고 teamAWin이랑 teamBWin이랑 사실 같은 함수인데 두개로 나눈게 좀 거슬리는 느낌이긴하다..
 * 첫판도 따로 나누고 시작한 점도...
 */
public class BOJ_14654 {
    static int maxRow = 0;
    static int teamARow = 0;
    static int teamBRow = 0;
    static boolean prevAWin = false;

    private static void teamAWin() {
        if(!prevAWin) { // B의 연승 횟수 초기화
            teamBRow = 0;
        }
        teamARow++;
        maxRow = Math.max(maxRow, teamARow); // A의 연승횟수 그때그때 업데이트
        prevAWin = true;
    }

    private static void teamBWin() {
        if(prevAWin) { // A의 연승 횟수 초기화
            teamARow = 0;
        }
        teamBRow++;
        maxRow = Math.max(maxRow, teamBRow); // B의 연승횟수 그때그때 업데이트
        prevAWin = false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int roundNum = Integer.parseInt(br.readLine());

        int[] teamA = new int[roundNum];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<roundNum; i++){
            teamA[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());

        // 첫판은 따로 수행
        int teamAValue = teamA[0]-1;
        int teamBValue = Integer.parseInt(st.nextToken())-1;
        // A team이 가위바위보에서 승
        if(teamAValue==(teamBValue+1)%3){
            prevAWin = true;
            teamARow++;
            maxRow = Math.max(maxRow, teamARow);
        }else{
            prevAWin = false;
            teamBRow++;
            maxRow = Math.max(maxRow, teamBRow);
        }

        for(int i=1; i<roundNum; i++){
            // 가위 = 0, 바위=1, 보=2로 재설정
            teamAValue = teamA[i]-1;
            teamBValue = Integer.parseInt(st.nextToken())-1;

            // A team이 가위바위보에서 승
            if(teamAValue==(teamBValue+1)%3){
                teamAWin();
            }else if(teamAValue==teamBValue){
                if(prevAWin){
                    // 새로 들어온 B가 이김
                    teamBWin();
                }else {
                    // 새로 들어온 A가 이김
                    teamAWin();
                }
            }else{ // B team이 가위바위보에서 승
                teamBWin();
            }
        }


        System.out.println(maxRow);
    }
}
