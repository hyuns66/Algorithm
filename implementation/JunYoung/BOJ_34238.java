import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Find the Fox
 *
 * N행 M열의 글자판
 * 글자판의 각 칸에는 영어 알파벳 F,O,X 중 하나가 쓰여있다.
 *
 * -> 글자판에서 영단어 FOX를 모두 찾자.
 * 1. 처음에 알파벳 F를 선택한다.
 * 2. 1에서 선택한 F와 상하좌우/대각선으로 인접한 알파벳 O를 선택한다.
 * 3. 2에서 선택한 O와 상하좌우/대각선으로 인접한 알파벳 X를 선택한다.
 * 4. 1,2,3에서 선택한 FOX가 모두 같은 행, 같은 열, 같은 대각선에 있을 경우 FOX를 찾은 것이다.
 *
 * (겹쳐진 FOX들도 모두 구분해서 세어줘야한다.)
 * => 글자판이 주어지면 FOX가 모두 몇 개 있는 지 구하여라.
 *
 */
public class BOJ_34238 {
    static char[][] array;
    static int[] dy = {-1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dx = {0, 0, -1, 1, -1, 1, -1, 1};

    static int countIfOX(int fy, int fx){
        int count = 0;
        for(int dir=0; dir<dy.length; dir++){
            if(fy+2*dy[dir]<0 || fy+2*dy[dir]>=array.length) continue; // y가 범위를 넘어가면 카운트 안함
            if(fx+2*dx[dir]<0 || fx+2*dx[dir]>=array[0].length) continue; // x가 범위를 넘어가면 카운트 안함
            if(array[fy+dy[dir]][fx+dx[dir]]=='O' && array[fy+2*dy[dir]][fx+2*dx[dir]]=='X'){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());

        // N개의 줄에 걸쳐 각 칸에 쓰인 알파벳이 각 행마다 주어진다. (주어지는 알파벳은 FOX중 하나이다.)

        // 1. 맵 저장
        array = new char[row][col];
        for(int rIndex=0; rIndex<row; rIndex++){
            String line =  br.readLine();
            for(int cIndex=0; cIndex<col; cIndex++){
                char c = line.charAt(cIndex);
                array[rIndex][cIndex] = c;
            }
        }

        // 2. 맵 순회하면서 FOX 찾기
        int answer = 0;
        for(int rIndex=0; rIndex<row; rIndex++) {
            for (int cIndex = 0; cIndex < col; cIndex++) {
                if (array[rIndex][cIndex] == 'F'){ // 2-1. F를 찾았다면
                    // 상하좌우, 대각선으로 OX가 있는지 체크해야한다.
                    answer += countIfOX(rIndex, cIndex);
                }
            }
        }

        System.out.println(answer);
    }
}
