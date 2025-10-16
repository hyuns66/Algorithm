import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/**
 * 카드 뒤집기
 * 1~N까지 서로 다른 정수가 적혀있는 카드를 N장 가지고 있다.
 * 각 카드에는 앞면과 뒷면이 존재한다. (앞면 = 숫자, 뒷면 = 무늬)
 *
 * 우선, 앞면이 보이도록 일렬로 배열한다
 * 1. 맨먼저 한장의 카드를 골라 뒷면으로 뒤집는다.
 * 2. 가장 마지막으로 뒤집은 카드에 적힌 번호를 x라 하자. 뒤집은 카드 왼쪽/또는 오른쪽으로 x장 떨어진 앞면카드를 뒤집는다. 해당하는 카드가 없으면 종료한다.
 * 3. 2번 단계가 종료될 때까지 뒤집는 과정을 반복한다.
 *
 * 카드의 장수 N이 주어질 때, 모든 카드를 뒤집을 수 있도록 배열할 수 있는지 알고싶다.
 * 모든 카드를 뒤집을 수 있는 배치가 존재하는지? 만약 가능하다면 YES, 불가능하다면 NO를 출력
 * 존재하다면 카드를 배열하는 방법과 뒤집는 순서를 출력하시오
 *
 * ==================================================
 * 규칙을 찾아내는 것이 중요한 문제다..!! 거의 전부
 */
public class BOJ_27920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 1~200,000(이십만)

        int[] arr = new int[N];
        int[] pos = new int[N];
        
        // 규칙: N-1부터 1까지 좌우 왔다갔다하며 끝에서부터 채워나가기, 마지막 남는 자리에 N
        int num = N-1;
        int left = 0;
        int right = N-1;
        boolean isLeft = true;
        int count = 0;
        while (num>=1){
            if(isLeft) {
                arr[left] = num;
                pos[count] = left+1;
                left++;
            }else{
                arr[right] = num;
                pos[count] = right+1;
                right--;
            }
            num--;
            count++;
            isLeft = !isLeft;
        }

        if(isLeft) {
            arr[left] = N;
            pos[count] = left+1;
        }else{
            arr[right] = N;
            pos[count] = right+1;
        }

        System.out.println("YES");
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < N; i++) {
            System.out.print(pos[i] + " ");
        }
        System.out.println();
    }
}
