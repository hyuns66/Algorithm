import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 좋은 수열
 *
 * 인접한 두개의 부분 수열이 동일한 것이 있으면 나쁜 수열
 * ----------------------------------------------
 * 풀이 보고 풀었땅..
 * 백트래킹 중에 답을 찾았다면 종료를 지금 방식대로 하는 방법밖엔 없나.. dfs 함수가 boolean을 반환하게 할 수 있다.
 * 그리고 만약 내부 재귀가 true를 반환했으면 외부 재귀도 true를 반환
 */
public class BOJ_2661 {
    static boolean find = false;

    static void dfs(String str){

        int len = str.length();
        if(!find&&len==n) {
            find = true;
            System.out.println(str);
            return;
        }

        char init = '0';
        for(int i=1; i<=3; i++){
            char add = (char) (init+i);
            String addString = str+add;
            int addLen = len+1;

            //System.out.println("addString="+addString);
            boolean isBad = false;
            for(int size=1; size<=addLen/2; size++){
                String strA = addString.substring(addLen-size);
                String strB = addString.substring(addLen-size*2, addLen-size);
                //System.out.println(strA+":"+strB);
                if(strA.equals(strB)){
                    isBad = true;
                    break;
                }
            }
            if(isBad) continue;

            dfs(str+add);
            if(find) return; // 위에서 찾았으면 다음단계는 하지 않아도 된다.
        }
    }

    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        dfs("1"); // 123212321... 하면 무한대로 늘어날 수 있다.
    }
}
