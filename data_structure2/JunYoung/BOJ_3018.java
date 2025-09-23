import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 캠프파이어
 *
 * 매일밤, 1번(선영)이가 캠프파이어에 참가한다면 나머지 사람들이 모르는 새로운 노래를 즉석에서 만들어 부른다.
 * 1번 선영이가 참여하지 않은 날은 사람들이 각자 아는 노래를 공유한다.
 * 매일 캠프파이어에 참가하는 사람이 주어졌을 때, 모든 노래를 알게 되는 사람이 누구인가?
 */
public class BOJ_3018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int peopleNum = Integer.parseInt(br.readLine()); // 1~100
        Map<Integer, List<Integer>> knowingSong = new HashMap<>();
        for(int i=1; i<=peopleNum; i++){
            knowingSong.put(i, new ArrayList<>());
        }


        int day = Integer.parseInt(br.readLine()); // 1~50
        int currentSongNum = 0;
        for(int i=0; i<day; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int participantsNum = Integer.parseInt(st.nextToken());

            // 참가자
            List<Integer> participants = new ArrayList<>();
            Set<Integer> songsUnion = new HashSet<>();

            boolean isMakingDay = false;
            for(int j=0; j<participantsNum; j++){
                int p = Integer.parseInt(st.nextToken());
                participants.add(p);
                songsUnion.addAll(knowingSong.get(p));
                if(p==1) isMakingDay=true;
            }

            if(isMakingDay){
                currentSongNum++;
                for(int s=0; s<participantsNum; s++){
                    int p = participants.get(s);
                    List<Integer> ks = knowingSong.get(p);
                    ks.add(currentSongNum);
                    //knowingSong.put(p, ks);
                }
            }else{ //노래 공유데이
                for(int s=0; s<participantsNum; s++){
                    int p = participants.get(s);
                    knowingSong.put(p, new ArrayList<>(songsUnion));
                }
            }
        }

        // 캠프파이어가 끝난 뒤
        for(int i=1; i<=peopleNum; i++){
            List<Integer> ks = knowingSong.get(i);
            //System.out.println(i+"번 사람이 아는 노래 수 :"+ ks.size());
            if (ks.size()==currentSongNum) System.out.println(i);
        }

    }
}
