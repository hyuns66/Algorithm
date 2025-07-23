import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 음악 프로그램
 *
 * 보조 PD들이 만든 순서들이 입력으로 주어질 때 전체 가수의 순서를 정하는 프로그램
 * 만일 모두를 만족하는 순서를 정하는게 불가능하면 0을 출력
 */

public class BOJ_2623 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    int[] indegree = new int[N+1];
    List<Integer>[] graph = new List[N+1];
    for(int i=1; i<=N; i++){
      graph[i] = new ArrayList<>();
    }

    for(int i=0; i<M; i++){
      st = new StringTokenizer(br.readLine());
      int inputNum = Integer.parseInt(st.nextToken());
      int prev = Integer.parseInt(st.nextToken());
      for(int j=1; j<inputNum; j++){
        int next = Integer.parseInt(st.nextToken());
        indegree[next] += 1;
        graph[prev].add(next);

        prev = next;
      }
    }

    // 위상 정렬
    Queue<Integer> queue = new ArrayDeque();
    for (int i=1; i<=N; i++){
      if(indegree[i]==0){
        queue.add(i);
      }
    }

    List<Integer> answer = new ArrayList<>();
    while(!queue.isEmpty()){
      Integer poll = queue.poll();
      answer.add(poll);

      for(int adj: graph[poll]){
        indegree[adj] -= 1;
        if(indegree[adj]==0){
          queue.add(adj);
        }
      }
    }

    // 정답 출력
    if(answer.size()==N){
      for(int a: answer){
        System.out.println(a);
      }
    }else{
      System.out.print(0);
    }

  }
}
