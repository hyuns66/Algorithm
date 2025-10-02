import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 사이클 게임
 *
 * 두명의 플레이어가 차례대로 돌아가며 진행하는 게임
 * 선 플레이어 - 후플레이어 반복
 *
 * 게임 시작 시, 0~n-1까지 고유한 번호가 부여된 평면 상의 점n개가 주어진다.
 * 이 중 어느 세점도 일직선 위에 놓이지 않는다.
 *
 * [매 차례]
 * - 두점을 선택해서 선분을 긋는다.
 *  (이전에 그린 선분을 다시 그을 수는 없지만, 교차하는 것은 가능하다.)
 * - 처음으로 사이클을 완성하는 순간 게임이 종료된다.
 *  (임의의 선분의 한끝점에서 시작해서 모든 선분을 한번씩만 지나서 출발점으로 돌아올 수 있다.)
 *
 * 게임의 진행 상황이 주어지면, 몇번째 차례에서 사이클이 완성되었는지
 * 혹은 아직 게임이 진행중인지 판단하는 프로그램을 작성해주세요!
 *
 * ----------------------------------------------------
 * 접근 1) = 유니온 파인드
 * - int[] parent
 *
 */
public class BOJ_20040 {

    static int[] parents;

    public static boolean union(int pointA, int pointB){
        int parentA = find(pointA);
        int parentB = find(pointB);

        if(parentA==parentB) return false; // 같은 그룹이라 union 할 필요 없음

        // [rank를 이용한 최적화]
        if(parents[parentA] <parents[parentB]) {// A의 랭크가 더 큰 경우
            parents[parentB] = parentA; // B루트를 A루트의 자식으로 둔다
        }else if(parents[parentA]>parents[parentB]){ // B랭크가 더 큰경우
            parents[parentA] = parentB; // A 그룹의 루트를 B 그룹의 루트 아래에 두기
        }else{
            parents[parentA]-=1;
            parents[parentB] = parentA; // B루트를 A루트의 자식으로 둔다
        }
        return true;
    }

    // find의 시간복잡도가 중요하다 최악의 경우 : O(N)
    public static int find(int point){

        if(parents[point] < 0) { // 루트 노드의 경우 반환
            return point;
        }

        // 루트노드가 아니면 부모의 부모찾기
        // [경로 압축을 이용한 최적화] = 내 부모의 부모를 내 부모로 만들기
        return parents[point] = find(parents[point]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int pointNum = Integer.parseInt(st.nextToken()); // 3~500,000(오십만)
        int turnNum = Integer.parseInt(st.nextToken()); // 3~1,000,000(백만)

        parents = new int[pointNum];
        for(int i=0; i<pointNum; i++){
            parents[i] = -1;
        }

        int answer = 0;
        for(int turn=1; turn<=turnNum; turn++){
            st = new StringTokenizer(br.readLine());
            int pointA = Integer.parseInt(st.nextToken());
            int pointB = Integer.parseInt(st.nextToken());
            boolean canUnion = union(pointA, pointB);
            if(!canUnion) {
                answer = turn;
                break; // 처음 사이클이 생겼을 때 종료해줘야한다!
            }
        }

        System.out.println(answer);
    }
}
