import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 샤워실 바닥 깔기
 *
 * 샤워실의 구조 = 정사각형이면서, 한변의 길이가 2의 제곱수이다.
 * 준서는 2x2로만 바닥을 채워 -> 배수구 위치를 만들지 못했다.
 *
 * 4칸을 차지하는 정사각형 타일 대신, 3칸의 ㄱ자 모양타일을 이용해 채워보자
 */
public class BOJ_14600 {
    static int[][] arr;
    static int index = 1;
    static int maxIndex = 5;

    public static void mark(int startY, int endY, int startX, int endX, int holeY, int holeX, int min, int max){
        int length = endX-startX+1;
        int halfLength = length/2;
        if(length==2){
            if(startX<=holeX&&holeX<=endX&&startY<=holeY&&holeY<=endY){
                // 하수구를 포함한 2x2의 정사각형의 경우
                for(int i=0; i<2; i++){
                    for(int j=0; j<2; j++){
                        // 안쪽을 비워두기
                        if(arr[startY+i][startX+j]==-1) continue;
                        arr[startY+i][startX+j] = index;
                    }
                }
            }else{
                for(int i=0; i<2; i++){
                    for(int j=0; j<2; j++){
                        // 안쪽을 비워두기
                        if(startY+i!=min&&startY+i!=max&&startX+j!=min&&startX+j!=max) arr[startY+i][startX+j] = maxIndex;
                        else arr[startY+i][startX+j] = index;
                    }
                }
            }
            index++;
        }else{
            mark(startY, startY+halfLength-1, startX, startX+halfLength-1, holeY, holeX, min, max);
            mark(startY+halfLength, endY, startX, startX+halfLength-1, holeY, holeX, min, max);
            mark(startY, startY+halfLength-1,startX+halfLength, endX, holeY, holeX, min, max);
            mark(startY+halfLength, endY, startX+halfLength, endX, holeY, holeX, min, max);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 바닥 한 변의 길이 (1~2)
        int k = Integer.parseInt(br.readLine());
        int length = (int) Math.pow(2,k);

        // 배수구의 위치 (왼쪽 아래 1,1 - 오른쪽 위 2^k, 2^k)
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        //
        arr = new int[length][length];
        arr[length-y][x-1] = -1;
        mark(0,length-1,0,length-1, length-y, x-1, 0, length-1);

        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr.length; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
