//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
///**
// * 색종이 붙이기
// *
// * 1x1~5x5크기까지 5종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
// * 색종이를 크기가 10x10인 종이위에 붙이려고 한다.
// * 종이는 1x1칸으로 나눠져있으며
// * 각 칸에는 0또는 1이 적혀있다.
// *
// * 1이 적힌 칸은 모두 색종이로 덮여져야한다.
// * 색종이를 붙일 때에는 종이의 경계 밖으로 나가서는 안되고, 겹쳐서도 안된다.
// * 0이 적힌 칸에는 색종이가 있으면 안된다.
// *
// */
//public class BOJ_17136 {
//    static int LENGTH = 10;
//    static int[] coverLeft = {5,5,5,5,5};
//    static int count = 0;
//
//    public static void cover(int row, int col, int[][] arr){
//        int coverLength = 0;
//        while (true){
//            boolean canExpand = true;
//            int nr = row+coverLength+1;
//            int nc = col+coverLength+1;
//
//            // 경계를 벗어나면 더 늘릴 수 없으므로 종료
//            if(nr>=10||nc>=10) break;
//
//            for(int i=row; i<=nr; i++){ // 세로줄
//                if(arr[i][nc]!=1) {
//                    canExpand = false;
//                }
//            }
//            for(int i=col; i<=nc; i++){ // 가로줄
//                if(arr[nr][i]!=1) {
//                    canExpand = false;
//                }
//            }
//
//            if(canExpand){
//                coverLength++;
//            }else{ // 0을 만나서 더 늘릴 수 없으면 종료
//                break;
//            }
//
//            // 현재 색종이 길이가 5이면 더 늘릴 수 없으므로 종료
//            if(coverLength==4) break;
//        }
//
//        if(coverLeft[coverLength]==0){
//            count = -1;
//            return;
//        }else{
//            coverLeft[coverLength]-=1;
//        }
//
//        System.out.println(row +","+ col+" -> "+ coverLength);
//        for(int i=0; i<=coverLength; i++){
//            for(int j=0; j<=coverLength; j++){
//                arr[row+i][col+j] = 0;
//            }
//        }
//    }
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        int[][] arr = new int[LENGTH][LENGTH];
//        for(int i=0; i<LENGTH; i++){
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            for(int j=0; j<LENGTH; j++){
//                arr[i][j] = Integer.parseInt(st.nextToken());
//            }
//        }
//
//        for(int i=0; i<LENGTH; i++){
//            for(int j=0; j<LENGTH; j++){
//                if(arr[i][j]==1) {
//                    count++;
//                    cover(i, j, arr);
//
//                    if(count==-1){
//                        System.out.println(-1);
//                        return;
//                    }
//                }
//            }
//        }
//
//        System.out.println(count);
//    }
//}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 색종이 붙이기
 *
 * 1x1~5x5크기까지 5종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
 * 색종이를 크기가 10x10인 종이위에 붙이려고 한다.
 * 종이는 1x1칸으로 나눠져있으며
 * 각 칸에는 0또는 1이 적혀있다.
 *
 * 1이 적힌 칸은 모두 색종이로 덮여져야한다.
 * 색종이를 붙일 때에는 종이의 경계 밖으로 나가서는 안되고, 겹쳐서도 안된다.
 * 0이 적힌 칸에는 색종이가 있으면 안된다.
 *
 */
public class BOJ_17136 {
    static int LENGTH = 10;
    static int[] coverLeft = {5,5,5,5,5};
    static int finalCount = Integer.MAX_VALUE;

    public static void cover(int row, int col, int[][] arr, int count){
        // 현재 사용한 색종이의 양이 이미 다른 경우보다 커지면 조기종료
        if(count>finalCount) return;

        // 마지막 요소에 도착했으면 함수 아예 종료
        if(row==10) {
            finalCount = count; // 여기까지 오면 무조건 색종이 양이 finalCount보다 작은 것이다.
            return;
        }

        // 가려야하는 영역이라면
        if(arr[row][col]==0) {
            if(col==9) cover(row+1, 0, arr, count); // 아랫줄 첫번째로 이동
            else cover(row, col+1, arr, count); //오른쪽으로 이동
            return;
        }

        // 가려야하는 영역이면
        int coverLength = 0; // 현재 위치에서 가릴 수 있는 가장 큰 색종이 크기 구하기
        while (true){
            boolean canExpand = true;
            int nr = row+coverLength+1;
            int nc = col+coverLength+1;

            // 경계를 벗어나면 더 늘릴 수 없으므로 종료
            if(nr>=10||nc>=10) break;

            for(int i=row; i<=nr; i++){ // 세로줄
                if(arr[i][nc]!=1) {
                    canExpand = false;
                }
            }
            for(int i=col; i<=nc; i++){ // 가로줄
                if(arr[nr][i]!=1) {
                    canExpand = false;
                }
            }

            if(canExpand){
                coverLength++;
            }else{ // 0을 만나서 더 늘릴 수 없으면 종료
                break;
            }

            // 현재 색종이 길이가 5이면 더 늘릴 수 없으므로 종료
            if(coverLength==4) break;
        }

        // 가장 큰 색종이부터 1칸 색종이까지 쓰기
        // coverLength=0이면 1칸 색종이 사용
        for(int cl = coverLength; cl>=0; cl--){
            // 색종이 다 썼으면 continue
            if(coverLeft[cl]==0) continue;

            // arr에 표시 (색종이 덮음)
            coverLeft[cl]--;
            //System.out.println(row +","+ col+" -> "+ cl+ "="+ (count+1));
            for(int i=0; i<=cl; i++){
                for(int j=0; j<=cl; j++){
                    arr[row+i][col+j] = 0;
                }
            }

            // 다음 칸으로 재귀
            if(col==9) cover(row+1, 0, arr, count+1); // 아랫줄 첫번째로 이동
            else cover(row, col+1, arr, count+1); //오른쪽으로 이동

            // arr복원
            coverLeft[cl]++;
            for(int i=0; i<=cl; i++){
                for(int j=0; j<=cl; j++){
                    arr[row+i][col+j] = 1;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 배열 입력받기
        int[][] arr = new int[LENGTH][LENGTH];
        for(int i=0; i<LENGTH; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<LENGTH; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 재귀함수
        cover(0, 0, arr, 0);

        if(finalCount>=Integer.MAX_VALUE) finalCount=-1;
        System.out.println(finalCount);
    }
}
