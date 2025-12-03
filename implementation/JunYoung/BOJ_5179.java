import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 우승자는 누구?
 * 문제를 맞힐 경우, 맞힌 사람은 총점에 문제를 맞힌 시각 + 그 문제를 틀린 횟수*20만큼을 더하게 된다.
 * 만일 동일한 문제를 두 번 이상 맞히더라도 처음 맞힌 것만 인정된다.
 *
 * 순위
 * - 푼 문제수 순
 * - 총점 낮은 순
 *
 * 놓친 케이스
 * - false로 들어와도, 이미 맞춘 문제일 수 있다.
 * - 마지막에 pq에 넣을 때 한번이라도 문제를 맞춘 애들만 넣어서, 점수가 0인 애들이 출력 안되는 문제가 있었다.
 */
public class BOJ_5179 {
    static class Node implements Comparable<Node>{
        int id;
        int num;
        long score;

        Node(int num, long score){
            this.id = 0;
            this.num = num;
            this.score = score;
        }

        @Override
        public int compareTo(Node o){
            if(this.num==o.num){
                return Long.compare(this.score, o.score); // 점수 낮은게 순위 높다.
            }else{
                return Integer.compare(o.num, this.num); // 맞춘 수가 높은게 순위 높다.
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcNum = Integer.parseInt(br.readLine());
        for(int tc=0; tc<tcNum; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken()); // 대회에 사용된 문제의 개수 (1~10)
            int n = Integer.parseInt(st.nextToken()); // 총 제출 수 (1~5000)
            int p = Integer.parseInt(st.nextToken()); // 참가자의 수 (1~500)

            Map<Integer, Node> scoreMap = new HashMap<>();
            Map<Integer, Integer[]> failCount = new HashMap<>();
            for(int i=1; i<=p; i++){
                Integer[] integerArray = new Integer[m];
                Arrays.fill(integerArray, 0);
                failCount.put(i, integerArray);
            }

            // 제출 기록을 순회
            for(int i=0; i<n; i++){
                st = new StringTokenizer(br.readLine());
                int participant = Integer.parseInt(st.nextToken());
                int problemNumber = st.nextToken().charAt(0)-'A';
                int submitTime = Integer.parseInt(st.nextToken());
                boolean isCorrect = Integer.parseInt(st.nextToken()) == 1;

                if(isCorrect){
                    Integer[] fcList = failCount.get(participant);
                    if(fcList[problemNumber]==-1) continue; // 동일문제를 두번 이상 맞힌 경우 무시

                    // 처음으로 맞춘 경우
                    long addScore = submitTime + fcList[problemNumber]* 20L;
                    Node pNode = scoreMap.getOrDefault(participant, new Node(0,0L));
                    pNode.score += addScore;
                    pNode.num += 1;
                    scoreMap.put(participant, pNode);
                    //System.out.println(pNode.num+" "+pNode.score);
                    fcList[problemNumber] = -1;
                }else{
                    Integer[] fcList = failCount.get(participant);
                    if(fcList[problemNumber]==-1) continue; // 동일문제를 이미 맞힌 경우 무시
                    fcList[problemNumber] += 1;
                }
            }

            sb.append("Data Set ").append(tc+1).append(":\n");
            PriorityQueue<Node> pq = new PriorityQueue<>();
            for(int people=1; people<=p; people++){
                Node node = scoreMap.getOrDefault(people, new Node(0, 0L));
                node.id = people;
                pq.add(node);
            }

            while (!pq.isEmpty()){
                // 참가자들의 아이디, 푼 문제 수, 총점
                Node node = pq.poll();
                sb.append(node.id).append(" ").append(node.num).append(" ").append(node.score).append("\n");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
