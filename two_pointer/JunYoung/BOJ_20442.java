import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * ㅋㅋ루ㅋㅋ
 *
 * 1. R로만 이루어진 문자열은 ㅋㅋ루ㅋㅋ 문자열이다. (단, 빈 문자열은 ㅋㅋ루ㅋㅋ이 아니다.)
 * 2. ㅋㅋ루ㅋㅋ 문자열 양 끝에 K를 하나씩 붙인 문자열은 ㅋㅋ루ㅋㅋ 문자열이다.
 * 
 * [누적합, 투포인터]
 * [예외체크: KK사이에 R이 없는 경우는 정답 계산하면 안됨]
 */
public class BOJ_20442 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine(); // K와 R로만 이루어져있음. 문자열의 최대길이는 3,000,000(삼백만)

        // 1. R의 누적합 구하기
        int sum = 0;
        int[] prefixSum = new int[s.length()];
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='R'){
                sum++;
            }
            prefixSum[i] = sum;
        }

        // 2. 투포인터로 돌면서 left, right모두 k인 구간에 정지해서 그 사이 r값을 더해서 정답 갱신
        int answer = sum;
        int kSum = 0;
        int left = 0;
        int right = s.length()-1;
        while (left<right){
            if (s.charAt(left)!='K'){
                left++;
                continue;
            }else if(s.charAt(right)!='K'){
                right--;
                continue;
            }

            // 둘 다 k이라면
            kSum++;
            int RSum = prefixSum[right]-prefixSum[left];
            if(RSum !=0){
                answer = Math.max(answer, 2*kSum+RSum);
            }

            // 범위 조여오기
            left++;
            right--;
        }

        System.out.print(answer);
    }
}
