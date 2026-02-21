import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// gcd(x,y) = a이고, x+y=b인 자연수쌍(x,y)가 존재하는가??
public class BOJ_25375 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int query = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for(int q=0; q<query; q++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            // a,b  = 1~10^18(100경)
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            // gcd(x,y) = a / gcd : 최대공약수
            // => x와, y는 a의 배수여야한다.
            // x+y=b
            // => a 의 배수 + a의 배수 = b
            // => b 또한 a의 배수이다.

            // x = a, y = b-a로 골랐을때
            // b가 a보다 큰 a의 배수이기만 하면 된다.

            if(b%a==0 && a<b) sb.append(1).append("\n");
            else sb.append(0).append("\n");
        }

        System.out.println(sb.toString());
    }
}
