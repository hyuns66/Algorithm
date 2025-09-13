import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 시간표
 * 시간표에 좋아하는 과목이 많을 수록 기분이 좋아진다.
 *
 * 시간표 선호도의 기본값은 0
 * 좋아하는 과목이 3교시 이상 연속으로 등장할 경우, 연속으로 등장한 과목의 개수만큼 선호도 증가
 * 싫어하는 과목이 3교시 이상 연속으로 등장할 경우, 연속으로 등장한 과목의 개수만큼 감소
 *
 * 좋아하는 과목과 싫어하는 과목이 주어질 때 동현이의 시간표 선호도는?
 * 과목은 1~M사이의 정수 (M:3~100000=십만)
 */
public class BOJ_33575 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int timeTableLen = Integer.parseInt(st.nextToken());
        int subjectNum = Integer.parseInt(st.nextToken());
        int likeSubjectNum = Integer.parseInt(st.nextToken());
        int hateSubjectNum = Integer.parseInt(st.nextToken());

        // 시간표가 입력됨
        int[] timeTable = new int[timeTableLen];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<timeTableLen; i++){
            timeTable[i] = Integer.parseInt(st.nextToken()); // 1~M까지의 과목들이 입력된다.
        }

        // 과목에 대한 정보 입력 (1: 좋아함/ 0: 무관심 / -1: 싫어함)
        Map<Integer, Integer> subjectInfo = new HashMap();
        for(int i=1; i<=subjectNum; i++){
            subjectInfo.put(i, 0); // 무관심한 과목
        }

        // 좋아하는 과목이 입력됨
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<likeSubjectNum; i++){
            int likeSubject = Integer.parseInt(st.nextToken());
            subjectInfo.put(likeSubject, 1);
        }

        // 싫어하는 과목이 입력됨
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<hateSubjectNum; i++){
            int hateSubject = Integer.parseInt(st.nextToken());
            subjectInfo.put(hateSubject, -1);
        }

        // 시간표에 대한 선호도 계산
        int likeStrike = 0;
        int hateStrike = 0;
        int timeTableScore = 0;
        int prevSubjectInfo = 0;
        for(int i=0; i<timeTableLen; i++){
            int sInfo = subjectInfo.get(timeTable[i]);

            if(prevSubjectInfo==sInfo){ // strike가 올라가는 원소이면
                if(prevSubjectInfo==1){
                    likeStrike++;
                } else if (prevSubjectInfo==-1) {
                    hateStrike++;
                }
            }else{ // 다른 원소가 나왔으면 strike가 끊김
                // 기존 strike들을 시간표 점수에 반영
                if(likeStrike>=3) timeTableScore += likeStrike;
                if(hateStrike>=3) timeTableScore -= hateStrike;
                //System.out.println("timeTableScore:"+timeTableScore);

                // strike 초기화
                likeStrike = 0;
                hateStrike = 0;

                // 현재 원소기준으로 strike 1 수립
                if(sInfo==1){
                    likeStrike=1;
                } else if (sInfo==-1) {
                    hateStrike=1;
                }
            }

            //System.out.println(sInfo+":"+likeStrike+":"+hateStrike);
            // 이전 과목의 info를 현재 과목의 info로 저장후, 반복문 될기
            prevSubjectInfo = sInfo;
        }
        if(likeStrike>=3) timeTableScore += likeStrike;
        if(hateStrike>=3) timeTableScore -= hateStrike;

        System.out.println(timeTableScore);
    }
}
