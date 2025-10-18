import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * 평행선
 *
 * 평면에 n개의 점이 있다.
 * 그 중 2개 이상의 점을 지나면서 x축 또는 y축에 평행한 직선이 몇개인지 알아내는 프로그램을 작성하시오.
 *
 * n : 점의 개수
 * 같은 점이 여러번 주어질 수 잇으면 그런 경우 다른 점으로 간주한다.
 */
public class BOJ_2358 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine()); // 1~100000(십만)

        HashMap<Integer, Integer>  xCount = new HashMap<>();
        HashMap<Integer, Integer>  yCount = new HashMap<>();
        for(int i=0; i<num; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if(xCount.containsKey(x)){
                xCount.put(x, xCount.get(x)+1);
            }else {
                xCount.put(x, 1);
            }

            if(yCount.containsKey(y)){
                yCount.put(y, yCount.get(y)+1);
            }else {
                yCount.put(y, 1);
            }
        }

        int lineCount = 0;
        // 세로선 세기
        for(int vertical : xCount.keySet()){
            if(xCount.get(vertical)>1) lineCount++;
        }
        // 가로선 세기
        for(int horizontal : yCount.keySet()){
            if(yCount.get(horizontal)>1) lineCount++;
        }

        System.out.println(lineCount);
    }
}
