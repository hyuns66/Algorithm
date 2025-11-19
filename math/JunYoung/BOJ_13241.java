import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 최소공배수
 *
 * 정수 B에, 0보다 큰 정수인 N을 곱해 A를 만들 수 있다면, A는 B의 배수이다.
 * 두 수 A,B에 대해서 최소 공배수를 구해보자.
 * 유클리드 호제법
 */
public class BOJ_13241 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        // 유클리드 호제법으로 gcd(최대 공약수) 구하기
        long a = A;
        long b = B;
        long temp;
        while (b!=0){
            temp = a%b;
            a= b; // a가 무조건 더 큰수로 변한다.
            b= temp; // b는 a를 b로 나눈 나머지로 갱신
        }
        // b==0이 될 때 종료되기 때문에 a가 최대공약수

        // 최소공배수 = 두수의 곱 / 최대공약수
        System.out.println(A*B/a);
    }
}
