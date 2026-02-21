import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * 소가 길을 건너간 이유2
 * ---------------------
 * 왕 꽤 복잡했지만 생각해내서 했다!!
 * Map의 getOrDefault는 java8에선 안돌아간다..!
 *
 * 소의 입구~출구까지에 있는 다른 소들의 입구출구중에서 짝이 맞지 않는 즉, 홀수개인 입구출구의 수를 세면
 * 해당 수 만큼의 경로가 내 경로랑 겹치는 것이다.
 * -> 카운트 해주고, 서로 양쪽에서 겹치는걸 중복해서 카운트 했으니까 /2로 해주기
 */
public class BOJ_14468 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine().strip();

        boolean[] checked = new boolean[26];
        int count = 0;
        for(int i=0; i<line.length()-1; i++){
            char c = line.charAt(i);
            int cIndex = c-'A';
            if(checked[cIndex]) continue;

            // 체크하지 않은 소였을 경우
            Map<Character, Boolean> isExist = new HashMap<>();
            for(int j=i+1; j<line.length(); j++){
                char mid = line.charAt(j);
                if(mid==c) break;
                // 현재소의 출구~현재소의 입구
                if(isExist.getOrDefault(mid, false)){
                    count--;
                }else{
                    count++;
                }
                isExist.put(mid, true); // 지금 mid를 지났으니까 맵에 표시하기
            }

            checked[cIndex] = true;
        }
        System.out.println(count/2); // 양쪽에서 count해서 중복이 들어갔을 것이므로 /2
    }
}
