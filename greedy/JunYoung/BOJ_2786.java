import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 상근이의 레스토랑
 *
 * 각 음식은 첫번째 시킬 때 가격, 아닐 때의 가격이 존재
 * 음식을 1~N개 시킬 때 필요한 최소가격?
 * 같은 종류 음식 여러번 중복 주문 x
 *
 * 음식 개수(N) = 2~500,000(오십만)
 *
 * -----------------------------------------------
 * a의 최솟값 음식이 b로 선택되었을 때 b로 선택한 애들 중에서만 a의 후보를 골랐는데
 * b로 선택한 애들 중에서 a를 골랐을 때 + b로 선택하지 않은 애들 중에서 a고를 때 둘다 고려해야해!
 *
 * 나는 그냥 a의 최솟값만 생각하고, a의 2번째 최솟값?같은건 생각안해봄
 */
public class BOJ_2786 {
  static class Food implements Comparable<Food>{
    int index;
    int a;
    int b;

    Food(int index, int a, int b){
      this.index = index;
      this.a = a;
      this.b = b;
    }

    @Override
    public int compareTo(Food o) {
      return Integer.compare(this.b, o.b); // 오름차순
    }

    public String toString(){
      return this.index+"번째 음식 = "+ this.a+"/"+ this.b;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(br.readLine()); // 2 ~ 500,000(오십만)

    // b를 기준으로 오름차순 정렬하기
    Food[] foods = new Food[num];
    for(int i=0; i<num; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int aCost = Integer.parseInt(st.nextToken());
      int bCost = Integer.parseInt(st.nextToken());
      foods[i] = new Food(i, aCost, bCost);
    }
    Arrays.sort(foods);

    // i~N까지의 최소 a값 찾기
    int[] minAaboveI = new int[num];
    int minValue = 1000000001;
    for(int i=0; i<num; i++){
      if(foods[num-1-i].a<minValue){
        minValue = foods[num-1-i].a;
      }
      minAaboveI[num-1-i] = minValue;
    }

    // 3. 1~N까지 하나씩
    long sum = 0;
    int minGap = 2000000001;
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<num; i++){
      Food nowFood = foods[i];

      int gap = nowFood.a - nowFood.b;
      if (gap < minGap) {
        minGap = gap; // a-b
      }

      long newSum = Math.min(sum+minAaboveI[i], sum+ nowFood.b+minGap);
      sum+=nowFood.b;

      // 정답 출력
      sb.append(newSum+"\n");
    }
    System.out.println(sb);
  }
}
