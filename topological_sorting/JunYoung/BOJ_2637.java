import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 장난감 조립
 *
 * 기본부품 -> 중간부품 -> 장난감
 *
 * 어떤 장난감 완제품과 그에 필요한 부품들의 관계가 주어졌을 때
 * 완제품을 위해 필요한 기본부품의 종류별 개수?
 * ==========================================================
 * 위상정렬로 풀긴 했는데..
 * DP론 어떻게 풀지..?
 */
public class BOJ_2637 {
  static class Node{
    int vertex;
    int inputNeed;

    Node(int vertex, int inputNeed){
      this.vertex = vertex;
      this.inputNeed = inputNeed;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int finalNum = Integer.parseInt(br.readLine());
    int infoNum = Integer.parseInt(br.readLine());

    // 인접그래프
    List<Node>[] graph = new ArrayList[finalNum+1];
    for(int i=1; i<=finalNum; i++){
      graph[i] = new ArrayList<>();
    }

    // indegree배열
    int[] indegree = new int[finalNum+1];
    int[] value = new int[finalNum+1];
    value[finalNum] = 1;

    for(int i=0; i<infoNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int output = Integer.parseInt(st.nextToken());
      int input = Integer.parseInt(st.nextToken());
      int inputNeed = Integer.parseInt(st.nextToken());

      // 인접리스트 (output->input 방향)
      graph[output].add(new Node(input, inputNeed));
      // indegree 배열
      indegree[input] += 1;
    }

    List<Integer> keys = new ArrayList<>();

    Deque<Integer> queue = new ArrayDeque();
    queue.add(finalNum);
    while(!queue.isEmpty()){
      Integer now = queue.pop();

      // 리프노드 = 기본부품
      if(graph[now].size()==0){
        // 기본 부품이라면
        keys.add(now);
      }

      // 인접리스트들에 대해
      for(Node adj: graph[now]){
        value[adj.vertex]+=value[now]*adj.inputNeed;
        indegree[adj.vertex] -=1;

        if(indegree[adj.vertex]==0){
          queue.add(adj.vertex);
        }
      }
    }

    Collections.sort(keys);
    for(int k: keys){
      System.out.printf("%d %d\n", k, value[k]);
    }

  }
}
