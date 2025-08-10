import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 구간 나누기2
 *
 * N개의 수로 이루어진 1차원 배열 (1~5,000)
 * 이 배열의 M개 이하의 구간으로 나누어 구간 점수의 최댓값을 최소로 하려고 한다. (1~10,000)
 *
 * 구간의 조건
 * 1. 하나의 구간은 하나이상의 연속된 수들
 * 2. 배열의 각 수는 모두 하나의 구간에 포함되어 있어야한다.
 *
 * 구간의 점수
 *  - 구간에 속한 수의 최댓값과 최솟값의 차이
 *  ((최댓값과 최솟값의 차이를 최소로!))
 *
 *  4,4,6 -> 6
 *  4,5,4 -> 5
 *
 *  https://dingdingmin-back-end-developer.tistory.com/entry/%EB%B0%B1%EC%A4%80-13397%EC%9E%90%EB%B0%94-java-%EA%B5%AC%EA%B0%84-%EB%82%98%EB%88%84%EA%B8%B0-2
 *  어렵당!
 */
public class BOJ_13397 {

  static int[] array;
  static int MAX = 10001;
  static int MIN = 0;

  public static void main(String[] args) throws IOException  {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int num = Integer.parseInt(st.nextToken());
    int splitNum = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());

    array = new int[num];
    int min = MAX;
    int max = MIN;
    for(int i=0; i<num; i++){
      array[i] = Integer.parseInt(st.nextToken());
      min = Math.min(min, array[i]);
      max = Math.max(max, array[i]);
    }

    // 최댓값과 최솟값의 차이는 0~max-min 사이에 존재
    // 해당값을 이분탐색으로 찾기
//    int left = 0;
//    int right = max-min;
//    while(left<right){
//      int mid = (left+right)/2;
//      if(solve(mid)<=splitNum){
//        right = mid;
//      }else{
//        left = mid+1;
//      }
//    }

    // 따로 이분 탐색 안해두 되네..
    int answer = -1;
    for(int target=0; target<=max-min; target++){
      if(solve(target)<=splitNum){
        answer = target;
        break;
      }
    }


    System.out.println(answer);
  }

  private static int solve(int mid) {
    int count = 1;
    int min = MAX;
    int max = MIN;
    for(int i=0; i< array.length; i++){
      min = Math.min(min, array[i]);
      max = Math.max(max, array[i]);
      if(max-min>mid){ // 이런게 있어서 조심해야해.. (MAX, MIN 설정할 때)
        // 목표하는 최대-최소차이를 넘으면 구간 나누기
        count++;
        // 초기화
        min = MAX;
        max = MIN;
        i--;
      }
    }
    return count;
  }
}
