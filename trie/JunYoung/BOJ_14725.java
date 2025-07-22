import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 개미굴
 * - Trie의 노드에 알파벳 말고 단어가 올 수도 있다.
 */
public class BOJ_14725 {

  static class Node{
    Map<String, Node> childNode = new HashMap<>();
    boolean isEndOfWord;
  }

  static class Trie{
    Node rootNode = new Node();

    public void insert(List<String> path){
      // 항상 rootNode 부터 시작
      Node node = this.rootNode;

      for(int i=0; i<path.size(); i++){
        String s = path.get(i);
        node = node.childNode.computeIfAbsent(s, key -> new Node());
      }

      node.isEndOfWord = true;
    }

    public void printAll(){
      print(this.rootNode, 0);
    }
    public void print(Node node, Integer level){
      List<String> childKey = new ArrayList<>(node.childNode.keySet());
      Collections.sort(childKey); // 자식들 정렬

      for (String s: childKey){
        // 현재 레벨의 노드 출력
        Node currentNode = node.childNode.get(s);
        for (int l=0; l<level; l++){
          System.out.print("--");
        }
        System.out.println(s);
        print(currentNode, level+1);

      }
    }

  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int infoNum = Integer.parseInt(br.readLine());
    Trie antHouse = new Trie();

    // 각 개미의 정보
    for(int i=0; i<infoNum; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int num = Integer.parseInt(st.nextToken());
      List<String> path = new ArrayList<>();
      for(int j=0; j<num; j++){
        String s =st.nextToken();
        path.add(s);
      }
      antHouse.insert(path);
    }

    // 개미굴 정보 출력
    antHouse.printAll();
  }
}
