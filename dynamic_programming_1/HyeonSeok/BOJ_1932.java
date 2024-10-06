import java.io.*;
import java.util.*;

public class 정수_삼각형 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        List<int[]> tree = new ArrayList<>();  // 가변 길이 배열을 위해 List 사용
        List<int[]> dp = new ArrayList<>();
        for (int n = 0; n < N; n++){
            String input = br.readLine();
            int[] row = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
            tree.add(row);
            int[] zeros = new int[n+1];
            dp.add(zeros);
        }
        int answer = tree.get(0)[0];;
        dp.get(0)[0] = answer;
        for (int n=1; n<N; n++){
            for (int i=0; i<n+1; i++){
                int max = 0;
                if (i > 0 && i < n){
                    max = Math.max(dp.get(n-1)[i-1], dp.get(n-1)[i]);
                } else if (i <= 0){
                    max = dp.get(n-1)[i];
                } else if (i >= n){
                    max = dp.get(n-1)[i-1];
                }
                dp.get(n)[i] = max + tree.get(n)[i];
                answer = Math.max(answer, dp.get(n)[i]);
            }
        }
        // for (int n=0; n<N; n++){
        //     for (int i=0; i<n+1; i++){
        //         System.out.print(String.format("%d ", dp.get(n)[i]));
        //     }
        //     System.out.println();
        // } 
        System.out.println(answer);
    }
}

