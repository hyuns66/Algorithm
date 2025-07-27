import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 선수 과목
 *
 * 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
 * 모든 과목은 매 학기 항상 개설된다.
 *
 * -> 각 과목을 이수하려면 최소 몇 학기가 걸리는가
 *
 * =============================================
 *
 * 위상 정렬로 풀이함. -> 위상정렬의 시간복잡도는 어떻게 되지?
 */
public class BOJ_14567 {

  static class Node{
    private int node;
    private int level;

    public Node(int node, int level) {
      this.node = node;
      this.level = level;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 과목의 수 (1~1000)
    int N = Integer.parseInt(st.nextToken());
    // 선수 조건의 수 (0~500000) 5십만
    int M = Integer.parseInt(st.nextToken());

    // 인접 그래프
    List<Integer>[] graph = new List[N+1];
    for(int i=1; i<=N; i++){
      graph[i] = new ArrayList<>();
    }
    // indegree 배열
    int[] indegree = new int[N+1];
    int[] answer = new int[N+1];

    for(int i=0; i<M; i++){
      st = new StringTokenizer(br.readLine());
      int subjectA = Integer.parseInt(st.nextToken());
      int subjectB = Integer.parseInt(st.nextToken());
      graph[subjectA].add(subjectB);
      indegree[subjectB] += 1;
    }

    Queue<Node> queue = new ArrayDeque<>();

    for(int i=1; i<=N; i++){
      if(indegree[i]==0){
        queue.add(new Node(i, 1));
      }
    }

    while (!queue.isEmpty()){
      Node current = queue.poll();
      answer[current.node] = current.level;

      for(int adj: graph[current.node]){
        indegree[adj] -= 1;
        if(indegree[adj]==0){
          queue.add(new Node(adj, current.level+1));
        }
      }
    }

    for(int a=1; a<=N; a++){
      System.out.print(answer[a]+ " ");
    }

  }
}
