import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * 친구
 *
 * 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다.
 *
 * [가장 유명한 사람을 구하는 방법]
 * 각 사람의 2-친구를 구하면 된다.
 * - 두 사람이 친구거나,
 * - A와 친구이고 B와 친구인 C가 존재해야한다.
 *
 * 2-친구의 수가 가장 많은 사람이 가장 유명한 사람이다.
 * -> 가장 유명한 사람의 2-친구수는?
 *
 * ================================================
 * 접근 = "친구도 내친구, 친구의 친구도 내 친구!"
 * (나는 셋을 이용해서 풀었다.)
 */
public class BOJ_1058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int peopleNum = Integer.parseInt(br.readLine()); // 1~50

        boolean[][] relationship = new boolean[peopleNum][peopleNum]; // 인접행렬
        for(int i=0; i<peopleNum; i++){
            String line = br.readLine();
            for(int j=0; j<peopleNum; j++){
                if(line.charAt(j)=='N'){
                    relationship[i][j] = false;
                }else{
                    relationship[i][j] = true;
                }
            }
        }

        int maxPopular = 0;
        for(int i=0; i<peopleNum; i++){
            Set<Integer> friendsOfI = new HashSet<>();
            for(int j=0; j<peopleNum; j++){
                if (relationship[i][j]) {
                    // 친구를 리스트에 넣기
                    friendsOfI.add(j);

                    // 친구의 친구를 리스트에 넣기
                    for(int s=0; s<peopleNum; s++){
                        if(s==i) continue; // 친구의 친구가 나라면 skip
                        if(relationship[j][s]){
                            friendsOfI.add(s);
                        }
                    }
                }
            }
            //System.out.println(friendsOfI);
            maxPopular = Math.max(maxPopular, friendsOfI.size());
        }

        System.out.println(maxPopular);
    }
}
