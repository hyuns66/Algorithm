import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_1068 {
  // 리프노드란, 자식의 개수가 0인 노드
  // 트리에서 노드 하나를 지울때, (그 노드의 자손도 제거된다.)
  // 남은 트리에서 리프 노드의 개수를 구하세요.

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 트리의 노두 수 = 1~50
    int treeNode = Integer.valueOf(br.readLine().trim());

    // 각 노드의 부모노드 (루트노드면 -1)
    Map<Integer, List<Integer>> childNode= new HashMap<>();
    Map<Integer, Integer> parentNode= new HashMap<>();
    for(int i=0; i<treeNode; i++){ // 빈 배열 생성
      childNode.put(i, new ArrayList<>());
    }

    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i=0; i<treeNode; i++){
      int pNode = Integer.parseInt(st.nextToken());
      if(pNode == -1) continue; // 부모노드면 자식이 아니니까 pass
      childNode.get(pNode).add(i);
      parentNode.put(i, pNode);
    }

    // 지울 노드의 번호
    int deleteNode = Integer.valueOf(br.readLine().trim());

    // 노드 삭제
    Deque<Integer> stack = new ArrayDeque<>();
    stack.add(deleteNode);
    while(!stack.isEmpty()){
      Integer dNode = stack.pop();
      Integer pNode = parentNode.get(dNode);
      if(childNode.get(pNode)!=null) {
        childNode.get(pNode).remove(Integer.valueOf(dNode)); // 부모리스트에서 자기 삭제
      }

      if(childNode.get(dNode)!=null && childNode.get(dNode).size()!=0){ // 리프노드가 아니면
        for(int dChild : childNode.get(dNode)) {
          stack.add(dChild);
        }
      }

      childNode.remove(dNode); // 자기자신 삭제
    }

    // 리프노드의 개수 구하기
    int leafNodeNum = 0;
    for(int parent : childNode.keySet()){
//      System.out.println("----------");
//      System.out.println(parent);
//      System.out.println(childNode.get(parent));
//      System.out.println("----------");
      if(childNode.get(parent)!=null && childNode.get(parent).size()==0){ // 리프노드
        leafNodeNum++;
      }
    }

    System.out.println(leafNodeNum);
  }

}