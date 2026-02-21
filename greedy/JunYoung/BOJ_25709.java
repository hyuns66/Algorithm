import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1 빼기
 * = 다음의 두 연산 중 하나를 골라 수행할 수 있다.
 * 1) 가지고 있는 수에서 1을 뺀다.
 * 2) 가지고 있는 수에 있는 1을 하나 지운다. 지우고 난뒤 좌우의 수를 합쳐 하나의 수로 만든다. (맨앞의 연속되는 0은 지워진다.)\
 *
 * 처음 있었던 수에서 이 수를 0으로 만들기 위해 최소 몇번의 1빼기 필요한가?
 *
 * ex) 506: 506 505 504 503 502 501 50 / 49 48 47 46 45 44 43 42 41 4 3 2 1 0
 * 70107 -> 70106, 70105, 70104, 70103, 70102, 70101, 7010, 70,69, 68, 67, 66, 65, 64, 63, 62, 61, 6, 5, 4, 3, 2, 1, 0
 * 699 691 69
 */
public class BOJ_25709 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 1~1,000,000,000 (10억)

        int count = 0;
        while (N!=0){
            //System.out.println(N);
            if(N%10==0){
                int tmp = N;
                // 0이 아닌 무언가가 나오는 부분을 찾기
                int back = 1;
                while(tmp%10==0){
                    tmp /= 10;
                    back *= 10;
                }
                int digit = tmp%10;

                // 0이 아닌 무언가가 1이 아니라면
                // 500 499 498 497 491 490
                if(digit!=1){
                    //System.out.println("10 더해짐");
                    count+=10;
                    N=N/10-1;
                }
                if(digit==1){
                    //System.out.println("1 더해짐");
                    int removedOneNumber = tmp/10 * back;
                    count+=1;
                    N=removedOneNumber;
                }
            }else{
                //System.out.println(N%10+" 더해짐");
                count+=N%10;
                N=N/10;
            }
        }

        System.out.println(count);
    }
}
