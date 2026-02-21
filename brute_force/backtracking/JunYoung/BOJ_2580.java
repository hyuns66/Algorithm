import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 스도쿠
 *
 * 가로 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 판이다.
 *  스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.
 *
 */
public class BOJ_2580 {
    static class Pos{
        int row;
        int col;

        Pos(int row, int col){
            this.row = row;
            this.col = col;
        }

        @Override
        public String toString(){
            return row+":"+col;
        }
    }

    static int LEN = 9;

    static Set<Integer> checkRow(int[][] arr, int rowIndex){
        Set<Integer> canPlace = new HashSet<>();

        boolean[] used = new boolean[10];
        for(int i=0; i<LEN; i++){
            int value = arr[rowIndex][i];
            used[value] = true; // 해당 숫자의 사용 기록
        }
        for(int i=1; i<10; i++){
            if(!used[i]) canPlace.add(i);
        }

        return canPlace;
    }


    static Set<Integer> checkCol(int[][] arr, int colIndex){
        Set<Integer> canPlace = new HashSet<>();

        boolean[] used = new boolean[10];
        for(int i=0; i<LEN; i++){
            int value = arr[i][colIndex];
            used[value] = true; // 해당 숫자의 사용 기록
        }
        for(int i=1; i<10; i++){
            if(!used[i]) canPlace.add(i);
        }

        return canPlace;
    }

    static Set<Integer> checkSquare(int[][] arr, int rowIndex, int colIndex){
        Set<Integer> canPlace = new HashSet<>();

        int minRow = rowIndex/3;
        int minCol = colIndex/3;
        //System.out.println(3*minRow+minCol+" 번째 삼각형");

        boolean[] used = new boolean[10];
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                int value = arr[3*minRow+i][3*minCol+j];
                used[value] = true; // 해당 숫자의 사용 기록
            }
        }

        for(int i=1; i<10; i++){
            if(!used[i]) canPlace.add(i);
        }

        return canPlace;
    }

    static Set<Integer> findPossible(int[][] arr, Pos point){
        Set<Integer> p1 = checkRow(arr, point.row);
        Set<Integer> p2 = checkCol(arr, point.col);
        Set<Integer> p3 = checkSquare(arr, point.row, point.col);

//        System.out.println("p1"+p1);
//        System.out.println("p2"+p2);
//        System.out.println("p3"+p3);
        // Union = 합집합 = addAll()
        // Intersection = 교집합 = retainAll()
        p1.retainAll(p2);
        p1.retainAll(p3);
        return p1;
    }

    static void print(int[][] arr){
        for(int i=0; i< arr.length; i++){
            for(int j=0; j< arr.length; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }

    static boolean fill(int[][] arr, List<Pos> needToFill, int fillIndex){
        if(fillIndex==needToFill.size()){
            // System.out.println(fillIndex);
            // 다 채움.
            print(arr);
            return true;
        }

        Pos curPos = needToFill.get(fillIndex);
        Set<Integer> possibleValue = findPossible(arr, curPos);
        //System.out.println(fillIndex);

        //System.out.println("possibleValue"+possibleValue);
        for(int v: possibleValue){
            arr[curPos.row][curPos.col] = v;
            //System.out.println(v+"후보지");
            boolean result = fill(arr, needToFill, fillIndex+1);
            if(result) return true;
            arr[curPos.row][curPos.col] = 0;
        }

        return false;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] arr = new int[LEN][LEN]; // 스토쿠판
        List<Pos> needToFill = new ArrayList<>(); // 채워야할 빈칸
        for(int r=0; r<LEN; r++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int c=0; c<LEN; c++){
                int value = Integer.parseInt(st.nextToken());
                arr[r][c] = value;
                if(value==0){
                    needToFill.add(new Pos(r,c));
                }
            }
        }

        //System.out.println(needToFill);

        // 채워야할 빈칸이 없을 때까지
        fill(arr, needToFill, 0);

    }
}
