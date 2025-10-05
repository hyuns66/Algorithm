import javax.swing.plaf.synth.SynthUI;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 숨바꼭질 3
 *
 * 수빈이는 점 N(0~100,000=십만)
 * 동생은 점 K(0~100,000)에 있다.
 *
 * 수빈이는 걷거나 순간이동을 할 수 있다.
 * 만약, 수빈이의 위치가 X일때 걷는다면 1초후에는 X-1, 또는 X+1이다.
 * 순간이동을 하는 경우, 0초후에 2*X의 위치로 이동하게 된다.
 *
 * 동생을 찾을 수 있는 가장 빠른 시간이 몇 초후인지?
 */
public class BOJ_13549 {
    static class Node implements Comparable<Node>{
        int vertex;
        int second;

        Node (int vertex, int second){
            this.vertex = vertex;
            this.second = second;
        }

        public int compareTo(Node o){
            return Integer.compare(this.second, o.second); // 적은 시간 순, 오름차순 정렬
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int myVertex = Integer.parseInt(st.nextToken());
        int targetVertex = Integer.parseInt(st.nextToken());

        // myPos노드부터 targetPos노드까지 갈 수 있는 최단거리를 구할꺼다.
        // 다익스트라를 쓰되, 인접리스트는 미리 만들지 않는다.

        PriorityQueue<Node> pq = new PriorityQueue<>();
        Map<Integer, Integer> dist = new HashMap<>(); // 노드번호, 걸리는 초

        // 시작점은 현재 수빈이의 위치인 myPos
        dist.put(myVertex, 0);
        pq.add(new Node(myVertex, 0));

        // 다익스트라 시작
        while (!pq.isEmpty()){
            Node curNode = pq.poll();
            int curSecond = curNode.second;
            int curVertex = curNode.vertex;
            //System.out.println(curVertex+"노드에 "+curSecond+"초 도착");

            if(curVertex== targetVertex) {
                System.out.println(curSecond);
                return;
            }

            // 현재 저장되어있는 거리값과 같지 않으면 pass
            if(!dist.getOrDefault(curVertex, -1).equals(curSecond)) continue;

            // N-1로 걸어서 이동
            if(curVertex-1>=0 && dist.getOrDefault(curVertex-1, Integer.MAX_VALUE)>curSecond+1){
                dist.put(curVertex-1, curSecond+1);
                pq.add(new Node(curVertex-1, curSecond+1));
            }

            // N+1로 걸어서 이동
            if(curVertex+1<=100000 && dist.getOrDefault(curVertex+1, Integer.MAX_VALUE)>curSecond+1){
                dist.put(curVertex+1, curSecond+1);
                pq.add(new Node(curVertex+1, curSecond+1));
            }

            // 2N으로 순간이동
            if(2*curVertex<=100000 && dist.getOrDefault(2*curVertex, Integer.MAX_VALUE)>curSecond){
                dist.put(2*curVertex, curSecond);
                pq.add(new Node(2*curVertex, curSecond));
            }
        }
    }
}
