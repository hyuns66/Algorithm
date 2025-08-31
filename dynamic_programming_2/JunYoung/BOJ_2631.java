import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 줄 세우기
 *
 * KOI 어린이집에는 N명의 아이들이 있다.
 * 1~N번까지의 번호표를 가슴에 붙여주었다.
 *
 * 일렬로 서서 걸어가는 도중, 번호가 바뀌었다.
 * 다시 번호대로 줄을 세울껀데, 혼란스러워하지 않도록 위치를 옮기는 아이들의 수를 최소로 하려고한다.
 *
 */
public class BOJ_2631 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    int[] arr = new int[N];
    for(int i=0; i<N; i++){
      arr[i] = Integer.parseInt(br.readLine());
    }

    int[] LIS = new int[N];
    for(int i=0; i<N; i++){
      LIS[i] = 1;
    }

    for(int i=1; i<N; i++){
      for(int j=0; j<i; j++){
        if(arr[j]<arr[i]) LIS[i] = Math.max(LIS[i], LIS[j]+1);
      }
    }

    int maxLIS = -1;
    for(int i=0; i<N; i++){
      //System.out.print(LIS[i]+" ");
      maxLIS = Math.max(maxLIS, LIS[i]);
    }
    //System.out.println();
    //System.out.println(maxLIS);

    System.out.println(N-maxLIS);
  }
}