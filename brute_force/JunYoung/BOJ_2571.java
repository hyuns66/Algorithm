import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

/**
 * 색종이 - 3
 *
 * 가로, 세로의 크기가 각각 100인 흰 도화지가 있다.
 * 여기에 가로 세로 10인 정사각형의 검은 색종이를 붙인다. (도화지변과 평행하도록, 색종이가 도화지 밖으로 나가는 경우는 없다.)
 *
 * 그 후, 검은색 직사각형을 잘라낼 때, 잘라낼 수 있는 검은색 직사각형의 최대 넓이?
 * ---------------------------------------------------------------------
 * [히스토그램 최대 직사각형, 2차원 최대 직사각형 문제]
 * [브루트 포스, 스택, 누적합(근데 이제.. 1인 구간만 누적하는...)]
 * [어려웠다.. 굉장히....]
 */
public class BOJ_2571 {

    static int getMaxArea(int[] h){
        Stack<Integer> stack = new Stack<>(); // 왼쪽에서 나보다 작은 첫 위치를 기억하기 위해 사용
        int maxArea = 0;

        // 왜 x가 101일때까지 도는거지??
        for(int x=0; x<=h.length; x++){
            int curHeight = (x==h.length)? 0: h[x]; // 같은 높이는 stack에 쌓아뒀다가 마지막에 curHeight가 0이 되는 순간에 계산

            // 지금 스택 첫번째 원소보다 작은 높이가 등장한다면,
            // 해당 높이보다 큰 애들을 다 뺀다. (이제 오른쪽으로 더 확장할 수 없기 때문)
            // >=를 하지 않는건 덩어리 유지.. 라고 생각하면 편하다.
            while (!stack.isEmpty() && h[stack.peek()] > curHeight){
                int height = h[stack.pop()];
                int width;

                if (stack.isEmpty()) {
                    width = x;
                } else {
                    width = x - stack.peek() - 1;
                }

                maxArea = Math.max(maxArea, height * width);
            }

            stack.push(x);
        }

        return maxArea;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int blackNum = Integer.parseInt(br.readLine()); // 1~100


        // 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지에
        // 검정 색종이가 붙으면 1로 표시하기 (색종이의 왼쪽 아래 좌표가 주어지고, 10x10의 정사각형)
        StringTokenizer st;
        int[][] map = new int[100][100];
        for(int s=0; s<blackNum; s++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for (int i = y; i < y + 10; i++) {
                for (int j = x; j < x + 10; j++) {
                    map[i][j] = 1;
                }
            }
        }

        int[] height = new int[100]; // height[i]: 해당 행의 i열에 대한 높이
        int max = 0;

        // 0~99행까지 각 행을 바닥으로 보면서
        for(int y=0; y<100; y++){
            // height 갱신
            for(int x=0; x<100; x++){
                if(map[y][x] == 1) height[x]++;
                else height[x] = 0;
            }

            // 히스토그램 최대 직사각형
            max = Math.max(max, getMaxArea(height));
        }

        System.out.println(max);
    }

}
