import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 반례 : 1 -1 2
public class BOJ_14913 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken()); // -1000<a<1000
        int d = Integer.parseInt(st.nextToken()); // -1000<d<1000 d!=0
        int k = Integer.parseInt(st.nextToken()); // -1,000,000<k<1,000,000

        // k가 몇번째 항인지 출력하시오
        // 만약 k가 a와 d로 만들어진 등차수열의 수가 아니라면 X를 출력하시오

        int gap = k-a; // gap은 첫항에서 부터 찾는수 사이의 거리(증가하는 수열이면 양수/ 감소하는 수열이면 음수)
        if(gap%d!=0) System.out.println("X");
        else if(gap<0 ^ d<0){ // 공차의 부호와 gap의 부호가 같아야한다. XOR은 두 같이 다를때만 true를 출력한다.
            System.out.println("X");
        }else{
            int index = gap/d;
            System.out.println(index+1);
        }
    }
}
