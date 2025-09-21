import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

/**
 * 도시와 비트코인
 * - 진우는 거래소에서 비트코인을 매도하려고한다.
 *
 * - 도시는 가로 N, 세로 M 크기의 격자모양으로 이루어져있다.
 * - 진우는 왼쪽상단끝에 있고, 거래소는 우측하단끝에 있다.
 * - 공터와 도로는 지나갈 수 있지만, 건물은 지나갈 수 없다.
 *
 * - 오른쪽, 아래쪽으로만 이동하여 거래소에 최대한 빨리 도착하자.
 * - 진우의 현재 위치가 거래소 일 수 있다.
 *
 */
public class BOJ_31575 {
    static class Pos{
        int row;
        int col;

        Pos(int row, int col){
            this.row = row;
            this.col = col;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int colSize = Integer.parseInt(st.nextToken()); // 가로크기
        int rowSize = Integer.parseInt(st.nextToken()); // 세로크기

        // 맵 기록하기 (최대 300x300)
        int[][] arr = new int[rowSize][colSize];
        for(int i=0; i<rowSize; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<colSize; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //bfs로 rowSize, colSize까지 도달할 수 있는지 측정
        Deque<Pos> queue = new ArrayDeque<>();
        queue.add(new Pos(0,0));

        // 리팩토링1) visited 안해서 오른쪽, 아래 방향으로 돌리니까 메모리 초과나서 추가해봄
        boolean[][] visited = new boolean[rowSize][colSize];
        visited[0][0] = true;

        boolean answer = false;
        while (!queue.isEmpty()){
            Pos current = queue.pollFirst();
            if(current.row== rowSize-1 && current.col==colSize-1) {
                answer = true;
                break;
            }

            // 아래
            if(current.row+1<rowSize && !visited[current.row+1][current.col] && arr[current.row+1][current.col]==1){
                visited[current.row+1][current.col] = true;
                queue.addLast(new Pos(current.row +1, current.col));
            }
            // 오른쪽
            if(current.col+1<colSize && !visited[current.row][current.col+1] && arr[current.row][current.col+1]==1){
                visited[current.row][current.col+1] = true;
                queue.addLast(new Pos(current.row, current.col+1));
            }
        }

        if(answer) System.out.println("Yes");
        else System.out.println("No");
    }
}
