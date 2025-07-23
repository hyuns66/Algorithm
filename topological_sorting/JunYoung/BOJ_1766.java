import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 문제집
 *
 * N개의 문제는 모두 풀어야한다.
 * 먼저 푸는 게 좋은 문제는 반드시 먼저 푼다.
 * 가능하면 쉬운 문제부터 풀어야한다. (숫자가 낮은 문제)
 */
public class BOJ_1766 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 문제의 수 N / 먼저 푸는게 좋은 정보 개수 M
    Integer N = Integer.parseInt(st.nextToken());
    Integer M = Integer.parseInt(st.nextToken());


    // 위상 정렬
    int[] indegree = new int[N+1];
    List<Integer>[] graph = new List[N+1];
    for(int i=1; i<=N; i++){
      graph[i] = new ArrayList<>();
    }

    //
    for (int i=0; i<M; i++){
      st = new StringTokenizer(br.readLine());
      Integer problemA = Integer.parseInt(st.nextToken());
      Integer problemB = Integer.parseInt(st.nextToken());
      indegree[problemB] += 1;
      graph[problemA].add(problemB);
    }

    // 위상 정렬 로직
    PriorityQueue<Integer> queue = new PriorityQueue<>();
    for(int i=1; i<=N; i++){
      if(indegree[i]==0){
        queue.add(i);
      }
    }

    List<Integer> answer = new ArrayList<>();
    while(!queue.isEmpty()){
      Integer node = queue.poll();
      answer.add(node);

      for(Integer adj: graph[node]){
        indegree[adj] -= 1;
        if(indegree[adj]==0){
          queue.add(adj);
        }
      }
    }

    // 정답 출력
    for (int a: answer){
      System.out.print(a + " ");
    }
  }
}
