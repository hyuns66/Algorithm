import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 문자열 지옥에 빠진 호석
 *
 * 이 세상은 N행 M열의 격자로 생겼으며
 * 각 칸에 알파벳이 써있고 환형으로 이어진다.
 *
 * 왼쪽 위 (1,1) 오른쪽 아래 (N,M)
 * 아무곳에서나 시작해서 상하좌우, 대각선 방향으로 이동 가능
 * 지나왔던 칸 다시 방문 가능
 *
 * 시작 격자를 시작으로, 이동하는 격자의 알파벳을 이어붙여서 문자열을 만들 수 있다.
 *
 * 신이 좋아하는 문자열 K개
 * 각 문자열마다 너가 만들 수 있는 경우의 수를 잘 대답하기
 *
 * 환형
 */
public class BOJ_20166 {
  static class Node{
    Map<Character, Node> childNode = new HashMap<>();
    boolean isEndOfWord;
    int count;
  }

  public static class Trie{
    Node rootNode = new Node();

    void insert(String str){
      Node node = rootNode;

      for(int i=0; i<str.length(); i++){
        node = node.childNode.computeIfAbsent(str.charAt(i), key-> new Node());
      }

      node.isEndOfWord = true;
      node.count++;
    }

    int search(String str){ // 원래는 boolean을 리턴하나 이 문제는 경우의 수를 출력해야하기에
      Node node = rootNode;

      for(int i=0; i<str.length(); i++){
        node = node.childNode.getOrDefault(str.charAt(i), null);
        if(node == null){
          return 0;
        }
      }

      if(node.isEndOfWord){
        return node.count;
      }
      return 0;
    }
  }

  static Trie trie;
  static char[][] arr;
  static int[] dy = {-1,1,0,0,-1,-1,1,1};
  static int[] dx = {0,0,-1,1,-1,1,-1,1};

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int row = Integer.parseInt(st.nextToken());
    int col = Integer.parseInt(st.nextToken());
    int godLike = Integer.parseInt(st.nextToken());

    trie = new Trie();
    arr = new char[row][col];
    for(int i=0; i<row; i++){
      String s = br.readLine();
      for(int j=0; j<col; j++){
        arr[i][j] = s.charAt(j);
      }
    }

    for(int i=0; i<row; i++){
      for(int j=0; j<col; j++){
        dfs(row, col, i, j, "", 0);
      }
    }

    // 신이 좋아하는 문자열
    for(int i=0; i<godLike; i++){
      String s = br.readLine();
      System.out.println(trie.search(s));
    }

  }

  static void dfs(int maxRow, int maxCol, int cRow, int cCol, String s, int length){
    s+=arr[cRow][cCol];
    length++;
    trie.insert(s);

    if(length>=5) return; // 신이 좋아하는 문자열중에 5이상은 없음

    for(int i=0; i< dy.length; i++){
      int nRow = cRow+dy[i];
      int nCol = cCol+dx[i];

      // 환형 적용
      nRow%=maxRow;
      nCol%=maxCol;
      if(nRow<0) nRow+=maxRow;
      if(nCol<0) nCol+=maxCol;

      dfs(maxRow,maxCol, nRow, nCol, s, length);
    }
  }
}
