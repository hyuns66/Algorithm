import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * ACM Craft
 *
 * 최백준은 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다.
 * 매 게임마다 특정 건물을 짓기 위한 순서가 달라진다.
 *
 * 특정 건물을 가장 빨리 지을 때까지 걸리는 최소시간?
 *
 * 1. Map<건물번호, List<인접건물번호>>
 * 2. inOrder가 0인것부터 시작, 큐에 <건물 번호, 건설 완료 시간> 넣기, 큐가 빌때까지 반복
 * 3. 큐에서 건물을 뽑아, 인접한 건물의 inOrder를 빼주고
 * 4. 인접 건물의 inOrder가 0이 되었다면 큐에 <인접건물, 현재 시간+ 인접건물의 건설 완료 시간>넣기
 *    큐는 우선순위 큐로, time오름차순으로 정렬해서, inOrder가 0이 될땐, 오래 걸리는 애 기준으로 적용할 수 있게해준다.
 */
public class BOJ_1005 {
    static class Building implements Comparable<Building>{
        int num;
        int time;

        Building(int num, int time){
            this.num = num;
            this.time = time;
        }

        public int compareTo(Building o){
            return Integer.compare(this.time, o.time);
        }

        @Override
        public String toString(){
            return "("+this.num+","+this.time+")";
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        // 10만초 * 노드수(1000) = 10000만초 = 만만 = 1억초 (answer는 int로 커버가능)
        for(int tc=0; tc<testCase; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int buildingNum = Integer.parseInt(st.nextToken()); //2~1000
            int ruleNum = Integer.parseInt(st.nextToken()); // 1~100.000(십만)

            // 건물을 짓는데 걸리는 시간 (0~100,000=십만)
            int[] buildingTime = new int[buildingNum+1];
            st = new StringTokenizer(br.readLine());
            for(int i=1; i<=buildingNum; i++){
                buildingTime[i] = Integer.parseInt(st.nextToken());
            }

            // 위상 정렬을 위한 자료구조
            Map<Integer, List<Integer>> graph = new HashMap<>();
            int[] inOrder = new int[buildingNum+1];

            // 건설 순서
            for(int i=0; i<ruleNum; i++){
                st = new StringTokenizer(br.readLine());
                int prev = Integer.parseInt(st.nextToken());
                int post = Integer.parseInt(st.nextToken());

                // inorder증가
                inOrder[post] += 1;

                // 그래프 관계 표시
                if(graph.containsKey(prev)){
                    graph.get(prev).add(post);
                }else{
                    List<Integer> adjs = new ArrayList<>();
                    adjs.add(post);
                    graph.put(prev, adjs);
                }
            }

            // 백준이가 승리하기 위해 건설해야할 건물 정보
            int targetBuilding = Integer.parseInt(br.readLine());

            // 위상 정렬 수행
            Queue<Building> queue = new PriorityQueue<>();

            for(int i=1; i<=buildingNum; i++){
                if(inOrder[i]==0) queue.add(new Building(i, buildingTime[i]));
            }

            while (!queue.isEmpty()){
                Building poll = queue.poll();
                //System.out.println(poll.num+":"+ poll.time+"초 걸려서 도착");

                if(poll.num==targetBuilding){
                    System.out.println(poll.time);
                    break;
                }

                // 뻗어나가는 인접 노드 없으면 continue;
                if(!graph.containsKey(poll.num)) continue;
                for(int adj: graph.get(poll.num)){
                    inOrder[adj] -= 1;
                    if(inOrder[adj]==0){
                        // adj빌딩번호와, adj 빌딩까지 세웠을 때의 시간을 큐에 넣기
                        queue.add(new Building(adj, poll.time+buildingTime[adj]));
                    }
                }
                //System.out.println(queue);
            }
        }
    }
}
