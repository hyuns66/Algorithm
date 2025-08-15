import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 휴대폰 자판
 *
 * 길이가 P인 영단어를 입력하려면 버튼을 P번 눌러야한다.
 * 입력 더 빠른 모듈
 * : 사전 내에 가능한 글자가 하나 뿐이라면 그 글자를 버튼 입력 없이 자동으로 입력해준다.
 * 1. 모듈이 단어의 첫번째 글자를 추론하진 X (사전의 모든 단어가 같은 알파벳으로 시작하더라도 첫글자는 버튼을 눌러 입력해야한다.)
 * 2. c1c2..cn이 입력됐을 때, 해당 문자열로 시작하는 글자 c가 존재한다면 자동으로 c를 입력해준다.
 *
 *  사전이 주어졌을 때 이 모듈을 사용하면서,
 *  각 단어를 입력하기 위해 버튼을 눌러야하는 횟수의 평균은?
 */
public class BOJ_5670 {

  static class Node{
    Map<Character, Node> childNode = new HashMap<>();
    boolean isEndOfWord;
  }

  static class Trie{
    Node rootNode = new Node();

    public void insert(String str){
      Node node = rootNode;

      // 문자열의 각 단어마다 가져와서 자식노드 중에 있는지 체크
      for(int i=0; i<str.length(); i++){
        // 없으면 자식노드 새로 생성
        node = node.childNode.computeIfAbsent(str.charAt(i), key-> new Node());
      }

      // 저장할 문자열의 마지막 단어에 매핑되는 노드에 단어의 끝임을 명시
      node.isEndOfWord = true;
    }

    // [[ Trie에서 문자열 검색 ]]
    int searchCount(String str){
      // 항상 rootNode 부터 시작
      Node node = this.rootNode;

      int count = 0;
      boolean hasStopped = false;
      // 문자열의 각 단어마다 노드가 존재하는지 체크
      for(int i=0; i<str.length(); i++){
        // 문자열이 존재하지 않는 경우
        if(node.childNode.containsKey(str.charAt(i))==false){
          return -1;
        }

        count++;
        // 자동 완성 가능한지
//        System.out.println(str.charAt(i)+"/"+node.childNode.size());
//        System.out.println(node.childNode);
        if(i!=0&&node.childNode.size()==1){
          if(!hasStopped){ // 앞에서 한번 끝겼으면
//            System.out.println(str.charAt(i)+"자동완성됨");
            count--; // 자동완성
//            System.out.println(hasStopped+"로 바뀜!");
          }
        }

        if(node.childNode.get(str.charAt(i)).isEndOfWord) hasStopped = true;
        else hasStopped = false;
        node = node.childNode.get(str.charAt(i));
      }

      // 문자열의 마지막 단어까지 매핑된 노드가 존재한다고 그 문자열이 있는건 아님
      // 해당 노드가 단어의 끝인지 체크해야하마
      if(node.isEndOfWord){
        return count;
      }else{
        return -1;
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String line;
    while ((line=br.readLine())!=null){
      // 테스트 케이스 시작
      Trie trie = new Trie();
      int wordNum = Integer.parseInt(line);
      List<String> words = new ArrayList<>();
      for(int i=0; i<wordNum; i++){
        String s = br.readLine();
        words.add(s);
        trie.insert(s);
      }

      int sum = 0;
      for(int i=0; i<wordNum; i++){
        int n = trie.searchCount(words.get(i));
        sum+=n;
        //System.out.println(n);
      }

      double avg = (double)sum/wordNum;
      System.out.println(String.format("%.2f", avg));
    }


  }
}
