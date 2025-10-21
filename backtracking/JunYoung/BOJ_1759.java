import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 암호 만들기
 *
 * 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며,
 * 최소 한개의 모음(a,e,i,o,u)과
 * 최소 2개의 자음으로 구성되어있다고 알려져있다.
 * 또한 암호는 정렬된 문자열일 것이다.
 *
 * 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지 존재
 * C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하시오
 * ------------------------------------------------------------
 * 단순 조합 + 조기종료 = 백트래킹
 * String.indexOf(c) >= 0 로 String안에 c가 있는지 체크가능함
 */
public class BOJ_1759 {
    static char[] candidate;
    static String moum = "aeiou";

    static void comb(int index, String password, int moumCount, int jaumCount, int passwordLen){
        if(password.length()==passwordLen){ // 패스워드 수를 다채웠다면
            if(moumCount>=1 && jaumCount>=2){
                System.out.println(password);
            }
            return; // 종료
        }

        if(index>=candidate.length){
            return; // 가능한 인덱스 범위를 넘어가면 종료
        }

        char c = candidate[index];

        int newMoumCount = moumCount;
        int newJaumCount = jaumCount;
        if(moum.indexOf(c) >= 0){
            newMoumCount++;
        }else{
            newJaumCount++;
        }

        // 현재 문자를 포함한 경우
        comb(index+1, password+c, newMoumCount, newJaumCount, passwordLen);
        // 현재 문자를 포함하지 않은 경우
        comb(index+1, password, moumCount, jaumCount, passwordLen);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 3 <= passwordLen <= candidateNum <= 15
        int passwordLen = Integer.parseInt(st.nextToken());
        int candidateNum = Integer.parseInt(st.nextToken());

        candidate = new char[candidateNum];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<candidateNum; i++){
            candidate[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(candidate);  // 정렬

        comb(0, "", 0, 0, passwordLen);

    }
}
