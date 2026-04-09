import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 근로장학생
 *
 * [문자열, 자료구조(맵, 정렬)]
 */
public class BOJ_31824 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 정보의 개수(1~1000)
        int M = Integer.parseInt(st.nextToken()); // 문장의 개수(1~10)

        // 해당 알파벳으로 시작하는 Q 단어.
        ArrayList<String>[] startsWord = new ArrayList[27];
        for(int i=0; i<27; i++){
            startsWord[i] = new ArrayList<>();
        }

        // Q단어에 매핑되는 A 단어.
        Map<String, String> QtoA = new HashMap<>();

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            String Q = st.nextToken(); // 길이는 1~10
            String A = st.nextToken(); // 길이는 1~10
            int index = Q.charAt(0)-'A';
            startsWord[index].add(Q);
            QtoA.put(Q, A);
        }


        StringBuilder sb = new StringBuilder();
        for(int t=0; t<M; t++){ // 각 문장에 대해서
            String S = br.readLine();
            boolean isNoAnswer = true;
            for(int i=0; i<S.length(); i++){ // 문장의 각 char=알파벳에 대해서
                int cIndex= S.charAt(i)-'A';
                if(!startsWord[cIndex].isEmpty()){ // 해당 알파벳으로 시작하는 단어가 있다면
                    Collections.sort(startsWord[cIndex]);
                    for(String sWord: startsWord[cIndex]){
                        //
                        boolean isMatch = true;
                        if(i+sWord.length()-1>=S.length()){ // StringIndexOutOfBounds를 막기 위함
                            isMatch = false;
                        }else{ // 문자열을 비교할 길이가 되는 경우에만 비교 수행
                            for(int j=1; j<sWord.length(); j++) {
                                if(S.charAt(i+j) != sWord.charAt(j)) { // i+j가 범위를 넘거나
                                    isMatch = false;
                                    break;
                                }
                            }
                        }


                        if(isMatch) {
                            sb.append(QtoA.get(sWord));
                            isNoAnswer = false;
                        }
                    }
                }
            }

            if(isNoAnswer){
                sb.append("-1");
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
