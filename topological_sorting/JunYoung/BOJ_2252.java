import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 줄 세우기
 * 위상 정렬
 * -----------
 *
 * N명의 학생들을 키 순서대로 줄을 세우려고 한다.
 * 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
 *
 */
public class BOJ_2252 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    Integer N = Integer.parseInt(st.nextToken());
    Integer M = Integer.parseInt(st.nextToken());

    // 인접 리스트
    List<Integer>[] graph = new List[N+1];
    for(int i=0; i<N; i++){
      graph[i+1] = new ArrayList<>();
    }
    // indegree 배열
    int[] indegree = new int[N+1];

    // M = 키를 비교한 횟수
    for(int i=0; i<M; i++){
      st = new StringTokenizer(br.readLine());
      Integer studentA = Integer.parseInt(st.nextToken());
      Integer studentB = Integer.parseInt(st.nextToken());
      graph[studentA].add(studentB);
      indegree[studentB]++;
    }

    Deque<Integer> queue = new ArrayDeque<>();
    for(int i=1; i<=N; i++){
      if(indegree[i]==0) queue.add(i);
    }

    List<Integer> answer = new ArrayList<>();
    while(!queue.isEmpty()){
      Integer pop = queue.pop();
      answer.add(pop);

      for(Integer adj: graph[pop]){
        indegree[adj] -= 1;
        if(indegree[adj]==0){
          queue.add(adj);
        }
      }
    }

    for(int a: answer){
      System.out.print(a+" ");
    }

  }
}
