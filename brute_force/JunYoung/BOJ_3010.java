import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 페그
 * - 칩이 다른 칩을 점프해서 점프한 칩을 제거하는 게임이다.
 * - 게임은 보드판에 칩이 하나 남을 때까지 계속한다.
 *
 * - o는 칩, .는 빈칸을 나타낸다.
 * - 플레이어가 칩 하나를 고른다음, 인접한 칸에 칩이 있고, 그 다음 칸이 비어있다면
 * - 그 칩을 뛰어넘고 뛰어넘은 칩을 보드판에서 제거한다. (방향은 위/아래/오른쪽/왼쪽)
 *
 * 보드의 상태가 주어졌을 때, 플레이어가 칩을 움직일 수 있는 올바른 방법의 수는?
 *
 * =================================================================
 * 7x7 맵에서
 * . 을 만났을 때, 상하좌우2칸을 탐색하면서 2칸이 모두 o이면 경우의 수 +1
 */
public class BOJ_3010 {

    public static int countMovement(int y, int x, int[][] arr){
        int count = 0;
        if(y-2>=0&&arr[y-1][x]==1&&arr[y-2][x]==1) count++; // 상
        if(y+2<7&&arr[y+1][x]==1&&arr[y+2][x]==1) count++; // 하
        if(x-2>=0&&arr[y][x-1]==1&&arr[y][x-2]==1) count++; // 좌
        if(x+2<7&&arr[y][x+1]==1&&arr[y][x+2]==1) count++; // 우
        return count;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 페그 보드판 기록
        int[][] arr = new int[7][7];
        for(int i=0; i<7; i++){
            String line = br.readLine();
            for(int j=0; j<7; j++){
                char c = line.charAt(j);
                if(c=='.') arr[i][j] = 0;
                else if(c=='o') arr[i][j] = 1;
                else arr[i][j] = -1; // 맵이 아니다.
            }
        }

        int answer = 0;
        for(int i=0; i<7; i++){
            for(int j=0; j<7; j++){
                if(arr[i][j]==0){ // .을 발견했을 때,
                    int count = countMovement(i, j, arr); // 상하좌우로 갈 수 있는 경우의수를 count
                    answer+=count;
                }
            }
        }

        System.out.println(answer);
    }
}
